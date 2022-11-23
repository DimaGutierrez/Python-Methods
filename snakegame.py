import turtle
import random
import time

player_score = 0
highest_score = 0
delay_time = 0.1

# window screen created
wind = turtle.Screen()
wind.title("Snake Maze🐍")
wind.bgcolor("red")

# The screen size
wind.setup(width=600, height=600)


# creating the snake 
snake = turtle.Turtle()
snake.shape("square")
snake.color("black")
snake.penup()
snake.goto(0, 0)
snake.direction = "Stop"

# creating the food
snake_food = turtle.Turtle()
shapes = random.choice('triangle','circle')
snake_food.shape(shapes)
snake_food.color("blue")
snake_food.speed(0)
snake_food.penup()
snake_food.goto(0, 100)

pen = turtle.Turtle()
pen.speed(0)
pen.shape('square')
pen.color('white')
pen.penup()
pen.hideturtle()
pen.goto(0, 250)
pen.write("Your_score: 0 Highest_Score : 0", align="center", 
font=("Arial", 24, "normal"))
turtle.mainloop()

# Assigning directions
def moveleft():
    if snake.direction != "right":
        snake.direction = "left"

def moveright():
    if snake.direction != "left":
        snake.direction = "right"

def moveup():
    if snake.direction != "down":
        snake.direction = "up"

def movedown():
    if snake.direction != "up":
        snake.direction = "down"

def move():
    if snake.direction == "up":
        coord_y = snake.ycor()
        snake.sety(coord_y+20)

    if snake.direction == "down":
        coord_y = snake.ycor()
        snake.sety(coord_y-20)

    if snake.direction == "right":
        coord_x = snake.xcor()
        snake.setx(coord_x+20)

    if snake.direction == "left":
        coord_x = snake.xcor()
        snake.setx(coord_x-20)

wind.listen()
wind.onkeypress(moveleft, 'L')
wind.onkeypress(moveright, 'R')
wind.onkeypress(moveup, 'U')
wind.onkeypress(movedown, 'D')

segments = []

#Implementing the gameplay
while True:
    wind.update()
    if snake.xcor() > 290 or snake.xcor() < -290 or snake.ycor() > 290 or snake.ycor() < -290:
        time.sleep(1)
        snake.goto(0, 0)
        snake.direction = "Stop"
        snake.shape("square")
        snake.color("green")

        for segment in segments:
            segment.goto(1000, 1000)
            segments.clear()
            player_score = 0
            delay_time = 0.1
            pen.clear()
            pen.write("Player's_score: {} Highest_score: {}".format(player_score,
highest_score), align="center", font=("Arial", 24, "normal"))

        if snake.distance(snake_food) < 20:
            coord_x = random.randint(-270, 270)
            coord_y = random.randint(-270, 270)
            snake_food.goto(coord_x, coord_y)

            # Adding segment
            added_segment = turtle.Turtle()
            added_segment.speed(0)
            added_segment.shape("square")
            added_segment.color("white")
            added_segment.penup()
            segments.append(added_segment)
            delay_time -= 0.001
            player_score += 5

            if player_score > highest_score:
                highest_score = player_score
                pen.clear()
                pen.write("Player's_score: {} Highest_score: {}".format(player_score,
highest_score), align="center", font=("Arial", 24, "normal"))

    # checking for collisions
    for i in range(len(segments)-1, 0, -1):
        coord_x = segments[i-1].xcor()
        coord_y = segments[i-1].ycor()
        segments[i].goto(coord_x, coord_y)

    if len(segments) > 0:
        coord_x = snake.xcor()
        coord_y = snake.ycor()
        segments[0].goto(coord_x, coord_y)
    move()

    for segment in segments:
        if segment.distance(snake) < 20:
            time.sleep(1)
            snake.goto(0, 0)
            snake.direction = "stop"
            snake.color('white')
            snake.shape('square')

            for segment in segments:
                segment.goto(1000, 1000)
                segment.clear()
                player_score = 0
                delay_time = 0.1
                pen.clear()
                pen.write("Player's_score: {} Highest_score: {}".format(player_score,
highest_score), align="center", font=("Arial", 24, "normal"))

     time.sleep(delay_time)

turtle.mainloop()
