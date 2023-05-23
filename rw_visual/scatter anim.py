import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

num_points = 10

point_numbers = range(num_points)
cmap = cmap=plt.get_cmap('Oranges')
my_numbers = []
my_cmap = []
for p in point_numbers:
    my_numbers.append(p/len(point_numbers))
    my_cmap.append(cmap(my_numbers[p]))
print(my_numbers)
print(my_cmap)

figN = plt.figure(figsize=(5, 4), dpi=150)
axN = figN.add_subplot(111)
axN.plot(my_numbers, my_numbers, c=my_cmap[7])

plt.show()
