#! /usr/bin/env python
# coding=utf-8

import tkinter as tk


class App:
    def __init__(self, root):

        # 创建一个框架，然后在里面添加一个Button按钮组件
        # 框架一般用于在复杂的布局中起到将组件分组的作用
        frame = tk.Frame(root)
        frame.pack()

        # 创建一个按钮，fg：foreground前景色，设置前景色为蓝色
        self.hi_there = tk.Button(
            frame, text='打招呼', bg='green', fg='red', command=self.say_hi)

        # side参数可以设置TOP, BOTTOM, LEFT, RIGHT四个方位，默认为TOP
        # padx,pady参数自定义按钮的偏移位置
        self.hi_there.pack(side=tk.LEFT, padx=10, pady=10)

    def say_hi(self):
        print('Hello everyone!')


# 创建toplevel的根窗口，并把它作为参数实例化app对象
root = tk.Tk()
app = App(root)

# 开始主事件循环
root.mainloop()
