import turtle
import time

window = turtle.Screen()

window.title("Dinossaur Knock Off")
window.bgcolor("black")
window.setup(width=800, height=600)
window.tracer(0) #stops the window from updating the window automatically, makes the game go faster

score = 0

# dinossaur
dinossaur = turtle.Turtle()
dinossaur.speed(0)
dinossaur.shape("square")
dinossaur.color("white")
dinossaur.penup()
dinossaur.goto(-350,-100)
dinossaur.forwardSpeed = 0
dinossaur.backwardSpeed = 0

# Floor
floor = turtle.Turtle()
floor.speed(0)
floor.color("white")
floor.penup()
floor.goto(-400,-110)
floor.pendown()
floor.forward(800)

#Enemy
enemy = turtle.Turtle()
enemy.speed(0)
enemy.shape("square")
enemy.color("white")
enemy.shapesize(stretch_wid=2, stretch_len=1) #the default size is 20x20, this stretches the square
enemy.penup()
enemy.goto(450,-90)
enemy.ascending = True
enemy.StretchModifier = 0
enemy.HeightModifier = 0
enemy.Speed = 0.07

#Pen to write the scores in the window
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup() #so it doesn't draw a line on the screen when it moves (the obj start at teh center of the screen)
pen.hideturtle()
pen.goto(0,260)
pen.write("Score: {}".format(score), align="center", font=("Courier", 24, "normal"))


def moveUp(obj):
    if obj.ycor() <= -100: # forbidding double jumps and stuff
        obj.sety(obj.ycor() + 120)
        
        if obj.forwardSpeed != 0:
            obj.setx(obj.xcor() + obj.forwardSpeed)

        if obj.backwardSpeed != 0:
            obj.setx(obj.xcor() - obj.backwardSpeed)
      
def moveLeft(obj):
    obj.backwardSpeed += 5
    obj.back(20)

def moveRight(obj):
    obj.forwardSpeed += 5
    obj.forward(20)

def releaseRight():
    dinossaur.forwardSpeed = 0

def releaseLeft():
    dinossaur.backwardSpeed = 0

#Keyboard binding
window.listen() #sets the window to listen for input
window.onkeypress(lambda: moveUp(dinossaur), "Up")
window.onkeypress(lambda: moveLeft(dinossaur), "Left")
window.onkeypress(lambda: moveRight(dinossaur), "Right")
window.onkeyrelease(releaseRight, "Right")
window.onkeyrelease(releaseLeft, "Left")

#change the modifiers to make the enemies taller/shorter
def setupModifiers(enemy):

    if enemy.StretchModifier == 2:
        enemy.ascending = False

    if enemy.StretchModifier == 0:
        enemy.ascending = True

    if enemy.ascending:
        enemy.StretchModifier += 1
        enemy.HeightModifier -= 10
    else:
        enemy.StretchModifier -= 1
        enemy.HeightModifier += 10

def resetEnemy(enemy):
    enemy.goto(450,-90)
    enemy.shapesize(stretch_wid= 2, stretch_len=1)
    enemy.StretchModifier = 0
    enemy.HeightModifier = 0
    enemy.Speed = 0.07

# Main Loop
while True:
    window.update()

    # collision detection
    if dinossaur.distance(enemy) < 20:
        dinossaur.goto(-350,-100)
        resetEnemy(enemy)
        score = 0
        pen.clear()
        pen.write("Score: {}".format(score), align="center", font=("Courier", 24, "normal"))

    # Gravity
    if dinossaur.ycor() - floor.ycor() > 10:
        dinossaur.sety(dinossaur.ycor() - 0.25)
        
    if enemy.xcor() <= -400:

        score += 1
        pen.clear()
        pen.write("Score: {}".format(score), align="center", font=("Courier", 24, "normal"))

        setupModifiers(enemy)

        enemy.shapesize(stretch_wid= 2 + enemy.StretchModifier, stretch_len=1) 

        if enemy.Speed < 0.9:
            enemy.Speed += 0.03
        
        enemy.goto(450,-90 - enemy.HeightModifier)
    else:
        enemy.back(enemy.Speed)
    
    

    
