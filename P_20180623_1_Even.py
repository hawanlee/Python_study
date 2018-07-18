import sys


def collatz(n):
    try:
        n1=int(n)
    except ValueError:
        print('Please input a Integer! Need Redo')
        sys.exit()
    a = n1 % 2
    if a == 0:
        return n1/2
        print('it is Even')
    else:
        return n1*3+1
        print('it is Odd')


num = input('Please input a number:')
num1 = collatz(num)
print(num1)

m=' '.join(['my','name','is','li haiwang'])
for i in m:
    print(i,end='')
print('\n')
m=m.split(' ')
for i in m:
    print(i,end='')
print('\n')
print('Hello'.rjust(15))
print('Hello'.center(15))