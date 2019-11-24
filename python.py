#ensure that the user has installed tkinter
try:
    from tkinter import *
except:
    print("You do not have tkinter installed")

from random import randint
import math

#size of snake is fixed, and location are global variable
snakeSize = 20
xSnake = 0;
ySnake = 0;

#food location is global, and so is the score
xValue = 0
yValue = 0
score = 0
snake = None
food = None
direction = "d"

'''
#assign the variables for the height and the width
try:
    heightChosen = int(input("choose a length for your canvas between 10 and 50: "))
except :
    print("ensure you enter a number")

#ensure that the size is within the given range
while(heightChosen < 10 or heightChosen > 50):
    try:
        print("You have chosen a value out of range")
        heightChosen = int(input("choose a length for your canvas between 10 and 50: "))
    
    except:
        print("ensure you enter a number")
'''

heightChosen = 30

#function to place the food in the canvas
def placeFood():
    global xValue, yValue
    xValue = randint(0, heightChosen - 1) * snakeSize
    yValue = randint(0, heightChosen - 1) * snakeSize
    food = canvas.create_rectangle(xValue, yValue, xValue + snakeSize, yValue + snakeSize, fill="yellow")

#move the food to another random location
def moveFood():
    global food, xValue, yValue
    canvas.delete(food)
    xValue = randint(0, heightChosen - 1) * snakeSize
    yValue = randint(0, heightChosen - 1) * snakeSize
    food = canvas.create_rectangle(xValue, yValue, xValue + snakeSize, yValue + snakeSize, fill="yellow")

#function to place the head of the snake
def placeSnake():
    global xSnake, ySnake, heightChosen, snake
    startPosition = math.floor(heightChosen / 2) * snakeSize
    xSnake = startPosition + 2
    ySnake = startPosition + 2
    snake = canvas.create_rectangle(xSnake, ySnake, xSnake + snakeSize, ySnake + snakeSize, fill="white")

#move the snake of the head depending on the direction
def up():
    global xSnake, ySnake, snake
    ySnake = (ySnake - snakeSize) % (snakeSize * heightChosen)
    canvas.delete(snake)
    snake = canvas.create_rectangle(xSnake, ySnake , xSnake + snakeSize, ySnake + snakeSize, fill="white")
    direction = "u"

def down():
    global xSnake, ySnake, snake
    ySnake = (ySnake + snakeSize) % (snakeSize * heightChosen)
    canvas.delete(snake)
    snake = canvas.create_rectangle(xSnake, ySnake , xSnake + snakeSize, ySnake + snakeSize, fill="white")
    direction = "d"

def left():
    global xSnake, ySnake, snake
    xSnake = (xSnake - snakeSize) % (snakeSize * heightChosen)
    canvas.delete(snake)
    snake = canvas.create_rectangle(xSnake, ySnake , xSnake + snakeSize, ySnake + snakeSize, fill="white")
    direction = "l"

def right():
    global xSnake, ySnake, snake
    xSnake = (xSnake + snakeSize) % (snakeSize * heightChosen)
    canvas.delete(snake)
    snake = canvas.create_rectangle(xSnake, ySnake , xSnake + snakeSize, ySnake + snakeSize, fill="white")
    direction = "r"

#decide where the snake goes depending on input
def move(inp):
    event = inp.keysym
    if event == "Left":
        left()
    elif event == "Right":
        right()
    elif event == "Up":
        up()
    elif event == "Down":
        down()
 
#create the canvas
main = Tk()
main.title("snake game")
canvas = Canvas(main, width = heightChosen * snakeSize + 2, height = heightChosen * snakeSize + 2, background = '#34eba4')
canvas.pack()
placeSnake()
placeFood()
main.bind("<Key>", move)
main.mainloop()

