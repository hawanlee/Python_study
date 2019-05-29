#!/usr/bin/env python
#coding: utf-8

# --------------------------------------
# Imports
# --------------------------------------
import shotgun_api3
from pprint import pprint # useful for debugging
import datetime
import time
from datetime import datetime, timedelta

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

    filters = [['tags', 'name_contains', 'DRC'], ['start_date', 'greater_than', '2019-03-01']]
    
    result = sg.find('Task', filters, ['id','due_date', 'start_date', 'sg_review_time', 'sg_search_date'])
    
    for i in result:
        i['due_date'] = str(i['sg_review_time'])[:10]
        i['start_date'] = str(i['sg_review_time'])[:10]
        i['sg_search_date'] = ''.join(str(i['sg_review_time'])[:10].split('-'))
    # pprint(result)

    for i in result:
        data = {
            'sg_search_date': i['sg_search_date'],
            'due_date': i['due_date'],
            'start_date': i['start_date'],
        }
        sg.update('Task', i['id'], data)