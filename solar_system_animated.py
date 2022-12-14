# A Solar system must have a Sun and one or more Planets
# a Planet may have one or more Moon. It also may have zero Moons
# Planets rotate around the Sun, the rotation periods may be different.
# Moons rotate around the Planets, the rotation periods may be different.
# Each solar object has name, size, distance from Sun, velocity
# 

import turtle
import math
import operator

class SolarSystem:
    EARTH_RADIUS = 1.5
    EARTH_DISTANCE = 1
    EARTH_ROTATION_SPEED = 0.01     # angular velocity in radians per program cycle. :)
    
    # A simplified edition treats the Sun as yet another planet, with a zero distance and a zero orbit radius.
    def __init__(self, width, height):
        # self.__theSun = None
        self.__planets = []
        self.__ssTurtle = turtle.Turtle()
        self.__ssTurtle.hideturtle()
        self.__ssScreen = turtle.Screen()
        
        self.__ssScreen.setworldcoordinates(-width/2.0, -height/2.0,
                                             width/2.0, height/2.0)

    def addPlanet(self, aPlanet):
        self.__planets.append(aPlanet)

    # def addSun(self, aSun):
    #     self.__theSun = aSun

    def showPlanets(self):
        for aPlanet in self.__planets:
            aPlanet.print_name()

    # Names of planets as well as the Sun are printed in an ascending order, based on the respective planet's distance from the Sun.
    # Sun is also included as per assignment condition.
    def showPlanetsByDistance(self):
        if len(self.__planets) < 1:
            print("No planets to show")
            return
        planets_sorted = sorted(self.__planets, key = lambda planet : planet.getDistance(),reverse=True)
        for aPlanet in planets_sorted:
            # Planet distance from the Sun is not shown, and Jupiter is to blame here.
            # Jupiter's distance should be much bigger than shown. 
            # Orbital radius for Mercury has also been slightly adjusted.
            print(aPlanet.getName()) # +" "+str(aPlanet.getDistance())+" AU")
    
    # Method to move the planets and the moons.
    def movePlanets(self):
        for p in self.__planets:
            p.angleMove()


    def freeze(self):
        self.__ssScreen.exitonclick() 

# Sun class not required.
# class Sun:
#     def __init__(self, iName, iRad, iM, iTemp):
#         self.__name = iName
#         self.__radius = iRad
#         self.__mass = iM
#         self.__temp = iTemp
#         self.__x = 0
#         self.__y = 0

#         self.__sTurtle = turtle.Turtle()
#         self.__sTurtle.turtlesize(self.__radius * SolarSystem.EARTH_RADIUS)

#         self.__sTurtle.shape("circle")
#         self.__sTurtle.color("gold")

#     def getMass(self):
#         return self.__mass

#     def getName(self):
#         return self.__name
    
#     def getXPos(self):
#         return self.__x

#     def getYPos(self):
#         return self.__y

class Planet:
    def __init__(self, i_object_name, i_object_radius, i_orbit_radius, i_angle_increment, i_color):
        
        self.__name = i_object_name
        self.__radius = i_object_radius
        self.__moons = []
        self.__distance = i_orbit_radius

        self.__x = self.__distance
        self.__y = 0
        self.__previous_x = self.__x
        self.__previous_y = self.__x
        self.__color = i_color

        self.__pTurtle = turtle.Turtle()
        self.__pTurtle.color(self.__color)
        self.__pTurtle.shape("circle")
        self.__pTurtle.turtlesize(self.__radius * SolarSystem.EARTH_RADIUS)

        self.__pTurtle.up()
        self.__pTurtle.goto(self.__x,self.__y)
        self.__pTurtle.down()
        self.__angle_increment = i_angle_increment  # rotation angle increment
        self.__current_angle = 0    # current rotation angle in radians

    def addMoon(self, i_moon_name, i_moon_radius, i_orbit_radius, i_angle_increment, i_color="ivory"):
        self.__moons.append(Moon(i_moon_name, i_moon_radius, i_orbit_radius, i_angle_increment, self.__x, self.__y, i_color))

    # moves the planet using angular velocity parameter.
    # Automatically triggers movement for all the moons the planet has.
    def angleMove(self):
        self.__current_angle += self.__angle_increment
        new_x = self.__distance * math.cos(self.__current_angle) 
        new_y = self.__distance * math.sin(self.__current_angle)
        self.__pTurtle.penup()
        self.__pTurtle.goto(self.__x,self.__y)
        self.__pTurtle.pendown()
        self.__pTurtle.goto(new_x, new_y)
        self.__x = new_x
        self.__y = new_y
        for m in self.__moons:
            m.angleMove(self.__x, self.__y)
        return

    def getName(self):
        return self.__name

    def printName(self):
        print(self.__name)
        for mo in self.__moons:
            mo.print_name()
        return
    
    def getDistance(self):
        return self.__distance

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
    def __init__(self, i_object_name, i_object_radius, i_orbit_radius, i_angle_increment, i_parent_x, i_parent_y, i_color="ivory"):
        self.__name = i_object_name
        self.__radius = i_object_radius
        self.__distance = i_orbit_radius

        self.__x = self.__distance + i_parent_x
        self.__y = 0
        self.__previous_x = self.__x
        self.__previous_y = self.__x
        self.__color = i_color
        self.__parent_x = i_parent_x
        self.__parent_y = i_parent_y

        self.__pTurtle = turtle.Turtle()

        self.__pTurtle.color(self.__color)
        self.__pTurtle.shape("circle")
        self.__pTurtle.turtlesize(self.__radius * SolarSystem.EARTH_RADIUS)

        self.__pTurtle.up()
        self.__pTurtle.goto(self.__x,self.__y)
        self.__pTurtle.down()
        self.__angle_increment = i_angle_increment  # rotation angle increment
        self.__current_angle = 0    # current rotation angle in radians

    def updateParentCoordinates(self, x, y):
        self.__parent_x = x
        self.__parent_y = y

    # Moves a moon. Different from planet movement as it requires the "parent" coordinates to calculate the new coordinates
    # An alternative approach would use a generic celestial object class, covering both the Sun, the planets and the moons.
    def angleMove(self, i_parent_x, i_parent_y):
        self.__current_angle += self.__angle_increment
        new_x = i_parent_x + self.__distance * math.cos(self.__current_angle) 
        new_y = i_parent_y + self.__distance * math.sin(self.__current_angle)
        self.__pTurtle.penup()
        self.__pTurtle.goto(new_x, new_y)
        self.__x = new_x
        self.__y = new_y
        self.updateParentCoordinates(i_parent_x,i_parent_y)
        
    
    def getName(self):
        return self.__name

    def printName(self):
        print("  " + self.__name)

