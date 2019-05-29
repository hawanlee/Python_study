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

    # --------------------------------------
    # Create a Shot with data
    # --------------------------------------
    data = {
        'project': {"type":"Project","id": 104},
        # project is a link to the Project the Shot belongs to. It should be a dictionary like {"type": "Project", "id": 123} where id is the id of the Project.

        'code': '100_010',
        # code (this is the field that stores the name Shot)

        'description': 'Open on a beautiful field with fuzzy bunnies',

        'sg_status_list': 'ip'
    }
    result = sg.create('Shot', data)
    pprint(result)
    print "The id of the %s is %d." % (result['type'], result['id'])