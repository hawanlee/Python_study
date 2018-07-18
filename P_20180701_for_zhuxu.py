#下载猫的图片
import urllib,math

a=100
b=200
for i in range(100):
    if i<25:
        a=100+i*10
        b=200+i*10
        response=urllib.request.urlopen('http://www.placekitten.com/g/'+str(a)+'/'+str(b))
        catImg=response.read()
        print(response.geturl())
        print(response.getcode())#200表示连接正常
        with open('cat+'+str(i)+'.jpg','wb') as f:
            f.write(catImg)
    else:
        a=10+i*5
        b=10+i*5
        response=urllib.request.urlopen('http://www.placekitten.com/g/'+str(a)+'/'+str(b))
        catImg=response.read()
        print(response.geturl())
        print(response.getcode())#200表示连接正常
        with open('cat+'+str(i)+'.jpg','wb') as f:
            f.write(catImg)
            