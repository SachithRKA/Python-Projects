from turtle import Turtle

FONT = ("Courier", 8, "normal")
ALIGN = "center"


class Scoreboard(Turtle):

  def __init__(self):
    super().__init__()
    self.score = 0
    self.color("white")
    self.penup()
    self.goto(0, 270)
    self.hideturtle()

    with open("data.txt") as data:
      self.high_score = int(data.read())

    self.update_scoreboard()

  def update_scoreboard(self):
    self.write(f"score: {self.score} High Score: {self.high_score}",
               align=ALIGN,
               font=FONT)

  def rest(self):
    if self.score > self.high_score:
      self.high_score = self.score
      with open("data.txt", mode="w") as data:
        data.write(f"{self.high_score}")

    self.score = 0
    self.update_scoreboard()

  def increase_score(self):
    self.score += 1
    self.clear()
    self.update_scoreboard()

  def game_over(self):
    self.goto(0, 0)
    self.write(f"GAME OVER {self.score}", align=ALIGN, font=FONT)
