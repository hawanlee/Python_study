import os
print(os.getcwd())


helloFile = open(r'c:\users\hawan\study\python\study_0\hello.txt', 'r')
helloContent = helloFile.read()
print(helloContent)
sonnetFile = open(r'c:\users\hawan\study\python\study_0\sonnet36.txt', 'r')
print(sonnetFile.readlines())
baconFile = open(r'c:\users\hawan\study\python\study_0\bacon.txt', 'w')
baconFile.write('Hello becon\n')
baconFile.close()
baconFile = open(r'c:\users\hawan\study\python\study_0\bacon.txt', 'a')
baconFile.write('How do you feel?')
baconFile.close()
baconFile = open(r'c:\users\hawan\study\python\study_0\bacon.txt')
print(baconFile.readlines())


import shelve

shelfFile = shelve.open('mydata')
cats = ['zophie', 'pooka', 'simon']
shelfFile['cats'] = cats
shelfFile.close()
'''
To read and write data using the shelve module, you first import shelve. Call shelve.open() and pass it a filename, and then store the returned shelf value in a variable. You can make changes to the shelf value as if it were a dictionary. When you’re done, call close() on the shelf value. Here, our shelf value is stored in shelfFile. We create a list cats and write shelfFile['cats'] = cats to store the list in shelfFile as a value associated with the key 'cats' (like in a dictionary). Then we call close() on shelfFile.
'''
shelfFile=shelve.open('mydata')
print(type(shelfFile))
print(shelfFile['cats'])
shelfFile.close()
'''
Just like dictionaries, shelf values have keys() and values() methods that will return listlike values of the keys and values in the shelf. Since these methods return list-like values instead of true lists, you should pass them to the list() function to get them in list form.
'''
shelfFile=shelve.open('mydata')
print(list(shelfFile.keys()))
print(list(shelfFile.values()))
shelfFile.close()
'''
Plaintext is useful for creating files that you’ll read in a text editor such as Notepad or TextEdit, but if you want to save data from your Python programs, use the shelve module.
'''

print('Next: pprint')
import pprint

cats_1=[{'name':'zophie','desc':'chubby'},{'name':'pooka','desc':'fluffy'}]
print(pprint.pformat(cats_1))
fileObj=open('myCats.py','w')
fileObj.write('cats_1 = '+pprint.pformat(cats_1)+'\n')
fileObj.close()

import myCats
print(myCats.cats_1)
print(myCats.cats_1[0])
print(myCats.cats_1[0]['desc'])

Page208