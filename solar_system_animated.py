# A Solar system must have a Sun and one or more Planets
# a Planet may have one or more Moon. It also may have zero Moons
# Planets rotate around the Sun, the rotation periods may be different.
# Moons rotate around the Planets, the rotation periods may be different.
# Each solar object has name, size, distance from Sun, velocity
# 

import turtle
import math

class SolarSystem:
    EARTH_RADIUS = 1.5
    EARTH_DISTANCE = 1
    EARTH_MASS = 1
    
    def __init__(self, width, height):
        self.__theSun = None
        self.__planets = []
        self.__ssTurtle = turtle.Turtle()
        self.__ssTurtle.hideturtle()
        self.__ssScreen = turtle.Screen()
        self.__ssScreen.setworldcoordinates(-width/2.0, -height/2.0,
                                             width/2.0, height/2.0)

    def addPlanet(self, aPlanet):
        self.__planets.append(aPlanet)

    def addSun(self, aSun):
        self.__theSun = aSun

    def showPlanets(self):
        for aPlanet in self.__planets:
            aPlanet.print_name()
            
    def movePlanets(self):
        G = .1
        dt = .001

        for p in self.__planets:
            p.moveTo(p.getXPos() + dt * p.getXVel(),
                     p.getYPos() + dt * p.getYVel())

            rX = self.__theSun.getXPos() - p.getXPos()
            rY = self.__theSun.getYPos() - p.getYPos()
          
            r = math.sqrt(rX**2 + rY**2)

            accX = G * self.__theSun.getMass() * rX/r**3
            accY = G * self.__theSun.getMass() * rY/r**3

            p.setXVel(p.getXVel() + dt * accX)
            p.setYVel(p.getYVel() + dt * accY) 


    def freeze(self):
        self.__ssScreen.exitonclick() 

class Sun:
    def __init__(self, iName, iRad, iM, iTemp):
        self.__name = iName
        self.__radius = iRad
        self.__mass = iM
        self.__temp = iTemp
        self.__x = 0
        self.__y = 0

        self.__sTurtle = turtle.Turtle()
        self.__sTurtle.turtlesize(self.__radius * SolarSystem.EARTH_RADIUS)

        self.__sTurtle.shape("circle")
        self.__sTurtle.color("yellow")

    def getMass(self):
        return self.__mass

   #other methods as before

    def getXPos(self):
        return self.__x

    def getYPos(self):
        return self.__y

class Planet:
    def __init__(self, iName, iRad, iM, iDist, iVx, iVy, iC):
        self.__name = iName
        self.__radius = iRad
        self.__mass = iM
        self.__moons = []
        self.__distance = iDist
        self.__velX = iVx
        self.__velY = iVy 

        self.__x = self.__distance
        self.__y = 0
        self.__color = iC

        self.__pTurtle = turtle.Turtle()

        self.__pTurtle.color(self.__color)
        self.__pTurtle.shape("circle")
        self.__pTurtle.turtlesize(self.__radius * SolarSystem.EARTH_RADIUS)

        self.__pTurtle.up()
        self.__pTurtle.goto(self.__x,self.__y)
        self.__pTurtle.down()

    def addMoon(self, aMoon):
        self.__moons.append(aMoon)


    #other methods as before

    def print_name(self):
        print(self.__name)
        for mo in self.__moons:
            mo.print_name()
        return

    def getXPos(self):
        return self.__x

    def getYPos(self):
        return self.__y

    def moveTo(self, newX, newY):
        self.__x = newX
        self.__y = newY
        self.__pTurtle.goto(self.__x, self.__y)

    def getXVel(self):
        return self.__velX

    def getYVel(self):
        return self.__velY

    def setXVel(self, newVx):
        self.__velX = newVx

    def setYVel(self, newVy):
        self.__velY = newVy 

class Moon(Planet):
    def __init__(self, iName):
        self.__name = iName

    def move(self):
        pass
    
    def getName(self):
        return self.__name

    def print_name(self):
        print("  " + self.__name)

def createSSandAnimate():
    ss = SolarSystem(2, 2)

    sun = Sun("Sun", 3.5, 10, 5800)
    ss.addSun(sun)
    
    m = Planet(iName="Mercury", iRad=0.4, iM=5000 * 0.055, iDist=.25, iVx=0, iVy=4.14, iC="blue")
    ss.addPlanet(m)

    m = Planet("Venus", 0.8, 5000 * 0.815, .35, 0, 1.27, "magenta")
    ss.addPlanet(m)


    m = Planet("Earth", 1, 5000, 0.5, 0, 1, "green")
    m1 = Moon("Earths Moon")
    
    m.addMoon(m1)
    # m.print_name()
 
    ss.addPlanet(m)

    m = Planet("Mars", 0.9, 5000 * 0.107, 0.7, 0, 0.53, "orange")
    m1 = Moon("Phobos")
    m.addMoon(m1)
    m1 = Moon("Deimos")
    m.addMoon(m1)

    ss.addPlanet(m)

    m = Planet("Jupiter", 2, 5000 * 318, 1, 0, 0.1, "black")
    m1 = Moon("Ganymede")
    m.addMoon(m1)

    ss.addPlanet(m)

    # ss.showPlanets()

    numTimePeriods = 2000
    for aMove in range(numTimePeriods):
        ss.movePlanets()

    ss.freeze()

# createSSandAnimate()