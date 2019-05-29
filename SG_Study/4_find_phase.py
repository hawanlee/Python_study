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
SERVER_PATH = "https://lemontree.shotgunstudio.com"
SCRIPT_NAME = 'hawanlee'
SCRIPT_KEY = 'iocuckamyhmzfh)rVqsea4uxo'

# -------------------------C:\Users\hawan\AppData\Local\conda\conda\envs\py2-------------
# Main
# --------------------------------------
if __name__ == '__main__':

    sg = shotgun_api3.Shotgun(SERVER_PATH, SCRIPT_NAME, SCRIPT_KEY)

    filters = [['id', 'is', 22]]
    result = sg.find_one('Phase', filters, ['start_date','end_date'])
    pprint(result)