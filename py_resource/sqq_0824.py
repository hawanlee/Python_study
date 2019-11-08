a=1
b=2
print(a+b)

c=float(input('input a numbser: '))
f=1.8*c+32
print(f)

pai=3.14
radius=float(input('input a number'))
s=pai*radius**2
c=2*radius*pai
print(s)
print(c)

# bmi=w/h**2

w=float(input('please input your weight:' ))
h=float(input('please input your height:'))
bmi=w/h**2
print(w)
print(h)
print('Your BMI is: '+str(bmi))

# 闰年：满足其一就是闰年
# 1. 能被4整除并且不能被100整除
# year%4==0 and year%100!=0
# 2. 能被400整除
# year%400==0

year = int(input('please input year:'))
t = year % 4 == 0 and year % 100 != 0 or year % 400 == 0
print(t)

a = False

if (a):
  print(456)
else:
  print(123)

light = input('当前红绿灯颜色：')
if(light == 'red'):
  print('stop!')
elif(light == 'green'):
  print('go!')
elif(light == 'yellow'):
  print('wait a moment!')
else:
  print('the light is broken!')

year = int(input('please input year:'))
t = year % 4 == 0 and year % 100 != 0 or year % 400 == 0
if(t):
  print("我今年过生日")
else:
  print("今年不过生日")

n = int(input ("please a number\n"))
t = n%2==0
if(t):
  print("The number is a even number")
else:
  print("The number is an odd number")

s = 0
for i in range(1, 101):
  s = s + i
print(s)

a=1
while(a<=100):
  s = s + a
  a = a + 1
print(s)

for i in range (1,101):
  if (i%2!=0):
    print(i)

# 输出100-999之间的水仙花数
# 水仙花数：一个三位数本身等于它的每位数字的立方之和
# 123 == 1*1*1+2*2*2+3*3*3

for a in range(100, 1000):
  bai = a//100   #整除100
  shi = a%100//10   #用100取余后整除10
  ge = a%10   #用10取余
  is_equal = a==bai**3+shi**3+ge**3
  if (is_equal):
    print(a)

# 质数：一个数只能被1和它本身整除，2,3,5,7...
print(2)
print(3)
for a in range (4,1001):
  _n = True
  for b in range(2,a):
    if (a%b==0):
      _n = False
      break
  if _n:
    print(a)

# 1, 5, 10, 20 组成 100
a=4
while(a<1001):
  _n = True
  b=2
  while(b<a):
    if (a%b==0):
      _n = False
      break
    b=b+1
  if _n:
    print(a)
  a = a+1

# 求阶乘
n! = 1*2*3*...*n
5! = 1*2*3*4*5

m=int(input('input a number:'))
a=1
for n in range(1,m+1):
  a=a*n
print(a)

# score
m=float(input("please a munber:"))
level=''
if m>=90:
  level="A"
elif m>=80:
  level="B"
elif m>=70:
  level="C"
elif m>=60:
  level="D" 
else:
  level="E"
print(level)