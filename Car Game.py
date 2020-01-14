#https://www.youtube.com/watch?v=NOyfgCz05Yo

import pygame
import time
import sys
import random
pygame.init()
#color
gray=(119,118,110)
white=(255,255,255)
black=(0,0,0)
red=(200,0,0)
green=(0,200,0)
blue=(0,0,255)
bright_red=(255,0,0)
bright_green=(0,255,0)
window_width=800
window_hight=600
#display surface
gd = pygame.display.set_mode([window_width, window_width])
carimg =pygame.image.load('Car_Images/Topdown_vehicle_sprites_pack/Car.png')
car1=pygame.transform.scale(carimg, (100,100))
clock = pygame.time.Clock()

def car (x,y) :
    gd.blit(car1, (x, y))
    pygame.display.update()

def gameloop() :
    x_change = 0
    y_lead = 0
    x = 300
    y = 490
    block = 10
    game_over = False
    while game_over == False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over= True
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
        car(x,y)

        clock.tick(60)
        pygame.display.update()


gameloop()