import turtle
import random
from turtle import Turtle,Screen

score  = 0
class Snakes:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
    def create_snake(self):
        starting_positions = [(-20,0),(-40,0),(-60,0)]
        for position in starting_positions:
            segment = Turtle("square")
            segment.color("green")
            segment.penup()
            segment.goto(position)
            self.segments.append(segment)
    def move(self):
        for seg_num in range(len(self.segments)-1,0,-1):
            new_x = self.segments[seg_num-1].xcor()
            new_y = self.segments[seg_num-1].ycor()
            self.segments[seg_num].goto(new_x,new_y)
        self.head.forward(20)

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)
    def down(self):
        if self.head.heading()!= 90:
            self.head.setheading(270)
    def left(self):
        if self.head.heading()!=0:
            self.head.setheading(180)
    def right(self):
        if self.head.heading()!=180:
            self.head.setheading(0)
class Food:
    def __init__(self):
        self.food = Turtle("circle")
        self.food.color("red")
        self.food.penup()
        self.refresh()
    def refresh(self):
        x_pos = random.randint(-380,380)
        y_pos = random.randint(-240,240)
        self.food.goto(x_pos,y_pos)
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.color()
        self.goto(0,220)
        self.update_score()
    def update_score(self):
        self.clear()
        self.write(f"Score:{self.score}",align = "center",font = ("Arial",18,"normal"))
    def increase_scores(self):
        self.score +=1
        self.update_score()
    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER",align = "center",font = ("Arial",24,"bold"))

game_windows = Screen()
game_windows.title("Welcome to the snake game")
game_windows.bgcolor("white")
game_windows.setup(800,500)
game_windows.tracer(0)

snakes = Snakes()
food = Food()
scoreboard = Scoreboard()

game_windows.listen()
game_windows.onkey(snakes.up,"Up")
game_windows.onkey(snakes.down,"Down")
game_windows.onkey(snakes.left,"Left")
game_windows.onkey(snakes.right,"Right")
games_on = True

while games_on:
    game_windows.update()
    turtle.time.sleep(0.1)
    snakes.move()

    if (
        snakes.head.xcor()>380 or
        snakes.head.xcor()<-380 or
        snakes.head.ycor()>240 or
        snakes.head.ycor()<-240
    ):
        games_on = False
        print("Game Over!")

    if snakes.head.distance(food.food)<15:
        food.refresh()
        new_segments = Turtle("square")
        new_segments.color("green")
        new_segments.penup()
        snakes.segments.append(new_segments)
        scoreboard.increase_scores()
        score += 1
        print(f"{score}")
    for segments in snakes.segments[1:] :
        if snakes.head.distance(segments)<10:
            if len(snakes.segments)>3:
                last_segments = snakes.segments.pop()
                last_segments.hideturtle()
                score-=1
                print(f"{score}")
            else:
                games_on = False
                scoreboard.game_over()

game_windows.exitonclick()
