'''
city.py
Represents a city
'''

from random import randint
from math import sqrt

class City:
    def __init__(self):
        self._x = randint(0,250)
        self._y = randint(0,250)

    def _getX(self):
        return self._x

    def _getY(self):
        return self._y

    x = property(_getX)
    y = property(_getY)

    def __str__(self):
        return "%s,%s" % (self.x, self.y)

    def distanceTo(self, city):
        x_dist = self.x - city.x
        y_dist = self.y - city.y
        dist = sqrt((x_dist**2)+(y_dist**2))
        return round(dist, 2)