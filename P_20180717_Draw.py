# -*- coding:utf-8 -*-

import pygame
import sys
from pygame.locals import *
import math

'''
绘制矩形
rect(Surfce, color, Rect, width=0)
第一个参数指定绘制在哪个对象上
第二个参数指定颜色
第三个参数指定矩形范围（left,top,width,height）
第四个指定矩形边框的大小，0表示填充矩形
'''

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

pygame.init()
size = width, height = 800, 800
clock = pygame.time.Clock()
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Draw a rectangle')
points = [(200, 175), (300, 125), (400, 175), (452, 125),
          (450, 225), (400, 175), (300, 225)]
center = (300, 300)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()

    screen.fill(WHITE)

    # rect(Surfce, color, Rect, width=0)
    pygame.draw.rect(screen, BLACK, (50, 50, 150, 0), 0)
    pygame.draw.rect(screen, BLACK, (250, 50, 150, 50), 1)
    pygame.draw.rect(screen, BLACK, (450, 50, 150, 50), 10)

    # polygon(Surface, color, pointlist, width=0)
    pygame.draw.polygon(screen, BLACK, points, 0)

    # circle(Surface, color, center, radius, width)
    pygame.draw.circle(screen, BLACK, center, 50, 5)

    # 椭圆形根据矩形绘制
    pygame.draw.ellipse(screen, BLACK, (200, 400, 200, 100), 0)
    pygame.draw.ellipse(screen, BLACK, (200, 600, 150, 150), 0)

    # arc(Surface, color, Rect, startAngle, endAngle, width=1)
    #开始结束角度使用弧度表示
    pygame.draw.arc(screen, BLACK, (400,600,200,100),math.pi,2*math.pi,5)
    
    pygame.display.flip()
    clock.tick(10)
