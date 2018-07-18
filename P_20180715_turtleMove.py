# -*- coding:UTF-8 -*-

import pygame
import sys

# 初始化pygame的模块，让它们做好准备随时被调用
pygame.init()
# 创建一个SURFACE对象，将其作为背景画布
# surface对象就是pygame用来表示图像的对象，即图像
size = width, height = 800, 600
speed = [-2, 1]
bg = (255, 255, 255)
screen = pygame.display.set_mode(size)
pygame.display.set_caption('初次见面，请多多关照!')
# 使用image.load()加载图片
turtle = pygame.image.load('turtle.png')
# 获得该图像的矩形区域
position = turtle.get_rect()

# 让图像不断移动的‘死循环’
while True:
    # 用户的一切行为都会变成一个个事件消息，放入事件队列里面，在这里迭代获取每个事件消息，检测到退出事件后，使用exit退出程序
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
# Rect对象有移动方法，实际上就是修改矩形的坐标
# 每次调用即修改一次坐标，[-2,1]即水平位置-2，垂直位置+1
    position = position.move(speed)
# 乌龟撞左右墙后让其掉头并改变移动方向
    if position.left < 0 or position.right > width:
        turtle = pygame.transform.flip(turtle, True, False)
        speed[0] = -speed[0]
# 改变上下移动方向
    if position.top < 0 or position.bottom > height:
        speed[1] = -speed[1]
# 这两句用于填充背景颜色和将移动后的乌龟放上去，surface.blit()将一个对象放到另一个对象的上方
# 将屏幕刷白，再将移动后的小乌龟画上去（实际上是修改背景画布中乌龟位置的像素颜色）
    screen.fill(bg)
    screen.blit(turtle, position)
# 刷新画面，pygame采用双缓冲模式，调用下面函数将缓冲好的画面一次性刷新到显示器上。双缓冲，即在内存中创建一个与屏幕绘图区域一直的对象，先将图形绘制到内存中的这个对象上，再一次性将这个对象上的图形复制到屏幕上，大大加快绘图速度以及避免屏幕闪烁现象
    pygame.display.flip()
# 让程序挂起5毫秒，避免速度极快
# pygame支持每秒钟切换40-200次图像
    pygame.time.delay(5)

'''
time模块有个clock类，可以用来实现帧率的控制
clock=pygame.time.Clock() # 实例化Clock对象
clock.tick(200) # 设置不高于200帧运行
clock.tick(1) # 每秒一帧
'''