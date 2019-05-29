#!/usr/bin/env python

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

    # find a shot
    filters = [ ['project', 'is', {'type': 'Project', 'id': 4}],
            ['code', 'is', '100_010'] ]
    shot = sg.find_one('Shot', filters)

    # find a task
    filters = [ ['project', 'is', {'type': 'Project', 'id': 4}],
            ['entity', 'is',{'type':'Shot', 'id': shot['id']}],
            ['content', 'is', 'Animation'] ]
    task = sg.find_one('Task', filters)
    # linking a Task to the Version is good practice. By doing so it is easy for users to see at what stage a particular Version was created, and opens up other possibilities for tracking in Shotgun. We highly recommend doing this whenever possible.

    # create a version
    data = { 'project': {'type': 'Project','id': 4},
         'code': '100_010_anim_v1',
         'description': 'first pass at opening shot with bunnies',
         'sg_path_to_frames': '/v1/gun/s100/010/frames/anim/100_010_animv1_jack.#.jpg',
         'sg_status_list': 'rev',
         'entity': {'type': 'Shot', 'id': shot['id']},
         'sg_task': {'type': 'Task', 'id': task['id']},
         'user': {'type': 'HumanUser', 'id': 165} }
    result = sg.create('Version', data)

    # Upload a Thumbnail for a Version
    sg.upload_thumbnail("Version", 214, "/v1/gun/s100/010/beauties/anim/100_010_animv1.jpg")