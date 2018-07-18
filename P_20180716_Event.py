# -*- coding:UTF-8 -*-

import pygame
import sys
from pygame.locals import *

pygame.init()
size = width, height = 600, 400
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Event Demo')
f = open('record_event.txt','w')

while True:
    for event in pygame.event.get():
        f.write(str(event)+'\n')
        if event.type == pygame.QUIT:
            f.close()
            sys.exit()