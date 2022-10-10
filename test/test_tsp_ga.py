import tsp_ga
from tsp_ga.city import City
from tsp_ga.ga import GA
from tsp_ga.population import Population
from tsp_ga.route_manager import RouteManager
from tsp_ga.route import Route

import unittest

class TestCity(unittest.TestCase):
    def test_city(self):
        c = City()
        c._x = 10
        c._y = 0

        c2 = City()
        c2._x = 0
        c2._y = 0

        self.assertEqual(c.x, 10)

        self.assertEqual(c.y, 0)

        self.assertEqual(c.distanceTo(c2), 10)

class TestGA(unittest.TestCase):
    def test_ga(self):
        pass

class TestPopulation(unittest.TestCase):
    def test_population(self):
        pass

class TestRoute(unittest.TestCase):
    def test_route(self):
        pass

class TestRouteManager(unittest.TestCase):
    def test_route_manager(self):
        pass