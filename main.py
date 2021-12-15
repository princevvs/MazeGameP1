import turtle
#import math

wn = turtle.Screen()
wn.bgcolor('black')
wn.title("A Maze Game")
wn.setup (700,700)

#Create Pen
class pen(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("white")
        self.penup()
        self.speed(0)

class Player(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("yellow")
        self.penup()
        self.speed(0)

# Create levels list
levels = [""]

#Define first level
level_1 = [
"XXXXXXXXXXXXXXXXXXXXXXXXX",
"XP XXXXXX          XXXXXX",
"X  XXXXXX  XXXXXX  XXXXXX",
"X      XX  XXXXXX  XXXXXX",
"X      XX  XXX         XX",
"XXXXX  XX  XXX         XX",
"XXXXX  XX  XXXXX       XX",
"XXXXX  XX    XXXX  XXXXXX",
"X  XX        XXXX  XXXXXX",
"X  XX  XXXXXXXXXXXXXXXXXX",
"X        XXXXXXXXXXXXXXXX",
"X               XXXXXXXXX",
"XXXXXXXXXX      XXXXXX  X",
"XXXXXXXXXXXXX   XXXXXX  X",
"XXX  XXXXXXXX           X",
"XXX                     X",
"XXX       XXXXXXXXXXXXXXX",
"XXXXXXXX  XXXXXXXXXXXXXXX",
"XXXXXXXX                X",
"XX  XXXX                X",
"XX  XXXXXXXXXXXXX   XXXXX",
"XX   XXXXXXXXXXXX   XXXXX",
"XX        XXXX          X",
"XXXX                    X",
"XXXXXXXXXXXXXXXXXXXXXXXXX",
]

#Add maze to mazes list
levels.append(level_1)

#Create level setup function
def setup_maze(level):
    for y in range(len(level[y])):
        for x in range(len(level[y])):
            #Get the character at each x,y coordinate 
            #NOTE the order of y and x in thenext line
            character = level[y][x]
            #calculate the screen x,y coordinates
            screen_x = -288 +(x * 24)
            screen_y = 288 - (y * 24)

            #Check if it is an X
            if character == "X":
                pen.goto(screen_x, screen_y)
                pen.stamp()

            #Check if it is a P (representing the player)
            if character == "P":
                player.goto(screen_x, screen_y)

#Create class instances 
pen = pen()
player = Player()

#Set up the level
setup_maze(levels[1])

#Main Game Loop 
while True:
    pass

