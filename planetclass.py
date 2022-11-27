class Planet:
    def __init__(self, iName, iRad, iM, iDist):
        self.__name = iName     # planētas nosaukums
        self.__radius = iRad    # rādiuss  
        self.__mass = iM        # masa
        self.__distance = iDist # attālums līdz saulei

    def getName(self):
        return self.__name

    def getRadius(self):
        return self.__radius

    def getMass(self):
        return self.__mass

    def getDistance(self):
        return self.__distance

    def getVolume(self):
        import math
        v = 4/3 * math.pi * self.__radius**3
        return v

    def getSurfaceArea(self):
        import math
        sa = 4 * math.pi * self.__radius**2
        return sa

    def getDensity(self):
        d = self.__mass / self.getVolume()
        return d

    def setName(self, newName):
        self.__name = newName 

    def setRadius(self, newRadius):
        self.__radius = newRadius 

    def setMass(self, newMass):
        self.__mass = newMass 

    def setDistance(self, newDistance):
        self.__distance = newDistance 

    def __str__(self):
        return self.__name
      
    def __lt__(self, otherPlanet):
        return self.__distance < otherPlanet.__distance

    def __gt__(self, otherPlanet):
        return self.__distance > otherPlanet.__distance  

