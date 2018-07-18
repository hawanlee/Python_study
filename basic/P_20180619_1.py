import random
import sys
i = 0
while True:
    i += 1
    a = random.randint(1, 10)
    if a == 1:
        print('Done')
        print('I\'ve been tried '+str(i)+' times!')
        break
    else:
        print('Working')
print('dog', 'cat', 'chicken')
print('dog', 'cat', 'chicken', sep='--')

#######

def spam(divi):
    try:
        return 100/divi
    except ZeroDivisionError:
        print('0 is not valid')


print(spam(0))
