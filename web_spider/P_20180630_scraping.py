'''
Page 259
webbrowser. Comes with Python and opens a browser to a specific page.
Requests. Downloads files and web pages from the Internet.
Beautiful Soup. Parses HTML, the format that web pages are written in.
Selenium. Launches and controls a web browser. Selenium is able to fill in forms and simulate mouse clicks in this browser.
'''
import webbrowser

# webbrowser.open('http://www.baidu.com')

import requests

res=requests.get('http://www.gutenberg.org/cache/epub/1112/pg1112.txt')
print(type(res))
print(res.status_code==requests.codes.ok)
#上边这行语句可以检查是否下载成功,或者：
try:
    res.raise_for_status()
except Exception as exc:
    print('There was a problem : %s' %(exc))
# Always call raise_for_status() after calling requests.get(). You want to be sure that the download has actually worked before your program continues.

print(len(res.text))
print(res.text[:488])

# Saving Downloaded Files to the Hard Drive
# you need to write binary data instead of text data in order to maintain the Unicode encoding of the text.
# To write the web page to a file, you can use a for loop with the Response object’s iter_content() method.

playFile=open('RomeoAndJuliet.txt','wb')
for chunk in res.iter_content(10000):
    playFile.write(chunk)
playFile.close()

# The iter_content() method returns “chunks” of the content on each iteration through the loop. Each chunk is of the bytes data type, and you get to specify how many bytes each chunk will contain. One hundred thousand bytes is generally a good size, so pass 100000 as the argument to iter_content().The iter_content() method returns “chunks” of the content on each iteration through the loop.  each chunk is of the bytes data type, and you get to specify how many bytes each chunk will contain. One hundred thousand bytes is generally a good size, so  pass 100000 as the argument to iter_content().
'''
To review, here’s the complete process for downloading and saving a file:
1. Call requests.get() to download the file.
2. Call open() with 'wb' to create a new file in write binary mode.
3. Loop over the Response object’s iter_content() method.
4. Call write() on each iteration to write the content to the file.
5. Call close() to close the file.
'''

