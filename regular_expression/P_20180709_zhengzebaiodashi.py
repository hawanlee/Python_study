import re

a=re.search(r'FishC','I love FishC.com')
print('a= '+str(a))

#.表示通配符
c=re.search(r'.','I love FishC.com')
#the following will print: <_sre.SRE_Match object; span=(0, 1), match='I'>
print('c= '+str(c))
b=re.search(r'Fish.','I love FishC.com')
print('b= '+str(b))

#字符类:匹配字符类中任一字符算作匹配
d=re.search(r'[aeiou]','I love FishC.com')
print('d= '+str(d))

#数字
e=re.search(r'\d','I love5 FishC.com')
print('e= '+str(e))

#匹配IP地址
g=re.search(r'([0-1]\d\d|2[0-4]\d|25[0-5])','188')
print('g= '+str(g))

f=re.search(r'([1]\d\d|[2][0-4]\d|25[0-5]\.){3}([0-1]\d\d|2[0-4]\d|25[0-5])','other 192.168.1.1 other')
print('f= '+str(f))
