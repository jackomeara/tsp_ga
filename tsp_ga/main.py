from tsp_ga.city import City
from tsp_ga.ga import GA
from tsp_ga.population import Population
from tsp_ga.route_manager import RouteManager
import matplotlib.pyplot as plt
from tqdm import tqdm
from time import perf_counter

if __name__ == '__main__':
    num_cities = 70
    pop_size = 100
    gens = 400
    mRate = GA().mutation_rate
    elitism = GA().elitism
    tournament_size = GA().tournament_size
    sims = 50


    RouteManager.cities = [City() for i in range(20)]


    X = []
    Y = []
    for city in RouteManager.cities:
        X.append(city.x)
        Y.append(city.y)


    def display(gens, dist, coords, X=X, Y=Y, pop_size=pop_size):
        plt.scatter(X, Y)
        plt.plot(coords[0], coords[1])
        plt.title("Distance: %s | %s Gens | Pop.Size: %s" % (round(dist, 3), gens, pop_size))
        plt.show()

    pop = Population(pop_size, True)

    firstd, firstcoords = (pop.getFittest().getDistance(), pop.getFittest().routeCoords())


    pop = GA().evolve(pop)
    for i in tqdm(range(gens)):
        if i % 50 == 0:
            display(i, pop.getFittest().getDistance(), pop.getFittest().routeCoords())
        pop = GA().evolve(pop)

    lastd, lastcoords = (pop.getFittest().getDistance(), pop.getFittest().routeCoords())

    print("First Distance: %s" % round(firstd, 3))
    print("Final Distance: %s" % round(lastd, 3))