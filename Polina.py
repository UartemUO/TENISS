from pygame import *

window = display.set_mode((1000,700))
clock = time.Clock()
display.set_caption('Настолный тенис')
background = transform.scale(image.load('ping-pong-rackets-pattern-background_24640-10252.jpg'),(1000,700))


font.init()
font = font.SysFont('Arial',35)

class Gamer(sprite.Sprite):
    def __init__(self,gamer_image,gamer_x,gamer_y,size_x,size_y,gamer_step):
        super().__init__()
        self.image=transform.scale(image.load(gamer_image),(size_x,size_y))
        self.rect=self.image.get_rect()
        self.rect.x=gamer_x
        self.rect.y=gamer_y
        self.step=gamer_step
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))
class Player(Gamer):
    def control_1(self):
        buttons = key.get_pressed()
        if buttons[K_w] and self.rect.y>0:
            self.rect.y -= self.step
        if buttons[K_s] and self.rect.y<600:
            self.rect.y += self.step
    def control_2(self):
        buttons = key.get_pressed()
        if buttons[K_o] and self.rect.y>0:
            self.rect.y -= self.step
        if buttons[K_l] and self.rect.y<600:
            self.rect.y += self.step
            
game = True 
finish = False
pl1 = Player('51539.png',20,300,10,100,15)
pl2 = Player('51539.png',970,300,10,100,15)
ball = Player('338287877_max.jpg',500,300,40,50,0)
lose_1 = font.render('Проиграл 1 игрок',True,(255,255,255))
lose_2 = font.render('Проиграл 2 игрок',True,(255,255,255))
ball_speed_x = 3
ball_speed_y = 3
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
 
    if finish != True:
        window.blit(background,(0,0))
        pl1.reset()
        pl2.reset()
        ball.reset()
        pl1.control_1()
        pl2.control_2()
        ball.rect.x += ball_speed_x
        ball.rect.y -= ball_speed_y
        if ball.rect.y < 0 or ball.rect.y > 650:
            ball_speed_y *= -1
        if ball.rect.x < 0:
            finish = True
            window.blit(lose_1, (400,300))
        if ball.rect.x > 1000:
            finish = True
            window.blit(lose_2, (400,300))
        if sprite.collide_rect (pl1, ball) or sprite.collide_rect (pl2,ball):
            ball_speed_y *= 1
            ball_speed_x *= -1
        display.update()
    clock.tick(60)