from turtle import Turtle

MOVE_DISTANCE = 20
STARTING_SEGMENTS = 3


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        x = 0
        y = 0
        for i in range(STARTING_SEGMENTS):
            self.add_segment(x, y)
            x -= 20.0

    def add_segment(self, x, y):
        new_segment = Turtle("square")
        new_segment.penup()
        new_segment.color("white")
        new_segment.goto(x=x, y=y)
        self.segments.append(new_segment)

    def increase_snake_size(self):
        self.add_segment(self.segments[-1].xcor(), self.segments[-1].ycor())

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def detect_collision(self):
        for segment in self.segments:
            if self.head == segment:
                pass
            elif self.head.distance(segment) < 10:
                return True
        if self.head.xcor() >= 290 or self.head.xcor() <= -290 or self.head.ycor() >= 290 or self.head.ycor() <= -290:
            return True
        else:
            return False
