

import matplotlib.pyplot as plt
import numpy as np
#from matplotlib.animation import FuncAnimation
import matplotlib.animation as animation



class Pendulum:

    def __init__(self, alpha_grad, g, l, m, rK, deltaR, anzahlT):

        # Die Konstanten und Parameter
        self.alpha_grad = alpha_grad
        self.alpha = (np.pi * self.alpha_grad) / 180  # Auslenkungswinkel in rad
        self.g = g  # Gravitationsbeschleunigung in m/(s^2)
        self.l = l  # Länge des Pendels in m
        self.m = m  # Masse des Pendelkörpers in kg
        self.rK = rK  # Radius des Pendelkörpers in m
        self.deltaR = deltaR  # Dämpfungskonstante der Reibungskraft in kg/s (für Luft 0.07)
        self.omega0 = (self.g / self.l) ** (0.5)  # Kreisfrequenz des harmonischen Pendels ohne Dämpfung in 1/s
        self.T0 = (2 * np.pi) / self.omega0  # Periode des harmonischen Pendels ohne Dämpfung in s
        self.T = self.T0 * (1 + (2 * self.rK ** 2 / (5 * self.l ** 2))) ** (0.5)  # Periode des harmonischen Pendels
        #   mit Dämpfung in s
        self.tau = 2 * self.m / self.deltaR  # Zeitkonstante des harmonischen Pendels mit Dämpfung in s
        self.omegaR = self.omega0 * (1 - (1 / (self.tau * self.omega0)) ** 2) ** (0.5)  # Kreisfrequenz des harmonischen
        #   Pendels ohne Dämpfung in 1/s
        self.anzahlT = anzahlT  # Anzahl der Perioden des harmonischen Pendels


    def p_steps(self):
        # Die Zeitschritte für  Perioden

        self.stepHalf = 0.01            # Zeitschrittversatz in s für die Berechnung der Winkelgeschwindigkeit
                                        #   omegaAlphaA der Änderung des Winkels alpha des
                                        #   anharmonischen Pendels (Numerische Lösung der DGL nach Feynman)
        self.step = 2 * self.stepHalf   # Zeitschrittversatz in s für die Berechnung des Winkels alpha
                                        #   und Winkelbeschleunigung aAlphaA des anharmonischen Pendels
                                        #   (Numerische Lösung der DGL nach Feynman)
        self.anzahlStepT = round(self.T / self.step, 0)                      # Anzahl der Zeitschritte pro eine Periode
        self.t = np.arange(0, self.anzahlT * self.T, self.stepHalf)     # Zeit in s für die Berechnung insgesamt
        self.stepV = 1                                                  # Schrittversatz wegen Winkelgeschwindigkeit
        self.numSteps = len(self.t) - self.stepV                        # Anzahl der Iterationen für die numerische Lösung der DGL

    def p_arrays(self):
        # Arrays für die Berechnung von aharmonischen und harmonischen Lösung

        self.alphaA = np.zeros(len(self.t))         # Array des Auslenkungswinkels anharmonisch
        self.omegaAlphaA = np.zeros(len(self.t))    # Array der Winkelgeschwindigkeit anharmonisch
        self.aAlphaA = np.zeros(len(self.t))        # Array der Winkelbeschleunigung anharmonisch

        self.alphaH = np.zeros(len(self.t))         # Array des Auslenkungswinkels harmonisch
        self.omegaAlphaH = np.zeros(len(self.t))    # Array der Winkelgeschwindigkeit harmonisch
        self.aAlphaH = np.zeros(len(self.t))        # Array der Winkelbeschleunigung harmonisch



    def p_calc(self):
        # Anfangsbedienungen

        self.alphaA[0] = self.alpha                                     # Anfangswert des Auslenkungswinkels anharmonisch
        self.aAlphaA[0] = -(self.omega0 ** 2) * np.sin(self.alphaA[0])  # Anfangswert der Winkelbeschleunigung anharmonisch
        self.omegaAlphaA[0] = 0                                         # Anfangswert der Winkelgeschwindigkeit anharmonisch
        self.omegaAlphaA[1] = self.omegaAlphaA[0] + self.stepHalf * self.aAlphaA[0]     # Wert der Winkelgeschwindigkeit
                                                                                        #   zw. ersten und zweiten
                                                                                        #   Zeitschritt anharmonisch
        self.phi = 0                                                                    # Phasenverschiebung
        self.alphaH[0] = self.alpha                                                     # Anfangswert des Auslenkungswinkels harmonisch
        self.aAlphaH[0] = -(self.omega0 ** 2) * self.alphaH[0]                          # Anfangswert der Winkelbeschleunigung harmonisch
        self.omegaAlphaH[0] = 0                                                         # Anfangswert der Winkelgeschwindigkeit harmonisch
        self.omegaAlphaH[1] = self.alphaH[0] * (-1) * np.sin(self.omega0 * self.t[1] + self.phi) * self.omega0  # Wert der Winkelgeschwindigkeit
                                                                                                                #  zw. ersten und zweiten
                                                                                                                #   Zeitschritt harmonisch

        # Berechnungen von anharmonischen und harmonischen Lösungen
        self.i_s = np.arange(2, self.numSteps, 2)
        for i in self.i_s:  # die ungerade i entspricht step für das Auslenkungswinkel und die Winkelbeschleunigung die gerade i entspricht stepHalf für die Winkelgeschwindigkeit
            self.alphaA[i] = self.alphaA[i - 2] + self.step * (self.omegaAlphaA[i - 1])  # Berechnung des Auslenkungswinkels anharmonisch
            self.aAlphaA[i] = -(self.omega0 ** 2) * np.sin(self.alphaA[i])  # Berechnung der Winkelbeschleunigung  anharmonisch
            self.omegaAlphaA[i + 1] = (self.omegaAlphaA[i - 1] + self.step * self.aAlphaA[i]) * (1 - (self.deltaR / (self.anzahlStepT * self.m)))  # Berechnung der Winkelgeschwindigkeit anharmonisch

            self.alphaH[i] = self.alphaH[0] * np.exp(-self.t[i] / self.tau) * np.cos(self.omegaR * self.t[i] + self.phi)  # Berechung des Auslenkungswinkels harmonisch
            self.aAlphaH[i] = -(self.omega0 ** 2) * self.alphaH[i]  # Berechnung der Winkelbeschleunigung harmonisch
            self.omegaAlphaH[i + 1] = self.alphaH[0] * (-1) * np.sin(self.omegaR * self.t[i + 1] + self.phi) * self.omegaR  # Berechnung der  Winkelgeschwindigkeit  harmonisch

        # linewidth
        self.alphaAn = self.alphaA[0:-1:2]
        self.alphaHn = self.alphaH[0:-1:2]
        self.tn = self.t[0:-1:2]
        self.alphaAnB = self.alphaAn[0:-1:2]
        self.alphaHnB = self.alphaHn[0:-1:2]
        self.tnB = self.tn[0:-1:2]
        # figure parameters
        self.figcolor = 'lightgrey'
        self.plotcolor = 'whitesmoke'
        self.hmarkercolor = 'royalblue'
        self.amarkercolor = 'forestgreen'
        self.title = 'Physikalisches Pendel mit Reibung,\naharmonische und harmonische Lösung'
        self.ylabel = r'Auslenkungswinkel $\alpha$ / °'
        self.xlabel = 'Zeit t / s'
        self.pendelA_str = 'aharmonische Lösung'
        self.pendelH_str = 'harmonische Lösung'


