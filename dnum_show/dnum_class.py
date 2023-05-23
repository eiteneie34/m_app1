import numpy as np
import matplotlib.pyplot as plt

class DnumEntry:

    def __init__(self, dnumInput, precInputDef):
        self.dnumInput = dnumInput
        self.precInputDef = precInputDef


    def dnum_fminus(self):
        if self.dnumInput[0] == "-":
            self.fminus = True
            self.dnumInput0 = self.dnumInput[1:]
        else:
            self.fminus = False
            self.dnumInput0 = self.dnumInput[:]
        return  self.dnumInput0, self.fminus


    def dnum_mminus(self):
        if '-' in self.dnumInput0:
            mminus = True
        else:
            mminus = False
        return mminus


    def dnum_passed(self):
        numberspass = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ',', '.']
        for n in self.dnumInput0:
            if n not in numberspass:
                passed = False
                break
            else:
                passed = True
        return   passed


    def dnum_lcomma(self):
        self.dnumInput1 = self.dnumInput0
        if ',' not in self.dnumInput0 and '.' not in self.dnumInput0:
            self.dnumInput1 = self.dnumInput0[:] + '.0'
        if self.dnumInput0[-1] == ',' or self.dnumInput0[-1] == '.':
            self.dnumInput1 = self.dnumInput0[:] + '0'
        return self.dnumInput1


    def dnum_fcomma(self):
        if self.dnumInput1[0] == "," or self.dnumInput1[0] == ".":
            self.dnumInput2 = "0" + self.dnumInput1[:]
        else:
            self.dnumInput2 = self.dnumInput1[:]
        return self.dnumInput2



    def dnum_dcomma(self):
        self.dcomma = False
        if ',' in self.dnumInput2 and self.dnumInput2.index(',') != self.dnumInput2.rindex(','):
            self.dcomma = True
        if '.' in self.dnumInput2 and self.dnumInput2.index('.') != self.dnumInput2.rindex('.'):
            self.dcomma = True
        if ',' in self.dnumInput2 and '.' in self.dnumInput2:
            self.dcomma = True
        return self.dcomma

        # fct I

    def dnum_Irow(self):
        self.dnumInput3 = self.dnumInput2
        if ',' in self.dnumInput2:
            self.dnumInput3 = self.dnumInput2.replace(',', '.')
        return self.dnumInput3

    def dnum_dnull(self):
        dnull = True
        xb = self.dnumInput3[:]
        ns = xb[0:2]
        n1 = xb[0]
        while dnull == True:
            if  ns != "0."  and  n1 =="0":
                xb = xb[1:]
                ns = xb[0:2]
                n1 = xb[0]
            else:
                self.dnumI = xb
                dnull = False
                return  self.dnumI

    def prec_default(self):
        precPass = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        if self.precInputDef not in precPass:
            self.precInputDef = "4"
        else:
            self.precInputDef = self.precInputDef[:]
        return self.precInputDef


class DnumNotation(DnumEntry):
    """ A class to generate random walks."""

    def __init__(self, dnumInput, precInputDef):
        """Inizialize attributes of a walk"""
        super().__init__(dnumInput, precInputDef)

    # fct DIN
    def dnum_DIN(self):
        self.dnumDIN = self.dnumI
        if '.' in self.dnumI:
            self.dnumDIN = self.dnumI.replace('.', ',')
        return self.dnumDIN



    # fct format to scientific notation
    def scientific_notation(self):
        self.dnumIf = float(self.dnumI)
        self.precInputDefi = int(self.precInputDef)
        self.dnumS = np.format_float_scientific(self.dnumIf, precision=self.precInputDefi, exp_digits=3)
        return self.dnumS


    def power_notation(self):
        mantissaInd = self.dnumS.index("e")
        self.dnumM = self.dnumS[0:mantissaInd]
        if ".e" in self.dnumS:
            self.dnumM = self.dnumS[0:mantissaInd] + '0'
        powerInd = self.dnumS.index("e") + 1
        numberSP = self.dnumS[powerInd:]
        if "-" in numberSP:
            self.dnumP = "-"
            self.dnumP += numberSP.lstrip("-0")

        if "+" in numberSP:
            self.dnumP = numberSP.lstrip("+0")
            if self.dnumP == "":
                self.dnumP = "0"
        return self.dnumM, self.dnumP




