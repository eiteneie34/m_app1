from random import choice
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np


class RandomWalk:
    """ A class to generate random walks."""

    def __init__(self, num_points, x_distance_str, y_distance_str):
        """Inizialize attributes of a walk"""
        self.num_points = num_points
        self.x_distance_str, self.y_distance_str = x_distance_str, y_distance_str
        self.point_numbers = range(self.num_points)
        self.point_numbers_random = np.random.rand(len(self.point_numbers))
        self.fig_c = 'lightgrey'

        # Alle Bewegungen beginnen bei (0. 0).
        self.x_values = [0]
        self.y_values = [0]


    def str_float_list(self, seq_str):
        seq_i = []
        seq_str_list = list(seq_str.split(" "))
        #seq_str_list = seq_str_list_row[0:-2]
        #print(seq_str_list_row)
        #print(seq_str_list)
        for k in seq_str_list:
            seq_i.append(float(k))
        #print(seq_i)
        return seq_i


    def str_int_list(self, seq_str):
        seq_i = []
        seq_str_list = list(seq_str.split(" "))
        #seq_str_list = seq_str_list_row[0:-2]
        #print(seq_str_list_row)
        #print(seq_str_list)
        for k in seq_str_list:
            seq_i.append(int(k))
        #print(seq_i)
        return seq_i


    def int_str_list(self, seq_i):
        seq_str_row = ''.join([str(elem) + ' ' for elem in seq_i])
        seq_str = seq_str_row.rstrip(" ")
        return seq_str


    def fill_walk(self):
        """Calculate all points in the walk"""

        # Führt Schritte aus, bis der Pfad die angegebene Länge erreicht hat.

        while len(self.x_values) < self.num_points:

            # Wählt die Richtung und die weglänge in dieser Richtung aus.
            x_distance_i, y_distance_i = self.str_int_list(self.x_distance_str), self.str_int_list(self.y_distance_str)
            x_direction = choice([1, -1])

            x_distance = choice(x_distance_i)
            x_step = x_direction * x_distance

            y_direction = choice([1, -1])

            y_distance = choice(y_distance_i)
            y_step = y_direction * y_distance

            # Lehnt Bewegungen ab, die nicht vom Fleck führen
            if x_step == 0 and y_step == 0:
                continue

            # Berechnet den nächsten x- und y-Wert.
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step


            self.x_values.append(x)
            self.y_values.append(y)

        x_values, y_values = self.int_str_list(self.x_values), self.int_str_list(self.y_values)
        point_numbers_random = self.int_str_list(self.point_numbers_random)
        return x_values, y_values, point_numbers_random


