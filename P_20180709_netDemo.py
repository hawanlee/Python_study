from bs4 import BeautifulSoup
import requests
import urllib
import bs4

html=urllib.request.urlopen('https://sf.taobao.com/item_list.htm?spm=a213w.7398504.filter.18.vyj6aa&category=50025969&city=%D6%A3%D6%DD&province=&auction_start_seg=-1').read()

hSoup=bs4.BeautifulSoup(html,'lxml')
# print(hSoup)
'''
print(type(hSoup))
eSoup=hSoup.select('sf-content')
if len(eSoup)!=0:
    print(len(eSoup))
    print(str(eSoup[0]))
else:
    print('length=0...')
'''


a=hSoup.select('img')
print(type(a))
print(len(a))

for i in range(len(a)):
    print(a[i])
