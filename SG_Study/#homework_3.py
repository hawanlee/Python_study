#coding:utf-8

import shotgun_api3
from pprint import pprint # useful for debugging

# make sure to change this to match your Shotgun server and auth credentials.
SERVER_PATH = "http://10.203.108.21"
SCRIPT_NAME = 'SG_Script_study_lhw_1'
SCRIPT_KEY = '88fd1416060a39491e3138c77a474271d4e4536910d545fddb20e338478a440c'


sg = shotgun_api3.Shotgun(SERVER_PATH, SCRIPT_NAME, SCRIPT_KEY)


ids = [12074, 12078, 12079, 12075, 12076, 12077, 12220]


filters = [
        # ['project','is',{'type': 'Project', 'id': 97}]
        ['content', 'is', "UDMB(358 LEGACY)"]
        ]

result = sg.find('Task', filters, ['content','start_date'])
print(result)
sg.delete("Task",12138)