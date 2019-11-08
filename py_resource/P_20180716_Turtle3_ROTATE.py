# -*- coding:UTF-8 -*-

import pygame
import sys
from pygame.locals import *

pygame.init()
size = width, height = 800, 600
bg = (255, 255, 255)

clock = pygame.time.Clock()
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Rotate Demo')
turtle = pygame.image.load('turtle.png')
position = turtle_rect = turtle.get_rect()
# 小乌龟顺时针行走
speed = [5, 0]
turtleRight = pygame.transform.rotate(turtle, 90)
turtleTop = pygame.transform.rotate(turtle, 180)
turtleLeft = pygame.transform.rotate(turtle, 270)
turtleBottom = turtle
# 刚开始走在顶部

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
    position = position.move(speed)

    if position.right > width:
        turtle = turtleRight
        # 旋转后矩形尺寸也发生变化
        position = turtle_rect = turtle.get_rect()
        # 矩形尺寸的变化导致位置也有变化
        position.left = width-turtle_rect.width
        speed = [0, 5]
    if position.bottom > height:
        turtle = turtleBottom
        position = turtle_rect = turtle.get_rect()
        position.left = width-turtle_rect.width
        position.top = height-turtle_rect.height
        speed = [-5, 0]
    if position.left < 0:
        turtle = turtleLeft
        position = turtle_rect = turtle.get_rect()
        position.top = height-turtle_rect.height
        speed = [0, -5]
    if position.top < 0:
        turtle = turtleTop
        position=turtle_rect=turtle.get_rect()
        speed=[5,0]

    screen.fill(bg)
    screen.blit(turtle,position)
    pygame.display.flip()
    clock.tick(60)
        
