#! /usr/bin/env python
# coding=utf-8

# 导入tkinter模块的所有内容
from tkinter import *

root = Tk()

# 创建一个文本Label对象
textLabel = Label(root, text='一只乌龟指着这些字！', fg='white', bg='black', justify=LEFT, padx=10, pady=5)
textLabel.pack(side=LEFT)

# 创建一个图像Label对象
# 用PhotoImage实例化一个图片对象
photo = PhotoImage(file='turtle.png')
imgLabel = Label(root, image=photo)
imgLabel.pack(side=RIGHT)

mainloop()