class PendulumFig(Pendulum):
    """ A class to generate a figure."""

    def __init__(self, alpha_grad, g, l, m, rK, deltaR, anzahlT, us):
        """Inizialize attributes of a figure"""
        self.us = us
        super().__init__(alpha_grad, g, l, m, rK, deltaR, anzahlT)


    def p_fig_t(self):
        figT = plt.figure(figsize=(5, 4), dpi=200)
        ax1 = figT.add_subplot(111)

        figT.set_facecolor(color=self.figcolor)
        ax1.set_facecolor(color=self.plotcolor)

        #print(len(tn), len(alphaAn))

        # ax1.plot(xRay, yRay, linewidth=1, alpha=1.0, color='grey')


        ax1.scatter(self.tn, self.alphaHn,  s=5, alpha=0.8, color=self.hmarkercolor, label=self.pendelH_str)
        ax1.scatter(self.tn, self.alphaAn, s=5, alpha=0.8, color=self.amarkercolor, label=self.pendelA_str)

        # Title x- and ylabel
        ax1.set_xlim(self.tn[0], self.tn[-1])
        ax1.set_ylim(-1.57, 1.57)
        ax1.axhline(y=0, xmin=0, xmax=1, color='grey')
        ax1.set_title(self.title, fontsize=10)
        ax1.set_xlabel(self.xlabel, fontsize=8)
        ax1.set_ylabel(self.ylabel, fontsize=8)

        ax1.tick_params(axis='both', which='both', labelsize=6)
        ax1.grid(which='both', color='grey', linestyle=':', linewidth=0.5)
        ax1.set_yticks(ticks=[-1.57, -1.05, -0.52, 0.0, 0.52, 1.05, 1.57], minor=False)
        ax1.set_yticklabels(labels=['-90', '-60', '-30', '0', '30', '60', '90'], fontdict=None, minor=False)
        #ax.get_yaxis().set_visible(False)
        ax1.legend(loc='best', labelcolor='black', facecolor=self.figcolor, edgecolor='grey', fontsize=8)
        pen_show = f'm_app1/media/pendulum/pen_show_{self.us}.png'
        plt.savefig(pen_show, dpi='figure', facecolor=self.figcolor, edgecolor='grey',
                            orientation='portrait', format='png',
                            transparent=False, bbox_inches=None, pad_inches=None,
                            metadata=None)

        #plt.show()
        plt.close()
        x_max = round(self.tn[-1], 1)
        #print(x_max)
        return x_max


