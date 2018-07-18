'''
urllib is a package that collects several modules for working wih URLs:
urllib.request for opening and reading URLs
urllib.error containing the exceptions raised by urllib.request
urllib.parse for parsing URLs
urllib.robotparser for parsing robots.txt files
'''

'''
import urllib.request
response=urllib.request.urlopen('http://www.fishc.com')
html=response.read()
html=html.decode('utf-8')
print(html)
'''

'''
#下载猫的图片
import urllib
response=urllib.request.urlopen('http://www.placekitten.com/g/200/300')
catImg=response.read()
print(response.geturl())
print(response.getcode())#200表示连接正常
with open('cat_200_300.jpg','wb') as f:
    f.write(catImg)
'''

#调用有道网站翻译文本
import urllib.request
import urllib.parse

url='http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
#将form data转换为字典
data={}
data['i']='上海通用汽车'
data['from']='AUTO'
data['to']='AUTO'
data['smartresult']='dict'
data['client']='fanyideskweb'
data['salt']='1531042863967'
data['sign']='bc318e26a9dc31e7cebc3dfae857ff82'
data['doctype']='json'
data['version']='2.1'
data['keyfrom']='fanyi.web'
data['action']='FY_BY_REALTIME'
data['typoResult']='false'

#data参数格式必须符合函数中定义的格式使用此函数转换格式
data=urllib.parse.urlencode(data).encode('utf-8')
#urlopen函数有个data参数，如果对其赋值，则HTTP的请求方式就是用post，否则其值为NULL，请求方式是get
response=urllib.request.urlopen(url,data)
#伪装浏览器
req=urllib.request.Request(url,data)
req.add_header( 'Referer','http://fanyi.youdao.com')
req.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36')
html=response.read().decode('utf-8')
print(html)

'''
#使程序每次执行延迟处理 
import time
time.sleep(5)
'''