'''
route.py
Represents a route of cities, ie an individual in this GA problem
'''

from random import shuffle
from tsp_ga.route_manager import RouteManager

class Route:
    def __init__(self):
        self.route = [-1] * len(RouteManager.cities)
        self.fitness = 0
        self.distance = 0

    def createIndividual(self):
        for index, city in enumerate(RouteManager.cities):
            self.route[index] = city
        shuffle(self.route)

    def getCity(self, index):
        return self.route[index]

    def setCity(self, index, city):
        self.route[index] = city
        self.fitness = 0
        self.distance = 0

    def getFitness(self):
        if self.fitness == 0:
            self.fitness = 1/self.getDistance()
        return self.fitness

    def getDistance(self):
        distance = 0
        for index in range(0, len(self.route)-1):
            distance += self.route[index].distanceTo(self.route[index+1])
        distance += self.route[-1].distanceTo(self.route[0])
        self.distance = distance
        return distance

    def routeSize(self):
        return len(self.route)

    def containsCity(self, city):
        return city in self.route

    def __str__(self):    
        route_string = "<"
        for city in self.route:
            route_string += city.__str__
        route_string += ">"
        return route_string

    def routeCoords(self):
        resx = []
        resy = []
        for city in self.route:
            resx.append(city.x)
            resy.append(city.y)
        return [resx, resy]