#! python3
# an insecure password locker pragram
import sys
import pyperclip

PASSWORDS={'email':'yhblsqt2016','qq':'793109917','luggage':'2589'}
if len(sys.argv)<2:
    print('Usage:python P_0623_pw.py [account] - copy account password')
    sys.exit()

account=sys.argv[1]
#first command line arg is the account name

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Password for '+account+' copied to clipboard.')
else:
    print('There is no account named '+account)