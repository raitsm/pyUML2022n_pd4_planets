import turtle
import solar_system_animated as sol



def main():
    SCR_SIZE = 1100    
    turtle.setup(width=SCR_SIZE, height=SCR_SIZE, startx=0, starty=0) #, startx=MARGIN, starty=MARGIN)
    turtle.screensize(canvwidth=SCR_SIZE, canvheight=SCR_SIZE,bg="black") #  

    sol.createSSandAnimate()


if __name__ == "__main__":
    main()
 