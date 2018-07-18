'''
def isPhoneNumber(text):
    if len(text)!=12:
        return False
    for i in range(0,3):
        if not text[i].isdecimal():
            return False
    if text[3]!='-':
        return False
    for i in range(4,7):
        if not text[i].isdecimal():
            return False
    if text[7]!='-':
        return False
    for i in range(8,12):
        if not text[i].isdecimal():
            return False
    return True

print('424-322-2332 is '+str(isPhoneNumber('424-322-2332')))
# print('424-322-233 is '+isPhoneNumber('424-322-233'))
message='Call me 415-555-5545. 695-412-5226 is my office'
for i in range(len(message)):
    chunk=message[i:i+12]
    if isPhoneNumber(chunk):
        print('Phone number found '+chunk)
print('Done')
'''

import re

message='Call me 415-555-5545. 695-412-5226 is my office'
phoneNumberRegex=re.compile(r'\d{3}-\d{3}-\d{4}')
mo=phoneNumberRegex.search(message)
print(mo.group())
phoneNumberRegex_1=re.compile(r'(\d{3})-(\d{3}-\d{4})')
mo_1=phoneNumberRegex_1.search(message)
print(mo_1.group(1))
print(mo_1.group(2))
print(mo_1.groups())

# (Ha){3,5} can match three, four, or five instances of Ha in the string 'HaHaHaHaHa',

'''
The \( and \) escape characters in the raw string passed to re.compile() will match
actual parenthesis characters.
'''

# |的作用：The | character is called a pipe. You can use it anywhere you want to match one of many expressions.
print('usage of "|": ')
heroRegex=re.compile(r'Batman|Tina')
mo2=heroRegex.search('Batman and Tina')
print(mo2.group())
mo3=heroRegex.search('Tina and Batman')
print(mo3.group())

#partial
print('Either match: ')
batRegex=re.compile(r'Bat(man|mobile|copter)')
mo3=batRegex.search('Batmobile lost a wheel')
print(mo3.group())
print(mo3.group(1))

# ?'s demo
batRegex_2=re.compile(r'Bat(wo)?man')
mo4=batRegex_2.search('The Adventures of Batman')
print(mo4.group())

# *matching zero or more with the symbol star
batRegex_3=re.compile(r'Bat(wo)*man')
mo5=batRegex_3.search('The adventure of Batwowowoman')
print(mo5.group())

#greedy and nongreedy matching
greedyHaregex=re.compile(r'(Ha){3,5}')
mo6=greedyHaregex.search('HaHaHaHaHa')
print(mo6.group())
nongreedyHaregex=re.compile(r'(Ha){3,5}?') #declaring a nongreedy match or flagging an optional group.
mo7=nongreedyHaregex.search('HaHaHaHaHa')
print(mo7.group())

message='Call me 415-555-5545. 695-412-5226 is my office'
phoneNumberRegex=re.compile(r'\d{3}-\d{3}-\d{4}')
mo8=phoneNumberRegex.findall(message)
print(mo8)

xmasRegex=re.compile(r'\d+\s\w+')
mo9=xmasRegex.findall('12 drummers, 11 pipers, 10 lords, 8maids')
print(mo9)

'''
Review of Regex Symbols
This chapter covered a lot of notation, so here’s a quick review of what you learned:
The ? matches zero or one of the preceding group.
The * matches zero or more of the preceding group.
The + matches one or more of the preceding group.
The {n} matches exactly n of the preceding group.
The {n,} matches n or more of the preceding group.
The {,m} matches 0 to m of the preceding group.
The {n,m} matches at least n and at most m of the preceding group.
{n,m}? or *? or +? performs a nongreedy match of the preceding group.
^spam means the string must begin with spam.
spam$ means the string must end with spam.
The . matches any character, except newline characters.
\d, \w, and \s match a digit, word, or space character, respectively.
\D, \W, and \S match anything except a digit, word, or space character, respectively.
[abc] matches any character between the brackets (such as a, b, or c).
[^abc] matches any character that isn’t between the brackets.

re.IGNORECASE or re.I as a second argument to re.compile()


已学到P195，需要继续学习p195的前几节
'''

