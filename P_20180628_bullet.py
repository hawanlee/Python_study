#! python3
# this program add bullrt points to the start
#of each line on the clipboard

import pyperclip
test=pyperclip.paste()
#TODO: seperate lines and add atars.
lines=test.split('\n')
print(lines)
for i in range(len(lines)):
    #loop through all indexs in the lines list
    lines[i]='* '+lines[i]
    #add star to each string in lines list
    test='\n'.join(lines)
pyperclip.copy(test)