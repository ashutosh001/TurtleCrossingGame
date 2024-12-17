from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.up()
        self.hideturtle()
        self.goto(-280,260)
        self.write_level(1)
    
    def write_level(self,level):
        """Writes the current level of the player"""
        self.down()
        self.clear()
        self.write(f"Level: {level}",align="left",font=FONT)

    def game_over(self):
        """Displays game over"""
        self.down()
        self.goto(0,0)
        self.write("GAME OVER",align="center",font=FONT)
