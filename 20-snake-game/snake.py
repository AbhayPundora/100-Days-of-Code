from turtle import Turtle
STARTING_POSITIONS = [(0,0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)



    def add_segment(self, position):
        segment = Turtle("square")
        segment.color("white")
        segment.penup()
        segment.goto(position)
        self.segments.append(segment)


    def extend_snake(self):
        self.add_segment(self.segments[-1].position())



    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)

        self.segments[0].forward(MOVE_DISTANCE)  # suppose self.segments = [0, 1, 2] then 2 -> 1 -> 0 -> stop loop in 0 and  0 -> forward -> 20paces


    def up(self):
        if self.head.heading() == DOWN:
            return
        self.head.setheading(UP)


    def down(self):
        if self.head.heading() == UP:
            return
        self.head.setheading(DOWN)


    def left(self):
        if self.head.heading() == RIGHT:
            return
        self.head.setheading(LEFT)


    def right(self):
        if self.head.heading() == LEFT:
            return
        self.head.setheading(RIGHT)

    def reset(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]
