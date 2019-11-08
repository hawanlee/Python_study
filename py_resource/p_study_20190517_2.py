#!/usr/bin/env python
#coding: utf-8

# Imports

if __name__ == '__main__':
  f = float(input('请输入华氏温度: '))
  c = (f - 32) / 1.8
  print('%.1f华氏度 = %.1f摄氏度' % (f, c))
