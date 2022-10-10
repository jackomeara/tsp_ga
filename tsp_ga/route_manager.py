'''
route_manager.py
Manages cities in our route
'''

class RouteManager():
    cities = []

    def addCity(city):
        global cities
        cities.append(city)

    def getCity(index):
        return cities[index]

    def numOfCities():
        return len(cities)