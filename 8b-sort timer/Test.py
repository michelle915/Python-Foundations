
from matplotlib import pyplot

pyplot.plot([1, 2, 3, 4, 10], [1, 4, 9, 16, 100], 'ro--', linewidth=2, label='series 1')
pyplot.plot([1, 2, 3, 4, 10], [1, 3, 7, 20, 150], 'go--', linewidth=2, label='series 2')
pyplot.xlabel("the x label")
pyplot.ylabel("the y label")
pyplot.legend(loc='upper left')
pyplot.show()