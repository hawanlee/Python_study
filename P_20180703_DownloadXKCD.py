#! python3
# download xkcd: download every single comic

import requests, os, bs4

# starting url
url='http://xkcd.com'
# store comics in ./xkcd
#exist_ok=True keyword argument prevents the function from throwing an exception if this folder already exists
os.makedirs('xkcd',exist_ok=True)
while not url.endswith('#'):
    #TODO download the page 
    print('Downloading page %s...' % url)
    res=requests.get(url)
    res.raise_for_status()
    soup=bs4.BeautifulSoup(res.text,'lxml')

    #TODO find the url of the comic image
    comicElem=soup.select('#comic img')
    if comicElem==[]:
        print('Could not find the image')
    else:
        comicUrl=comicElem[0].get('src')
        #TODO download the image
        print('Downloading image %s...' %(comicUrl))
        res=requests.get('http:'+comicUrl)
        res.raise_for_status()

    #TODO save image to ./xkcd
    imageFile=open(os.path.join('xkcd',os.path.basename(comicUrl)),'wb')
    for chunk in res.iter_content(100000):
        imageFile.write(chunk)
    imageFile.close()
    #TODO get the Prev button's url
    preLink=soup.select('a[rel="prev"]')[0]
    url='http://xkcd.com'+preLink.get('href')

print('Done')