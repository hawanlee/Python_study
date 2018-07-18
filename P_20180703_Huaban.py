#! python3
# download xkcd: download every single comic

import requests, os, bs4

# starting url
url='http://huaban.com/pins/1561612007/'
# store comics in ./xkcd
#exist_ok=True keyword argument prevents the function from throwing an exception if this folder already exists
os.makedirs('Huaban_gh',exist_ok=True)
i=0
while i<689:
    #TODO download the page
    print('Downloading page %s in progress...' % url)
    res=requests.get(url)
    res.raise_for_status()
    soup=bs4.BeautifulSoup(res.text,'lxml')

    #TODO find the url of the comic image
    comicElem=soup.select('.main-image img')
    if comicElem==[]:
        print('Could not find the image')
    else:
        comicUrl=comicElem[0].get('src')
        #TODO download the image
        print('Downloading image %s in progress' %(comicUrl))
        res=requests.get('http:'+comicUrl)
        res.raise_for_status()

    #TODO save image to ./xkcd
    imageFile=open(os.path.join('Huaban_gh',os.path.basename(comicUrl)),'wb')
    for chunk in res.iter_content(100000):
        imageFile.write(chunk)
    imageFile.close()
    #TODO get the Prev button's url
    preLink=soup.select('a[class="next x layer-view"]')[0]
    url='http://huaban.com'+preLink.get('href')

    i=i+1

print('Done')