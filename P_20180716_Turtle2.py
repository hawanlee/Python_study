# -*- coding:UTF-8 -*-

import pygame
import sys
from pygame.locals import *
# 将pygame的所有常量名导入

pygame.init()
size = width, height = 800, 600
bg = (255, 255, 255)
speed = [1, 1]
clock = pygame.time.Clock()
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Crazy Turrle')
turtle = pygame.image.load('turtle.png')
# turtle = pygame.transform.flip(turtle, True, False)
position = turtle.get_rect()
l_head = turtle
r_head = pygame.transform.flip(turtle, True, False)

'''
fullscreen = False
# 快捷键全屏F11
if event.key == K_F11:
    fullscreen = not fullscreen
    if fullscreen:
        screen = pygame.display.set_mode((1920, 1080), FULLSCREEN | HWSURFACE)
    else:
        screen = pygame.display.set_mode(size)
'''

# pygame常用的事件及含义参见书中列表
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
    if event.type == KEYDOWN:
        if event.key == K_LEFT:
            speed = [-1, 0]
            turtle = l_head
        if event.key == K_RIGHT:
            speed = [1, 0]
            turtle = r_head
        if event.key == K_UP:
            speed = [0, -1]
        if event.key == K_DOWN:
            speed = [0, 1]
    position = position.move(speed)
    if position.left < 0 or position.right > width:
        turtle = pygame.transform.flip(turtle, True, False)
        speed[0] = -speed[0]
    if position.top < 0 or position.bottom > height:
        speed[1] = -speed[1]
    screen.fill(bg)
    screen.blit(turtle, position)
    pygame.display.flip()
    clock.tick(200)
