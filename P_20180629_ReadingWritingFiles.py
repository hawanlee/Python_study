'''
Variables are a fine way to store data while your program is running, but if you want your,data to persist even after your program has finished, you need to save it to a file. You can think of a file’s contents as a single string value, potentially gigabytes in size.
'''
'''
The C:\ part of the path is the root folder, which contains all other folders. On Windows, the root folder is named C:\ and is also called the C: drive. On OS X and Linux, the root folder is /.
Additional volumes, such as a DVD drive or USB thumb drive, will appear differently on different operating systems. On Windows, they appear as new, lettered root drives, such as D:\ or E:\. On OS X, they appear as new folders under the /Volumes folder. On Linux, they appear as new folders under the /mnt (“mount”) folder. Also note that while folder names and filenames are not case sensitive on Windows and OS X, they are case sensitive on Linux.
'''

import os
a1=os.path.join('usr','bin','spam')
print(a1)
#使用os.path.join避免在不同操作系统出现的文件路径问题

a2=os.getcwd()
print(a2)
#os.chdir('c:\\windows\\System32') 改变工作路径
# .\代表当前文件夹（使用当前文件夹可省略不写），..\代表父级文件夹
#os.makedirs('C:\\Users\\hawan\\study\\python\\temp') #创建路径，已存在时再次创建会报错
a3=os.path.abspath('P_2018') #将相对路径转化诶绝对路径
print(a3)
#os.isabs()判断是否为绝对路径
# os.path.dirname(path) 返回路径
# os.path.basename(path) 返回文件名加后缀
# os.path.split() 包含二者字符串的元组
# 
a4=os.getcwd().split(os.path.sep)
print (a4)
#列出当前路径下所有文件
print(os.listdir(r'study_0\P_2018'))
totalSize=0
for i in os.listdir(r'study_0\P_2018'):
    totalSize=totalSize+os.path.getsize(os.path.join('study_0\\P_2018',i))
#计当前目录下所有文件的大小总和
print(totalSize)

