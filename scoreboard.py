from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def create_line(self):
        self.penup()
        self.goto(0, 300)
        self.setheading(270)
        self.shape('square')
        self.shapesize(0.5, 0.5)
        self.color('white')
        for _ in range(10):
            for _ in range(3):
                self.stamp()
                self.forward(10)
            self.forward(30)
    
        
    def update_scoreboard(self):
        self.clear()
        self.create_line()
        self.goto(-100, 200)
        self.write(self.l_score, align='center', font=('Pixel Sans Serif', 60, 'normal'))
        self.goto(100, 200)
        self.write(self.r_score, align='center', font=('Pixel Sans Serif', 60, 'normal'))

    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        self.r_score += 1
        self.update_scoreboard()
