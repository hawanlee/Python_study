#! /usr/bin/env python
# coding=utf-8

import tkinter as tk

# 创建一个主窗口，用于容纳整个GUI程序
root = tk.Tk()

# 设置主窗口对象标题栏
root.title("tkinter demo")

# 添加Label组件，GUI最常用的组件之一
# 可以显示文本、图标或者图片
# 这里显示文本
theLabel = tk.Label(root, text='我的第一个窗口程序！')

# 调用Label组件的pack方法，用于自动调节窗口尺寸
theLabel.pack()

# 这时候窗口不会显示，除非执行下面这行代码：
# tkinter.mainloop()通常是程序的最后一行代码，执行后程序进入主事件循环
root.mainloop()

# 界面编程名言
# ‘Don't call me, I will call you’
# GUI程序开发与以往开发经验会有截然不同的感受