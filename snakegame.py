import turtle
import random
import time

delay=0.1
score=0
highestscore=0
#snakebodies
bodies=[]

#getting a screen | canvas
s=turtle.Screen()
s.title("snake game mg2.0")
s.bgcolor("blue")
s.setup(width=600,height=600)

#create snake head
head=turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.fillcolor("orange")
head.penup()
head.goto(0,0)
head.direction="stop"

#snake food
food=turtle.Turtle()
food.shape("circle")
food.color("black")
food.fillcolor("magenta")
food.penup()
food.ht()
food.goto(0,200)
food.st()

#score board
sb=turtle.Turtle()
sb.shape("square")
sb.fillcolor("grey")
sb.penup()
sb.ht()
sb.goto(0,-250)
sb.write("score: 0 |  highest  score: 0",align= "center",font=("candara,24,bold"))

def moveup():
    if head.direction!="down":
        head.direction="up"

def moveleft():
    if head.direction!="right":
        head.direction="left"

def moveright():
    if head.direction!="left":
        head.direction="right"

def movedown():
    if head.direction!="up":
        head.direction="down"

def movestop():
        head.direction="stop"

#actual movement function

def move():
    if head.direction=="up":
        y=head.ycor()
        head.sety(y+20)

    if head.direction=="down":
        y=head.ycor()
        head.sety(y-20)
    if head.direction=="left":
        x=head.xcor()
        head.setx(x-20)
    if head.direction=="right":
        x=head.xcor()
        head.setx(x+20)


#event handling - key mapping
s.listen()
s.onkey(moveup,"Up")
s.onkey(movedown,"Down")
s.onkey(moveleft,"Left")
s.onkey(moveright,"Right")
s.onkey(movestop,"space")


#mainloop
while True:
    s.update()#this is to update the screen
    #check collission with boarder
    if head.xcor()>290:
        head.setx(-290)
        
    if head.xcor()<-290:
        head.setx(290)


    if head.ycor()>290:
        head.sety(-290)

    if head.ycor()<-290:
        head.sety(290)
        
        

    
    #check collision with food

    if head.distance(food)<20:
        #move the food to new random place
        x=random.randint(-290,290)
        y=random.randint(-290,290)
        food.goto(x,y)
        #increase the length of the snake
        body=turtle.Turtle()
        body.speed(0)
        body.penup()
        body.shape("square")
        body.color("red")
        bodies.append(body)#append new body
            
        #increase the score
        score+=10

        #increase delay
        delay+=0.001

        #update the highest score
        if score>highestscore:
            highestscore=score

        sb.clear()
        sb.write("Score: {}| Highest score: {}".format(score,highestscore),align= "center",font=("candara,24,bold"))


    #move the snake bodies
    for index in range(len(bodies)-1,0,-1):
            x=bodies[index-1].xcor()
            y=bodies[index-1].ycor()
            bodies[index].goto(x,y)


    if len(bodies)>0:
            x=head.xcor()
            y=head.ycor()
            bodies[0].goto(x,y)
    move()

    
    #check collision with snake body
    for body in bodies:
        if body.distance(head)<20:
            time.sleep(1)
            head.goto(0,0)
            head.direction="stop"
            #hide bodies
            for body in bodies:
                body.ht()
            bodies.clear()
            score=0
            delay=0.1
            #update score board
            sb.clear()
            sb.write("Score: ()| Highest score: ()".format(score,highestscore),align= "center",font=("candara,24,bold"))

    time.sleep(delay)
s.mainloop()

#this is end of the snake game code

        
