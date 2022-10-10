'''
ga.py
Manages algorithms for evolving
'''

from tsp_ga.population import Population
from tsp_ga.route import Route
from random import random


class GA:
    def __init__(self):
        self.mutation_rate = 0.015
        self.tournament_size = 5
        self.elitism = True
    
    def evolve(self, population):
        new_population = Population(population.size, False)
        new_population.routes = [-1] * population.size
        elitism_offset = 0
        if self.elitism:
            new_population.routes[0] = population.getFittest()
            elitism_offset = 1
        
        for index in range(elitism_offset, len(population.routes)):
            parent1 = self.tournament_selection(population)
            parent2 = self.tournament_selection(population)

            child = self.crossover(parent1, parent2)

            new_population.routes[index] = child

        for index in range(elitism_offset, len(new_population.routes)):
            self.mutate(new_population.routes[index])

        return new_population

    def crossover(self, parent1, parent2):
        child = Route()

        start_pos = round(random() * len(parent1.route))
        end_pos = round(random() * len(parent1.route))

        for index in range(child.routeSize()):
            if (start_pos < end_pos and index > start_pos and index < end_pos):
                child.setCity(index, parent1.getCity(index))
                if type(set(child.route)) != bool and len(child.route) != len(set(child.route)) and (-1 not in child.route):
                    print("DUPLICATES [49]: " + child.__str__())
                    quit()
            elif (start_pos > end_pos):
                if not (index < start_pos and index > end_pos):
                    child.setCity(index, parent1.getCity(index))
                    if type(set(child.route)) != bool and len(child.route) != len(set(child.route)) and (-1 not in child.route):
                        print("DUPLICATES [55]: " + child.__str__())
                        quit()

        for index in range(parent2.routeSize()):
            if not child.containsCity(parent2.getCity(index)):
                for index2 in range(child.routeSize()):
                    if child.getCity(index2) == -1:
                        child.setCity(index2, parent2.getCity(index))
                        if type(set(child.route)) != bool and len(child.route) != len(set(child.route)) and (-1 not in child.route):
                            print("DUPLICATES [64]: " + child.__str__())
                            quit()
                        break
        

        return child

    def mutate(self, route):
        pos1 = 0
        while pos1 < route.routeSize():
            if random() < self.mutation_rate:
                pos2 = round((route.routeSize()-1) * random())
            
                city1 = route.getCity(pos1)
                city2 = route.getCity(pos2)

                route.setCity(pos2, city1)
                route.setCity(pos1, city2)
            pos1 += 1

    def tournament_selection(self, population):
        tournament = Population(self.tournament_size, False)
        tournament.routes = [-1] * self.tournament_size
        for index in range(len(tournament.routes)):
            id = round(random() * len(population.routes)-1)
            tournament.routes[index] = population.routes[id]

        fittest = tournament.getFittest()
        return fittest