class PendulumFigAnim(Pendulum):
    """ A class to generate animation."""

    def __init__(self, alpha_grad, g, l, m, rK, deltaR, anzahlT, us):
        self.us = us
        """Inizialize attributes of an animation."""
        super().__init__(alpha_grad, g, l, m, rK, deltaR, anzahlT)



    def p_fig_t_anim(self):
        figA = plt.figure(figsize=(5, 4), dpi=150)
        axA = figA.add_subplot(111)

        figA.set_facecolor(color=self.figcolor)

        xdata, ydataA, ydataH, kdata = [], [], [], []
        alphaAnA, = plt.plot([], [], '.', alpha=0.8, color=self.amarkercolor, label=self.pendelA_str)
        alphaAnH, = plt.plot([], [], '.', alpha=0.9, color=self.hmarkercolor, label=self.pendelH_str)

        def init():
            axA.set_facecolor(color=self.plotcolor)
            axA.grid(which='both', color='grey', linestyle=':', linewidth=0.5)
            axA.set_title(self.title, fontsize=10)
            axA.set_xlabel(self.xlabel, fontsize=8)
            axA.set_ylabel(self.ylabel, fontsize=8)

            axA.set_xlim(self.tn[0], self.tn[-1])
            axA.set_ylim(-1.57, 1.57)
            axA.tick_params(axis='both', which='both', labelsize=6)
            axA.grid(which='both', color='grey', linestyle=':', linewidth=0.5)
            axA.set_yticks(ticks=[-1.57, -1.05, -0.52, 0.0, 0.52,  1.05, 1.57 ],  minor=False)
            axA.set_yticklabels(labels=['-90', '-60', '-30', '0', '30', '60', '90'],  fontdict=None, minor=False)
            axA.axhline(y=0, xmin=0, xmax=1, color='grey')
            axA.legend(loc='best', labelcolor='black', facecolor=self.figcolor, edgecolor='grey', fontsize=8)
            return alphaAnH, alphaAnA,

        def update(frame):
            xdata.append(frame)
            k = xdata.index(frame)
            ydataA.append(self.alphaAnB[k])
            ydataH.append(self.alphaHnB[k])
            alphaAnA.set_data(xdata, ydataA)
            alphaAnH.set_data(xdata, ydataH)

            #print(frame, k)
            return alphaAnH, alphaAnA,

        anim = animation.FuncAnimation(figA, update, frames=self.tnB[0:-1],
                            init_func=init, blit=True)
        writervideo = animation.FFMpegWriter(fps=30)


        anim_v = f'm_app1/media/pendulum/anim_v_{self.us}.mp4'
        anim.save(anim_v, writer=writervideo)
        #plt.show()
        plt.close()
        prv = False
        return prv


    def p_polar_fig_anim(self):

        figP = plt.figure(figsize=(5, 4), dpi=150)
        #axP = figP.add_subplot(111)
        axP = plt.subplot(1, 1, 1, projection='polar')
        #figP, axP = plt.subplots(subplot_kw={'projection': 'polar'})
        figP.set_facecolor(color=self.figcolor)

        alphaAnA, = plt.plot([], [], '-', color=self.amarkercolor, alpha=0.7)
        alphaAnADot, = plt.plot([], [], 'o', color=self.amarkercolor, alpha=0.9, label=self.pendelA_str)
        alphaHnA, = plt.plot([], [], '-', color=self.hmarkercolor, alpha=0.7)
        alphaHnADot, = plt.plot([], [], 'o', color=self.hmarkercolor, alpha=0.9, label=self.pendelH_str)

        def init():
            axP.set_facecolor(color=self.plotcolor)
            #axP.grid(which='both', color='grey', linestyle=':', linewidth=0.5)
            axP.set_title(self.title, fontsize=10)
            #axP.set_rlabel("Länge des Pendels l/m", fontsize=14)
            #axP.set_thetalabel("Auslenkungswinkel alpha/rad", fontsize=14)
            axP.tick_params(labelsize=8)
            axP.set_rmax(self.l*(1+0.2))
            axP.set_thetamax(180)
            axP.set_theta_direction(1)
            axP.set_theta_zero_location(loc='W', offset=0.0)
            #axP.set_rticks([0.5, 1, 1.5, 2])  # Less radial ticks
            #axP.set_rgrids(radii, labels=None, angle=None, fmt=None, **kwargs)
            axP.set_thetagrids(angles=[0, 30, 60, 90, 120, 150, 180],
                              labels=['-90', '-60', '-30', '0', '30', '60', '90'], fmt=None)
            axP.legend(loc='best', labelcolor='black', facecolor=self.figcolor, edgecolor='grey', fontsize=8)

            return alphaAnA,


        def update(i):
            my_rDot = [self.l] # dot
            my_r = [0., self.l] # line
            my_thetaH = [(self.alphaHnB[i] + np.pi / 2), (self.alphaHnB[i] + np.pi / 2)]
            my_thetaA = [(self.alphaAnB[i] + np.pi / 2), (self.alphaAnB[i] + np.pi / 2)]

            alphaHnADot.set_data(my_thetaH, my_rDot)  # move dot
            alphaHnA.set_data(my_thetaH, my_r)  # move line aharmonic
            alphaAnADot.set_data(my_thetaA, my_rDot) # move dot
            alphaAnA.set_data(my_thetaA, my_r) # move line aharmonic


            #print(i)
            return  alphaAnA, alphaAnADot, alphaHnA, alphaHnADot

        anim = animation.FuncAnimation(figP, update, (len(self.alphaAnB)-1), interval=(1/(len(self.alphaAnB)-1))*1000,
                            init_func=init, blit=True)
        writervideo = animation.FFMpegWriter(fps=30)
        anim_x = f'm_app1/media/pendulum/anim_x_{self.us}.mp4'
        anim.save(anim_x, writer=writervideo)
        #plt.show()
        plt.close()
        prx = False
        return prx
