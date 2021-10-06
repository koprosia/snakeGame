from turtle import Turtle, Screen

segments = []
screen = Screen()


class Snake:
    def __init__(self):
        self.segments = segments
        for i in range(3):
            new_segment = Turtle(shape="square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(x=0 - i * 20, y=0)
            segments.append(new_segment)

    def move(self):
        for seg_num in range(len(segments) - 1, 0, -1):
            segments[seg_num].goto(segments[seg_num - 1].xcor(), segments[seg_num - 1].ycor())

        segments[0].forward(10)
        screen.update()

