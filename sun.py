class Sun:
    def __init__(self, iName, iRad, iM, iTemp):
        self.__name = iName
        self.__radius = iRad
        self.__mass = iM
        self.__temp = iTemp

    def getMass(self):
        return self.__mass

    def __str__(self):
        return self.__name


