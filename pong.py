import turtle 
import os

wn=turtle.Screen()  #create window & give title
wn.title("Pong game")
wn.bgcolor("Black")
wn.setup(width=800 , height =600)

wn.tracer(0) # stops window from updating (we manually have to update)

#paddle A
A=turtle.Turtle()
A.speed(0)  #sets the speed for paddle for max possile speed
A.shape("square")
A.color("white")
A.shapesize(stretch_wid=5 , stretch_len=1) # defualt shape is 20x20 width will become 5 times length remain same
A.penup() # our paddle will not leave any trave while moving
A.goto(-350 , 0) #vertically centered in out screen (00 , 350 , -350 is middle)

#score
score_a=0
score_b=0

#paddle A
B=turtle.Turtle()
B.speed(0)  
B.shape("square")
B.color("white")
B.shapesize(stretch_wid=5 , stretch_len=1)  #dimension of each peddle (100,20)
B.penup() 
B.goto(350 , 0)

#ball
Ball=turtle.Turtle()
Ball.speed(0)  
Ball.shape("square")
Ball.color("white")
Ball.penup() 
Ball.goto(0 , 0)
Ball.dx = 0.4 # each time BAll will move by 2pixelss (d is delta)
Ball.dy = 0.4

#pen
pen=turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Plyer A: 0  Player B: 0" , align="center" , font=("Courier" ,24 ,"normal"))


#movement of peddle
def A_up():
    y=A.ycor() #get the y cordinate
    y+=20      #add 20 to y cor
    A.sety(y)  # set new y cor

def A_down():
    y=A.ycor()
    y-=20      
    A.sety(y)

def B_up():
    y=B.ycor()
    y+=20      
    B.sety(y)

def B_down():
    y=B.ycor()
    y-=20      
    B.sety(y)

#keyboard binding
wn.listen()                     #window will listen to keyboard input
wn.onkeypress(A_up, "w")        #ny pressing w , peddle A will move upward
wn.onkeypress(A_down, "s") 
wn.onkeypress(B_up, "Up")
wn.onkeypress(B_down, "Down")

#main game loop
while True:
    wn.update()

    #MOVING OF BALL
    Ball.setx(Ball.xcor() + Ball.dx)
    Ball.sety(Ball.ycor() + Ball.dy)

    # height of window is 600 (300,-300) and height of ball is 20 (10,-10)
    if Ball.ycor() > 290 : #300-10
        Ball.sety(290)
        Ball.dy *= -1      # reverse the direction of ball (when ycor reaches 290 its y cor will will decrese each time by 0.2 pixel )
        

    if Ball.ycor() < -290 : #300-10
        Ball.sety(-290)
        Ball.dy *= -1

    if Ball.xcor() > 390 : #400-10 width=800
        Ball.goto(0,0) 
        Ball.dx *= -1 
        score_a+=1
        pen.clear() #prevent overlapping
        pen.write("Plyer A: {}  Player B: {}".format(score_a , score_b) , align="center" , font=("Courier" ,24 ,"normal"))

    if Ball.xcor() < -390 : #300-10
        Ball.goto(0,0)
        Ball.dx *= -1
        score_b+=1 
        pen.clear()  
        pen.write("Plyer A: {}  Player B: {}".format(score_a , score_b) , align="center" , font=("Courier" ,24 ,"normal"))

    #ball and peddle collision
    if (Ball.xcor()>340 and Ball.xcor()<350) and ( Ball.ycor()< B.ycor()+40 and Ball.ycor()> B.ycor() -40):
        Ball.setx(340)
        Ball.dx *= -1
    
    if (Ball.xcor()<-340 and Ball.xcor()>-350) and ( Ball.ycor()< A.ycor()+40 and Ball.ycor()> A.ycor() -40):
        Ball.setx(- 340)
        Ball.dx *= -1