class DnumShiftFig():
    """ A class to generate random walks."""

    def __init__(self, fminus, dnumM, dnumP, us):
        self.fminus, self.dnumM, self.dnumP, self.us = fminus, dnumM, dnumP, us
        self.dnumMshift, self.dnumPshift = dnumM, dnumP


    def shift_comma_str(self, lrInput):
        numberSMR, numberSPkR = self.dnumM, int(self.dnumP)
        nC = numberSMR.index('.')
        if lrInput == "l":
            numberSPkR += 1
            if numberSMR[0] != '0':
                numberSMR = numberSMR[0:nC - 1] + numberSMR[nC] + numberSMR[nC - 1] + numberSMR[nC + 1:]
                if numberSMR[0] == '.':
                    numberSMR = "0" + numberSMR[:]
                if ".00" in numberSMR:
                    numberSMR = numberSMR[:-1]
                if numberSMR[-3] == '.' and numberSMR[-1] == '0':
                    numberSMR = numberSMR[:-1]

            else:
                numberSMR = numberSMR[0:nC + 1] + "0" + numberSMR[nC + 1:]
                if numberSMR[-2:-1] == "00":
                    numberSMR = numberSMR[:-2]

        if lrInput == "r":

            numberSPkR -= 1
            if numberSMR[0] != '0':
                numberSMR = numberSMR[0:nC] + numberSMR[nC + 1] + numberSMR[nC] + numberSMR[nC + 2:]
                if numberSMR[-1] == '.':
                    numberSMR = numberSMR[:] + "0"

            else:
                numberSMR = numberSMR[0:nC] + numberSMR[nC + 1] + numberSMR[nC] + numberSMR[nC + 2:]
                if numberSMR[-1] == '0':
                    numberSMR = numberSMR[:-1]
                if numberSMR[0:2] == "00":
                    numberSMR = numberSMR[1:]
                if numberSMR[0] == '.':
                    numberSMR = "0" + numberSMR[:]
                if numberSMR[0] == '0' and numberSMR[1] != '0' and numberSMR[1] != '.':
                    numberSMR = numberSMR[1:]
                if numberSMR[-1] == '.':
                    numberSMR = numberSMR[:] + "0"

        self.dnumMshift, self.dnumPshift = str(numberSMR), str(numberSPkR)
        return self.dnumMshift, self.dnumPshift


    def prefix(self):
        dnumPrefixDic = {
            '-24': {'prefix': 'Yokto', 'abb': 'y'},
            '-21': {'prefix': 'Zepto', 'abb': 'z'},
            '-18': {'prefix': 'Atto', 'abb': 'a'},
            '-15': {'prefix': 'Femto', 'abb': 'f'},
            '-12': {'prefix': 'Piko', 'abb': 'p'},
            '-9': {'prefix': 'Nano', 'abb': 'n'},
            '-6': {'prefix': 'Mikro', 'abb': 'u'},
            '-3': {'prefix': 'Milli', 'abb': 'm'},
            '-2': {'prefix': 'Zenti', 'abb': 'c'},
            '-1': {'prefix': 'Dezi', 'abb': 'd'},
            '1': {'prefix': 'Deka', 'abb': 'da'},
            '2': {'prefix': 'Hekto', 'abb': 'h'},
            '3': {'prefix': 'Kilo', 'abb': 'k'},
            '6': {'prefix': 'Mega', 'abb': 'M'},
            '9': {'prefix': 'Giga', 'abb': 'G'},
            '12': {'prefix': 'Tera', 'abb': 'T'},
            '15': {'prefix': 'Peta', 'abb': 'P'},
            '18': {'prefix': 'Exa', 'abb': 'E'},
            '21': {'prefix': 'Zetta', 'abb': 'Z'},
            '24': {'prefix': 'Yotta', 'abb': 'Y'}

        }
        self.dnumAbb, self.dnumPrefix = 'n.a.', 'n.a.'
        for n, p in dnumPrefixDic.items():
            if n == self.dnumPshift:
                self.dnumAbb = p['abb']
                self.dnumPrefix = p['prefix']
        return self.dnumAbb, self.dnumPrefix


    def minus(self, fminus):
        if fminus == True:
            signum = '-'
        else:
            signum = ''
        return signum

    # figure number ray
    def dnum_ray(self):
        if self.fminus==True:
            dnum_f = (-1)*float(self.dnumM) * 10 ** int(self.dnumP)
            len_dnumP = len(self.dnumP)
            if len_dnumP == 1:
                dnum_str = f'{self.dnumM} ·10' + fr'$^{self.dnumP[0]}$'
            if len_dnumP == 2:
                dnum_str = f'{self.dnumM} ·10' + fr'$^{self.dnumP[0]}$' + fr'$^{self.dnumP[1]}$'
            if len_dnumP == 3:
                dnum_str = f'{self.dnumM} ·10' + fr'$^{self.dnumP[0]}$' + fr'$^{self.dnumP[1]}$' + fr'$^{self.dnumP[2]}$'

            xRayMax = (-1)*10 ** int(self.dnumP)
            xRayMin = (-1)*10 ** (int(self.dnumP) + 1)

        else:
            dnum_f = float(self.dnumM) * 10 ** int(self.dnumP)
            len_dnumP = len(self.dnumP)
            if len_dnumP==1:
                dnum_str = f'{self.dnumM} ·10' + fr'$^{self.dnumP[0]}$'
            if len_dnumP==2:
                dnum_str = f'{self.dnumM} ·10' + fr'$^{self.dnumP[0]}$' + fr'$^{self.dnumP[1]}$'

            if len_dnumP == 3:
                dnum_str = f'{self.dnumM} ·10' + fr'$^{self.dnumP[0]}$' + fr'$^{self.dnumP[1]}$' + fr'$^{self.dnumP[2]}$'


            xRayMin = 10 ** int(self.dnumP)
            xRayMax = 10 ** (int(self.dnumP) + 1)
            if float(self.dnumM)==0.0:
                xRayMin = -3.0
        xRay = [xRayMin, xRayMax]
        yRay = [0.0, 0.0]
        # plt.style.use('bmh')
        figD = plt.figure(figsize=(5, 4), dpi=200)
        axD = figD.add_subplot(111)
        #figD, ax = plt.subplots()
        figD.set_facecolor(color='lightgrey')
        axD.set_facecolor(color='whitesmoke')

        # linewidth
        axD.plot(xRay, yRay, linewidth=1, alpha=0.7, color='navy')

        axD.scatter(dnum_f, 0.0, s=50, alpha=1.0, color='navy', label=dnum_str)

        # Title x- and ylabel
        axD.set_title("Dezimalzahl auf dem Zahlenstrahl", fontsize=10)
        axD.set_xlabel("Reelle Zahlen R", fontsize=8)
        axD.tick_params(axis='both', which='both', labelsize=6)
        axD.axis([xRayMin, xRayMax, -1, 1])
        axD.grid(which='both', color='grey', linestyle=':', linewidth=0.5)
        axD.set_yticks(ticks=[-1.0, -0.75, -0.5, -0.25, 0.0, 0.25, 0.5, 0.75, 1.0], minor=False)
        axD.set_yticklabels(labels=['-1', '', '', '', '0', '', '', '', '1'], fontdict=None, minor=False)
        #ax.get_yaxis().set_visible(False)
        axD.legend(loc='best', labelcolor='navy', facecolor='whitesmoke', edgecolor='grey', fontsize=8)
        dnum_ray = f'm_app1/media/dnumray/dnum_ray_{self.us}.png'
        plt.savefig(dnum_ray, dpi=200, facecolor='lightgrey', edgecolor='grey',
                    orientation='portrait', format=None,
                    transparent=False, bbox_inches=None, pad_inches=0.1,
                    metadata=None)

        plt.close()

