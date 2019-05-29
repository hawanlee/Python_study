#!/usr/bin/env python
#coding: utf-8

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

    filters = [['tags', 'name_contains', 'EDR'], ['start_date', 'greater_than', '2019-03-01']]

    result = sg.find('Task', filters, ['id','due_date', 'sg_search_date'])

    pprint(result)

    # for i in result:
    #     i['sg_search_date'] = ''.join(i['due_date'].split('-'))
    #     data = {
    #         'sg_search_date': i['sg_search_date']
    #     }
    #     sg.update('Task', i['id'], data)
