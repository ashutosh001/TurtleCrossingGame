from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("red")
        self.up()
        self.setheading(90)
        self.got_to_start()

    def got_to_start(self):
        """Moves the player to the starting position"""
        self.goto(STARTING_POSITION)

    def race_finish(self):
        """Detects if the player has reached the finsih line"""
        if self.ycor() >= FINISH_LINE_Y:
            self.got_to_start()
            return True
        return False

    def move(self):
        """Moves the turtle based on user input"""
        self.forward(MOVE_DISTANCE)
        
