#https://www.youtube.com/watch?v=NOyfgCz05Yo

import pygame
import time
import sys
import random

pygame.init()

#GLOBALS

#color
gray=(119,118,110)
white=(255,255,255)
black=(0,0,0)
red=(200,0,0)
green=(0,200,0)
blue=(0,0,255)
bright_red=(255,0,0)
bright_green=(0,255,0)

#GAMESTATE
INTRO = 1
MENU = 2
GAME = 3
GAMEOVER = 4
QUIT = 0

window_width=1332
window_height=700

#display surface
background = pygame.image.load('Intro_Background/background_1.jpg')
carimg =pygame.image.load('Car_Images/Topdown_vehicle_sprites_pack/Car.png')
car1=pygame.transform.scale(carimg, (100,100))

print(window_width, window_height)

gd = pygame.display.set_mode([window_width, window_height])
clock = pygame.time.Clock()


def car (display, x,y) :
    display.blit(car1, (x, y))
    pygame.display.update()


def game_intro():
  gd.blit('Intro_Background/background_1.jpg', 0, 0)
  gameintro=False
  while gameintro==False:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameintro = True
            game_over=True

    window_width = 800
    window_hight = 600


def game_loop(game_state):
    game_state = INTRO
    x_change = 0
    y_lead = 0
    x = 300
    y = 490
    block = 10
    while game_state != QUIT:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_state = QUIT
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -block
                elif event.key == pygame.K_RIGHT:
                    x_change = +block
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

        x += x_change

        gd.fill(black)
        car(gd, x,y)

        clock.tick(60)
        pygame.display.update()

game_intro()

pygame.quit()
quit()