class RandomFigure(RandomWalk):
    """ A class to generate a figure."""

    def __init__(self, num_points,x_distance_str, y_distance_str,  us):
        """Inizialize attributes of a figure"""
        self.us = us

        super().__init__(num_points, x_distance_str, y_distance_str)


    def rw_figure(self, dot_marker='.', dot_size=5, dot_size_v = False, dot_color='White', dot_alpha=1.0, dot_alpha_v = False, dot_cmap='Purples', ax_color='darkblue' ):
        xmin = np.min(self.x_values)
        xmax = np.max(self.x_values)
        ymin = np.min(self.y_values)
        ymax = np.max(self.y_values)
        fig_r = plt.figure(figsize=(5, 4), dpi=200)
        ax_r = fig_r.add_subplot(111, xlim=(xmin, xmax), ylim=(ymin, ymax),)

        fig_r.set_facecolor(color=self.fig_c)

        ax_r.set_facecolor(color=ax_color)
        point_numbers = self.point_numbers

        if dot_size_v == True:
            s_arr = np.round(dot_size * (1 + 5*self.point_numbers_random), 1)
            dot_size = s_arr

        if dot_alpha_v == True:
            a_arr = np.round(dot_alpha * (1 - 0.2*self.point_numbers_random), 1)
            a_arr1 = np.where(a_arr < 1.0, a_arr, 1.0)
            a_arr2 = np.where(a_arr1 > 0.01, a_arr1, 0.1)
            dot_alpha = a_arr2


        if dot_cmap=='n':
            if dot_marker == '(4,1)':
                dot_marker = (4, 1)
            if dot_marker == '(5,2)':
                dot_marker = (5, 2)
            if dot_marker == '(6,2)':
                dot_marker = (6, 2)
            if dot_marker == '(7,1)':
                dot_marker = (7, 1)
            if dot_marker == '(9,1)':
                dot_marker = (9, 1)
            if dot_marker == '(7,2)':
                dot_marker = (7, 2)
            if dot_marker == '(7,2)':
                dot_marker = (8, 2)
            if dot_marker == '(8,1)':
                dot_marker = (8, 1)
            if dot_marker == '(8,2)':
                dot_marker = (8, 2)
            if dot_marker == '(9,2)':
                dot_marker = (9, 2)
            ax_r.scatter(self.x_values, self.y_values, marker=dot_marker, s=dot_size, alpha=dot_alpha, color=dot_color)

        else:
            if dot_marker == '(4,1)':
                dot_marker = (4, 1)
            if dot_marker == '(5,2)':
                dot_marker = (5, 2)
            if dot_marker == '(6,2)':
                dot_marker = (6, 2)
            if dot_marker == '(7,1)':
                dot_marker = (7,1)
            if dot_marker == '(9,1)':
                dot_marker = (9, 1)
            if dot_marker == '(7,2)':
                dot_marker = (7, 2)
            if dot_marker == '(7,2)':
                dot_marker = (8, 2)
            if dot_marker == '(8,1)':
                dot_marker = (8, 1)
            if dot_marker == '(8,2)':
                dot_marker = (8, 2)
            if dot_marker == '(9,2)':
                dot_marker = (9, 2)
            ax_r.scatter(self.x_values, self.y_values, marker=dot_marker, s=dot_size, alpha=dot_alpha, c=point_numbers, cmap=dot_cmap)

        ax_r.get_xaxis().set_visible(False)
        ax_r.get_yaxis().set_visible(False)
        rw_visual = f'm_app1/media/rwvisual/rw_visual_{self.us}.png'
        plt.savefig(rw_visual, dpi=200, facecolor=self.fig_c, edgecolor='w',
                    orientation='portrait', format=None,
                    transparent=False, bbox_inches=None, pad_inches=0.1,
                    metadata=None)
        #plt.show()
        plt.close()


