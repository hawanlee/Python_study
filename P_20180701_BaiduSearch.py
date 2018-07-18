#! python3
#Open several Google search results in the browser

'''
It would be nice if I could simply type a search term on the command line and have my computer automatically open a browser with all the top search results in new tabs. Let’s write a script to do this.
'''

# TODO Gets search keywords from the command line arguments or clipboard.
import requests, sys, webbrowser, bs4, pyperclip

print('Baidu_ing....')
#display text while downloading
if len(sys.argv)>1:
    #Get searchContent from command line .
    searchContent=''.join(sys.argv[1:])
else:
    #Get searchContent in clipboard
    searchContent=pyperclip.paste()

# res=requests.get('https://www.baidu.com/s?wd='+searchContent)
res=requests.get('https://www.baidu.com/s?wd=%E5%BE%88%E5%B9%B8%E8%BF%90')
res.raise_for_status()
# webbrowser.open('https://www.baidu.com/s?wd='+searchContent)
# TODO Retrieves the search results page.
'''
use the selector '.t a' to find all <a> elements that are within an element that has the t CSS class.
'''
soup=bs4.BeautifulSoup(res.text,'lxml')
linkElems=soup.select('html')
print(len(linkElems))
# TODO Opens a browser tab for each result.
print(linkElems[0])
'''
numOpen=min(7,len(linkElems))
for i in range(numOpen):
    webbrowser.open(linkElems[i].get('href'))
'''
print('Are you OK?')