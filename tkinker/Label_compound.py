#! /usr/bin/env python
# coding=utf-8

from tkinter import *

root=Tk()
photo=PhotoImage(file='turtle.png')

# 设置文字与图片混排
theLabel=Label(root,text='hello, \nturtle', justify=LEFT, image=photo, compound=CENTER, font=('none',20), fg='blue')

theLabel.pack()

mainloop()