class RandomFigureAnim(RandomWalk):
    """ A class to generate an animation."""

    def __init__(self, num_points, x_distance_str, y_distance_str, point_numbers_random_str, x_values_str, y_values_str, us):

        """Inizialize attributes of an animation"""
        self.us = us
        self.x_values_str, self.y_values_str, self.point_numbers_random_str = x_values_str, y_values_str, point_numbers_random_str
        #print(self.x_values_str, self.y_values_str)
        self.x_values_a, self.y_values_a, self.point_numbers_random_a = self.str_int_list(self.x_values_str), self.str_int_list(self.y_values_str), self.str_float_list(self.point_numbers_random_str)
        super().__init__(num_points, x_distance_str, y_distance_str)


    def ran_fig_anim(self, dot_marker='.', dot_size=500, dot_size_v=False, dot_color='White', dot_alpha=1.0, dot_alpha_v=False, dot_cmap='Purples', ax_color='darkblue' ):
        p = []

        i=0
        while i < self.num_points:
            p.append(i)
            i += 1

        xmin = np.min(self.x_values_a)
        xmax = np.max(self.x_values_a)
        ymin = np.min(self.y_values_a)
        ymax = np.max(self.y_values_a)
        fig_n = plt.figure(figsize=(5, 4), dpi=150)
        ax_n = fig_n.add_subplot(111, xlim=(xmin, xmax), ylim=(ymin, ymax),)

        fig_n.set_facecolor(color=self.fig_c)
        ax_n.set_facecolor(color=ax_color)

        if dot_cmap == 'n':
            if dot_marker == '(4,1)':
                dot_marker = (4, 1)
            if dot_marker == '(5,2)':
                dot_marker = (5, 2)
            if dot_marker == '(6,2)':
                dot_marker = (6, 2)
            if dot_marker=='(7,1)':
                dot_marker=(7,1)
            if dot_marker == '(9,1)':
                dot_marker = (9, 1)
            if dot_marker == '(7,2)':
                dot_marker = (7, 2)
            if dot_marker == '(7,2)':
                dot_marker = (8, 2)
            if dot_marker == '(8,1)':
                dot_marker = (8, 1)
            if dot_marker == '(8,2)':
                dot_marker = (8, 2)
            if dot_marker == '(9,2)':
                dot_marker = (9, 2)
            rn = plt.scatter(x=[self.x_values_a[0]], y=[self.y_values_a[0]],   marker=dot_marker, s=dot_size, alpha=dot_alpha, color=dot_color)
        else:
            if dot_marker == '(4,1)':
                dot_marker = (4, 1)
            if dot_marker == '(5,2)':
                dot_marker = (5, 2)
            if dot_marker == '(6,2)':
                dot_marker = (6, 2)
            if dot_marker=='(7,1)':
                dot_marker=(7,1)
            if dot_marker == '(9,1)':
                dot_marker = (9, 1)
            if dot_marker == '(7,2)':
                dot_marker = (7, 2)
            if dot_marker == '(7,2)':
                dot_marker = (8, 2)
            if dot_marker == '(8,1)':
                dot_marker = (8, 1)
            if dot_marker == '(8,2)':
                dot_marker = (8, 2)
            if dot_marker == '(9,2)':
                dot_marker = (9, 2)

            point_numbers = range(self.num_points)
            c_map = plt.get_cmap(dot_cmap)
            my_numbers = []
            my_cmap = []
            for kp in point_numbers:
                my_numbers.append(kp / len(point_numbers))
                my_cmap.append(c_map(my_numbers[kp]))
            rn = plt.scatter(x=[self.x_values_a[0]], y=[self.y_values_a[0]], marker=dot_marker, s=dot_size, alpha=dot_alpha, color=my_cmap[0])

        def init():
            rn.set_offsets([])
            ax_n.get_xaxis().set_visible(False)
            ax_n.get_yaxis().set_visible(False)
            return rn,

        def update(frame):

            k = p.index(frame)

            rn.set_offsets([self.x_values_a[k],
                            self.y_values_a[k]])
            if dot_cmap != 'n':
                rn.set_color(my_cmap[k])



            return rn,

        anim = animation.FuncAnimation(fig_n, update, frames=p[0:-1],
                            init_func=init, blit=True)

        writervideo = animation.FFMpegWriter(fps=30)
        anim_n = f'm_app1/media/rwvisual/rw_visual_n_{self.us}.mp4'
        anim.save(anim_n, writer=writervideo)
        #plt.show()
        plt.close()


    def ran_fig_anim2(self, dot_marker='.', dot_size=500, dot_size_v=False, dot_color='White', dot_alpha=1.0, dot_alpha_v=False, dot_cmap='Oranges', ax_color='darkblue' ):
        p = []
        i = 0
        while i < self.num_points:
            p.append(i)
            i += 1
        dot_size_i = int(dot_size)
        dot_alpha_i = float(dot_alpha)
        xmin = np.min(self.x_values_a)
        xmax = np.max(self.x_values_a)
        ymin = np.min(self.y_values_a)
        ymax = np.max(self.y_values_a)
        fig_n2 = plt.figure(figsize=(5, 4), dpi=150)
        ax_n2 = fig_n2.add_subplot(111, xlim=(xmin, xmax), ylim=(ymin, ymax))

        fig_n2.set_facecolor(color=self.fig_c)
        ax_n2.set_facecolor(color=ax_color)

        if dot_cmap == 'n':
            if dot_marker == '(4,1)':
                dot_marker = (4, 1)
            if dot_marker == '(5,2)':
                dot_marker = (5, 2)
            if dot_marker == '(6,2)':
                dot_marker = (6, 2)
            if dot_marker=='(7,1)':
                dot_marker=(7,1)
            if dot_marker == '(9,1)':
                dot_marker = (9, 1)
            if dot_marker == '(7,2)':
                dot_marker = (7, 2)
            if dot_marker == '(7,2)':
                dot_marker = (8, 2)
            if dot_marker == '(8,1)':
                dot_marker = (8, 1)
            if dot_marker == '(8,2)':
                dot_marker = (8, 2)
            if dot_marker == '(9,2)':
                dot_marker = (9, 2)

            if dot_size_v == True:
                s_arr = []
                for d in self.point_numbers_random_a:
                    s = round(float(dot_size_i) * (1.0 + 5*d), 2)
                    s_arr.append(s)
                    dot_size_arr = s_arr
                rn = plt.scatter(x=[self.x_values_a[0]], y=[self.y_values_a[0]], marker=dot_marker, s=dot_size_arr[0],
                                alpha=dot_alpha, color=dot_color)

            rn = plt.scatter(x=[self.x_values_a[0]], y=[self.y_values_a[0]],   marker=dot_marker, s=dot_size,
                                alpha=dot_alpha, color=dot_color)

        else:
            if dot_marker == '(4,1)':
                dot_marker = (4, 1)
            if dot_marker == '(5,2)':
                dot_marker = (5, 2)
            if dot_marker == '(6,2)':
                dot_marker = (6, 2)
            if dot_marker=='(7,1)':
                dot_marker=(7,1)
            if dot_marker == '(9,1)':
                dot_marker = (9, 1)
            if dot_marker == '(7,2)':
                dot_marker = (7, 2)
            if dot_marker == '(7,2)':
                dot_marker = (8, 2)
            if dot_marker == '(8,1)':
                dot_marker = (8, 1)
            if dot_marker == '(8,2)':
                dot_marker = (8, 2)
            if dot_marker == '(9,2)':
                dot_marker = (9, 2)

            #print(self.point_numbers_random_a)


                #print(s_arr)


            point_numbers = range(self.num_points)
            c_map = plt.get_cmap(dot_cmap)
            my_numbers = []
            my_cmap = []
            for kp in point_numbers:
                my_numbers.append(kp / len(point_numbers))
                my_cmap.append(c_map(my_numbers[kp]))


            if dot_size_v == True:
                s_arr = []
                for d in self.point_numbers_random_a:
                    s = round(float(dot_size_i) * (1.0 + 5*d), 2)
                    s_arr.append(s)
                    dot_size_arr = s_arr

                rn = plt.scatter(x=[self.x_values_a[0]], y=[self.y_values_a[0]], marker=dot_marker, s=dot_size_arr[0],
                                 alpha=dot_alpha, color=my_cmap[0])

            rn = plt.scatter(x=[self.x_values_a[0]], y=[self.y_values_a[0]], marker=dot_marker, s=dot_size,
                                alpha=dot_alpha, color=my_cmap[0])

        def init():
            rn.set_offsets([])
            ax_n2.get_xaxis().set_visible(False)
            ax_n2.get_yaxis().set_visible(False)
            return rn,

        def update(frame):

            k = p.index(frame)


            xdata = self.x_values_a[:k]
            ydata = self.y_values_a[:k]

            rn.set_offsets(np.c_[xdata, ydata])
            if dot_size_v == True:
                rn.set_sizes(dot_size_arr[:k])
                #print(dot_size_arr[k])
            #if dot_alpha_v == True:
            #    rn.set_alpha(dot_alpha_arr[:k])
            #    print(dot_alpha_arr[k])
            if dot_cmap != 'n':
                rn.set_color(my_cmap[:k])


            return rn,

        anim = animation.FuncAnimation(fig_n2, update, frames=p[0:-1],
                            init_func=init, blit=True)

        writervideo = animation.FFMpegWriter(fps=30)
        anim_n2 = f'm_app1/media/rwvisual/rw_visual_n2_{self.us}.mp4'
        anim.save(anim_n2, writer=writervideo)
        #plt.show()
        plt.close()
        pr = False
        return pr





#my_fig_a = RandomFigureAnim2(num_points=100, us='Eugen')
#my_fig_a.fill_walk()
#my_fig_a.ran_fig_anim2(dot_marker='*', dot_size=400, dot_color='gold', dot_alpha=float(0.7), dot_cmap='Oranges', ax_color='navy')

#my_fig_a = RandomFigureAnim(num_points=100, us='Eugen')
#my_fig_a.fill_walk()
#my_fig_a.ran_fig_anim(dot_marker='*', dot_size=500, dot_color='gold', dot_alpha=float(0.7), dot_cmap='Oranges', ax_color='navy')

#x_distance_str, y_distance_str = '0, 1, 2, 3, 4', '0, 1, 2, 3, 4'

#my_fig = RandomFigure(num_points=500, x_distance_str= '0 1 2 3 4', y_distance_str= '0 1 2 3 4', us='Eugen')
#my_fig.fill_walk()
#my_fig.rw_figure(dot_marker='*', dot_size=20, dot_size_v=True, dot_color='gold', dot_alpha=float(0.5), dot_alpha_v=True, dot_cmap='Oranges', ax_color='navy')

