'''
population.py
Holds the population of routes
'''

from tsp_ga.route import Route

class Population:
    def __init__(self, size:int, init:bool):
        self.routes = []
        self.size = size
        if init:
            for _ in range(size):
                newRoute = Route()
                newRoute.createIndividual()
                self.routes.append(newRoute)

    def getRoute(self, index):
        return self.routes[index]

    def getFittest(self):
        fittest = self.routes[0]
        for route in self.routes:
            if route.getFitness() > fittest.getFitness():
                fittest = route
        return fittest