"""
# test
dnumInput = '0,00,4'
my1_dnum = DnumNotation(dnumInput, '4')
my1_dnumInput0, my1_fminus = my1_dnum.dnum_fminus()
my1_mminus = my1_dnum.dnum_mminus()
my1_passed = my1_dnum.dnum_passed()
my1_dnumInput1 = my1_dnum.dnum_lcomma()
my1_dnumInput2 = my1_dnum.dnum_fcomma()
my1_dcomma = my1_dnum.dnum_dcomma()
my1_dnumInput3 = my1_dnum.dnum_Irow()
precInputDef = my1_dnum.prec_default()
if my1_mminus == True or my1_passed == False or my1_dcomma == True:
    dnumDIN, dnumI, dnumS, dnumM, dnumP = "Eingabefehler!", 'n.a.', 'n.a.', 'n.a.', 'n.a.'
else:
    dnumI = my1_dnum.dnum_dnull()
    dnumDIN = my1_dnum.dnum_DIN()
    dnumS = my1_dnum.scientific_notation()
    dnumM, dnumP = my1_dnum.power_notation()

print ('my1_mminus', my1_mminus, 'my1_passed', my1_passed, 'my1_dcomma', my1_dcomma,
        '\nmy1_dnumInput1', my1_dnumInput1, 'my1_dnumInput2', my1_dnumInput2, 'my1_dnumInput3', my1_dnumInput3,
        '\ndnumDIN', dnumDIN,
        '\ndnumI', dnumI,
        '\ndnumS', dnumS,
        '\ndnumM,  dnumP', dnumM, dnumP,
        '\ndnumMshift, t.dnumPshift', dnumM, dnumP,

)
"""
