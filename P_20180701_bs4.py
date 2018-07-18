# 以一个气象网站为例
'''
From the developer tools, you can see that the HTML responsible for the temperature part of the web page is <p class="myforecast-current -lrg">57°F</p>. This is exactly what you were looking for! It seems that the temperature information is contained inside a <p> element with the myforecast-current-lrg class. Now that you know what you’re looking for, the BeautifulSoup module will help you find it in the string.
'''

# Creating a BeautifulSoup Object from HTML
import bs4
import requests

'''
soup.select('div') All elements named <div>
soup.select('#author') The element with an id attribute of author
soup.select('.notice') All elements that use a CSS class attribute named notice
soup.select('div span') All elements named <span> that are within an element named <div>
soup.select('div > span') All elements named <span> that are directly within an element named <div>, with no other element in between
soup.select('input[name]') All elements named <input> that have a name attribute with any value
soup.select('input[type="button"]') All elements named <input> that have an attribute named type with value button
'''

exapFile = open('./study_0/P_2018/P_20180701_bs4_html.html')
exapSoup = bs4.BeautifulSoup(exapFile.read())
print(type(exapSoup))
elems = exapSoup.select('#author')
# 选出id='author'的元素
print(type(elems))
print(len(elems))
# 告诉我们在网页中找到一个符合的标签
print(type(elems[0]))
print(elems[0].getText())
# 返回元素的文本或者inner html
print(str(elems[0]))
# 转换成字符串后会返回包含开始和结束标签的语句
print(elems[0].attrs)
# attrs返回元素属性的字典,'id':'author'

print('\nThe following is other try:\n')
pElem = exapSoup.select('p')
print('p包含', end='')
print(str(len(pElem))+'个元素')
print(str(pElem[0]))
print(pElem[0].getText())
print(str(pElem[1]))
print(pElem[1].getText())
print(str(pElem[2]))
print(pElem[2].getText())

#Getting Data from an Element’s Attributes
#传入属性名字符串，返回属性值
print('\n下面输出的是get()方法实例\n')
soup=bs4.BeautifulSoup(open('./study_0/P_2018/P_20180701_bs4_html.html'))
spanElem=soup.select('span')[0]
#获取第一个匹配搜索的元素
print(str(spanElem))
print(spanElem.get('id'))
#获取id的属性值
print(spanElem.get('some_noneexistent_addr')==None)
#当此属性不存在时返回的值是None
print(spanElem.attrs)
