#!/usr/bin/env python
#coding:utf-8

# --------------------------------------
# Imports
# --------------------------------------
import shotgun_api3
from pprint import pprint # useful for debugging

# --------------------------------------
# Globals
# --------------------------------------
# make sure to change this to match your Shotgun server and auth credentials.
SERVER_PATH = "http://10.203.108.21"
SCRIPT_NAME = 'SG_Script_study_lhw_1'
SCRIPT_KEY = '88fd1416060a39491e3138c77a474271d4e4536910d545fddb20e338478a440c'

# --------------------------------------
# Main
# --------------------------------------
if __name__ == '__main__':

    sg = shotgun_api3.Shotgun(SERVER_PATH, SCRIPT_NAME, SCRIPT_KEY)

    # EDR REview page auto_complete
    data_review_EDR = {
        'milestone' : True,
        'content' : 'EDR_Review',
        'sg_status_list' : 'fin'
    }

    filters_tag_EDR = [
        ['tag_list', 'is', 'EDR'], 
        # ['id', 'is', 11621],
        ['due_date', 'greater_than', '2018-11-10']
        ]

    result_EDR = sg.find('Task', filters_tag_EDR, ['id'])

    for i in range(0,len(result_EDR)):
        rr = sg.update('Task', result_EDR[i]['id'], data_review_EDR)

    # r2 = sg.update('Task',result[0]['id'], data)


    
