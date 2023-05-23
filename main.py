from turtle import *
import random 
                  
class Player(Turtle):
  def __init__(self, left_key, right_key, fire_key):
    super().__init__()  
    self.x = random.randrange(-300, 300)
    self.y = random.randrange(-150, 150)
    self.penup()
    self.goto(self.x, self.y)
    self.shape('turtle')
    self.color('purple')
    screen.onkey(self.turnleft, left_key)
    screen.onkey(self.turnright, right_key)
    screen.onkey(self.fire, fire_key)
  def draw(self):
    self.pendown()
    self.penup()
  def update(self):
    self.forward(5)
    if self.xcor() < -300 or self.xcor() > 300 or self.ycor() < -150 or self.ycor() > 150:
      self.right(180)
      self.forward(5)
  def turnleft(self):
    self.left(10)
  def turnright(self):
    self.right(10)
  def fire(self):
    bullets.append(Bullet(self.heading(), self.xcor(), self.ycor()))
    

    
class Prize(Turtle):
  def __init__(self):
    super().__init__()
    self.x = random.randrange(-300, 300)
    self.y = random.randrange(-150, 150)
    self.penup()
    self.color('yellow')
    self.goto(self.x, self.y)
    self.shape('circle')
    self.pendown()
  def update(self):
    deltax = 0
    deltay = 0
    while True:
      deltax = self.x + random.randrange(-5, 5)
      deltay = self.y + random.randrange(-5, 5)
      if deltax < -300 or deltax > 300 or deltay < -150 or deltay > 150:
        continue
      else:
        break
    self.penup()
    self.x = deltax
    self.y = deltay
    self.goto(self.x, self.y)
    self.pendown()
    
  def respond(self):
    self.x = random.randrange(-300, 300)
    self.y = random.randrange(-150, 150)
    self.penup()
    self.goto(self.x, self.y)
    self.pendown()
    zombies.append(Zombie(player1))
    zombies.append(Zombie(player2))
    
    
class Zombie(Turtle):
  def __init__(self, player):
    super().__init__()
    self.x = random.randrange(-300, 300)
    self.y = random.randrange(-150, 150)
    self.penup()
    self.goto(self.x, self.y)
    self.shape('turtle')
    self.color('green')
    self.player = player
    self.pendown()
  def update(self):
    self.penup()
    self.setheading((self.towards(self.player)))
    self.forward(2)
    self.pendown()
  
class Bullet(Turtle):
  def __init__(self, heading, x, y):
    super().__init__()
    self.penup()
    self.goto(x, y)
    self.shape('circle')
    self.color('red')
    self.shapesize(.25,.25,.25)
    self.setheading(heading)
    self.pendown()
  def update(self):
    self.penup()
    self.forward(15)
    self.pendown()
    

screen = Screen()
screen.bgcolor('light blue')
screen.setup(width = 600,height = 300, startx= 0, starty=0)
screen.listen()

zombies = []
bullets = []
player1 = Player("a", "d", "w")
player2 = Player("Left", "Right", "l")
prize = Prize()

def player1wins():
  text = Turtle()
  text.penup()
  text.hideturtle()
  text.goto(-150, 75)
  text.write("player 1 wins!", False, align = "left", font=("Arial", 18, "bold"))

def player2wins():
  text = Turtle()
  text.penup()
  text.hideturtle()
  text.goto(-150, 75)
  text.write("player 2 wins!", False, align = "left", font=("Arial", 18, "bold"))

alive = True

while alive:
  for zombie in zombies:
    if player1.distance(zombie) <15:
      player1.hideturtle()
      player2wins()
      alive = False
      break
    if player2.distance(zombie) <15:
      player2.hideturtle()
      player1wins()
      alive = False
      break
    zombie.update()
  newbullets = []
  for bullet in bullets:
    if bullet.xcor() < -300 or bullet.xcor() > 300 or bullet.ycor() < -150 or bullet.ycor() > 150:
      bullet.hideturtle()
      continue 
    tempzombie = None
    for zombie in zombies:
      if zombie.distance(bullet) < 20:
        tempzombie = zombie
    if tempzombie is not None:
      tempzombie.hideturtle()
      bullet.hideturtle()
      zombies.remove(tempzombie)
      continue
    bullet.update()
    newbullets.append(bullet)
  bullets = newbullets  
  player1.update()
  player1.draw()
  player2.update()
  player2.draw()
  prize.update()
  if player1.distance(prize) < 20 or player2.distance(prize) < 20:
    prize.respond()

while True:
  pass
