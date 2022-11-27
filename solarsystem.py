class SolarSystem:
    def __init__(self, aSun):
        self.__theSun = aSun
        self.__planets = []

    def addPlanet(self, aPlanet):
        self.__planets.append(aPlanet)

    def showPlanets(self):
        for aPlanet in self.__planets:
            print(aPlanet)
