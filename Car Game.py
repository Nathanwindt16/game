#https://www.youtube.com/watch?v=NOyfgCz05Yo

import pygame
import time
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
gd=pygame.display.set.mode((window_width, window_hight))
carimg =pygame.image.load('./Car Images/Police.png')
car1=pygame.transform.scale(carimg, (100,100))
clock = pygame.time.Clock()