import pygame, sys, time
from pygame.locals import *

pygame.mixer.pre_init(44100, -16, 1, 512)
pygame.mixer.init()
pygame.init()

window = pygame.display.set_mode((800, 600), HWSURFACE | DOUBLEBUF)
world = pygame.Surface((800, 600))
pygame.display.set_caption("Pong")
font = pygame.font.SysFont("PressStart2P.ttf", 30, False)
clock = pygame.time.Clock()
white = 255, 255, 255
black = 0, 0, 0
red = 255, 0, 0
sound = pygame.mixer.Sound("Hit sound.wav")
sound1 = pygame.mixer.Sound("Score sound.wav")


class Paddles:
    def __init__(self, x, y, w, h, s):
        self.x, self.y, self.width, self.height, self.speed = x, y, w, h, s
        self.colour = (255, 255, 255)
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def collision(self):
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        if self.y <= 0:
            self.y = 0
        if self.y >= 450:
            self.y = 450

    def draw(self):
        pygame.draw.rect(world, self.colour, (self.x, self.y, self.width, self.height))


paddle1 = Paddles(30, 250, 20, 150, 8)
paddle2 = Paddles(750, 250, 20, 150, 8)


class Ball:
    def __init__(self, x, y, w, h, ):
        self.x, self.y, self.width, self.height = x, y, w, h,
        self.colour = (255, 255, 255)
        self.speedx = 5
        self.speedy = 5
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.player1_Score = 0
        self.player2_score = 0

    def movement(self):
        self.x += self.speedx
        self.y += self.speedy
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        if self.rect.colliderect(paddle1.rect):
            sound.play()
            self.speedx = self.speedx * -1
        if self.rect.colliderect(paddle2.rect):
            sound.play()
            self.speedx = self.speedx * -1
        if self.y >= 585:
            sound.play()
            self.speedy = self.speedy * -1
        if self.y <= 0:
            sound.play()
            self.speedy = self.speedy * -1
        if self.x <= 0:
            self.x = 385
            self.player2_score += 1
            sound1.play()
        if self.x >= 800:
            self.x = 280
            self.player1_Score += 1
            sound1.play()

    def draw(self):
        pygame.draw.rect(world, self.colour, (self.x, self.y, self.width, self.height))


ball = Ball(385, 280, 15, 15)

running = True
while running:
    window.blit(world, (0, 0))
    world.fill(black)
    for event in pygame.event.get():  
        if event.type == pygame.QUIT:
            sys.exit()
    for y in range(0, 600, 20):
        pygame.draw.rect(world, white, (390, y, 8, 15))
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        paddle1.y -= paddle1.speed
    if keys[pygame.K_s]:
        paddle1.y += paddle1.speed
    if keys[pygame.K_UP]:
        paddle2.y -= paddle2.speed
    if keys[pygame.K_DOWN]:
        paddle2.y += paddle2.speed
    ball.movement()
    paddle1.collision()
    paddle2.collision()

    text = font.render(str(ball.player1_Score), True, white)
    text1 = font.render(str(ball.player2_score), True, white)
    ball.draw()
    paddle1.draw()
    paddle2.draw()
    world.blit(text, (370, 10))
    world.blit(text1, (407, 10))
    clock.tick(60)
    pygame.display.flip()
