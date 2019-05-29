# 函数、包
# 函数：可以重复使用的代码片段


def say_hello():
    print('hello world!')

    # 函数结束
say_hello()


def print_max(a=3, b=4):
    print('a='+str(a)+', b='+str(b))
    print('the bigger one is: ', end='')
    if a > b:
        print(a)
    else:
        print(b)


print_max(4, 5)
print_max(16, 9)
print_max()

# 可变参数


def total(a, b, **c):
    print('a = '+str(a))
    for i in b:
        print('b = '+str(i))
    for m in c:
        print('c = '+str(m)+':'+c[m])


total(4545, [6, 3, 25, 2], qq='ww', ee='rr', tt='yy', uu='ii')

print('x='+str(int(2.9)))

# 函数作用域
# 仅在函数中有作用域，其它语句块没有作用域

# launch jupyter: cmd->jupyter-notebook

# 模块安装，程序先在本地寻找，可以将模块放在本地项目文件夹
# 包：比模块高一级的组织单元


