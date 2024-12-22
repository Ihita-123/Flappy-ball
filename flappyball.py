import pgzrun
import random

TITLE='Flappy Ball Game'
HEIGHT= 600
WIDTH= 400


gravity = 2000.0

class Ball:
    def __init__ (self,initial_x,initial_y):
        self.x = initial_x
        self.y = initial_y
        self.vx=200
        self.vy = 0
        self.radius= 40
        self.colour=self.rcolour()
    def rcolour(self):
        R= random.randint(0,255)
        G= random.randint(0,255)
        B= random.randint(0,255)
        return R,G,B

    def draw(self):
        pos = (self.x, self.y)
        screen.draw.filled_circle(pos,self.radius,self.colour)

ball=Ball(50,100)
ball2=Ball(300,40)

def draw():
    screen.clear()
    ball.draw()
    ball2.draw()

def update(dt):
    uy=ball.vy
    ball.vy+=gravity*dt
    ball.y+=(uy+ball.vy)*0.5*dt
    uy=ball2.vy
    ball2.vy+=gravity*dt
    ball2.y+=(uy+ball2.vy)*0.5*dt

    if ball.y>HEIGHT-ball.radius:
        ball.y=HEIGHT-ball.radius
        ball.vy=-ball.vy*0.9
    if ball2.y>HEIGHT-ball2.radius:
        ball2.y=HEIGHT-ball2.radius
        ball2.vy=-ball2.vy*0.9
        
    ball.x+=ball.vx*dt
    ball2.x+=ball2.vx*dt
    if ball.x>WIDTH-ball.radius or ball.x<ball.radius:
        ball.vx=-ball.vx
    if ball2.x>WIDTH-ball2.radius or ball2.x<ball2.radius:
        ball2.vx=-ball2.vx

def on_key_down(key):
    if key==key.SPACE:
        ball.vy=-500
        ball2.vy=-500



pgzrun.go() 
