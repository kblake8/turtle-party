# Turtle Party Peoject
# by Krista Blake
# 06.12.2023

import turtle
turtle.color("red")

def back(len):
  turtle.penup()
  turtle.backward(len)
  turtle.pendown()
  
# foward helper function
def move(len):
  back(-1 * len)

def polygon(num, size):
  for p in range(num):
    turtle.forward(size)
    turtle.left(360 / num)

def spiral(len, angle):
  for s in range(len, 5, -5):
    turtle.forward(s)
    turtle.right(angle)
    
spiral(75, 45)
move(150)
turtle.color("green")
spiral(100, 90)