def createSSandAnimate():
    ss = SolarSystem(6, 6)

    # sun = Sun("Sun", 3, 10, 5800)
    # ss.addSun(sun)

    m = Planet(i_object_name="Sun", i_object_radius=3, i_orbit_radius=0, i_angle_increment=0,i_color="gold")
    ss.addPlanet(m)
    # actual proportions: i_object_radius=11.2,i_orbit_radius=5.2, angle_increment=0.084
    m = Planet(i_object_name="Jupiter",i_object_radius=2,i_orbit_radius=2.2,i_angle_increment=0.16*SolarSystem.EARTH_ROTATION_SPEED,i_color="tan")
    m.addMoon(i_moon_name="Ganymede", i_moon_radius=0.34, i_orbit_radius=0.46, i_angle_increment=0.01)
    m.addMoon(i_moon_name="Callisto", i_moon_radius=0.32, i_orbit_radius=0.53, i_angle_increment=0.018)
    m.addMoon(i_moon_name="Io", i_moon_radius=0.29, i_orbit_radius=0.32, i_angle_increment=0.03)
    m.addMoon(i_moon_name="Europa", i_moon_radius=0.24, i_orbit_radius=0.39, i_angle_increment=0.02)
    ss.addPlanet(m)

    m = Planet(i_object_name="Mars",i_object_radius=0.53,i_orbit_radius=1.32,i_angle_increment=0.53*SolarSystem.EARTH_ROTATION_SPEED,i_color="darkorange")
    m.addMoon(i_moon_name="Phobos", i_moon_radius=0.12, i_orbit_radius=0.12, i_angle_increment=0.06)
    m.addMoon(i_moon_name="Deimos", i_moon_radius=0.15, i_orbit_radius=0.16, i_angle_increment=0.08)
    ss.addPlanet(m)

    m = Planet(i_object_name="Earth",i_object_radius=1,i_orbit_radius=1,i_angle_increment=SolarSystem.EARTH_ROTATION_SPEED,i_color="dodgerblue")
    m.addMoon(i_moon_name="Earth's Moon", i_moon_radius=0.27, i_orbit_radius=0.16, i_angle_increment=.1)

    # # radius = 0.27, iM = 5000 * 0.01, iDist = 0.0025695
    ss.addPlanet(m)

    m = Planet(i_object_name="Venus",i_object_radius=0.94,i_orbit_radius=0.722,i_angle_increment=1.62*SolarSystem.EARTH_ROTATION_SPEED,i_color="antiquewhite")
    ss.addPlanet(m)

    # i_orbit_radius = 0.3
    m = Planet(i_object_name="Mercury",i_object_radius=0.38,i_orbit_radius=0.5,i_angle_increment=4.14*SolarSystem.EARTH_ROTATION_SPEED,i_color="lightgray")
    ss.addPlanet(m)

    # ss.showPlanets()

    ss.showPlanetsByDistance()

    numTimePeriods = 4000
    for counter in range(numTimePeriods):
        ss.movePlanets()

    ss.freeze()
