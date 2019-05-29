#!/usr/bin/env python
# -*- coding: utf-8 -*-

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

    # 思路：找到全部version及对应用户名，抽取用户名组成列表，统计用户名出现次数并对应输出

    # 找到所有包含用户名与对应version的条目，得到一个固定格式的列表
    filters = [['sg_status_list', 'is_not', 'hello']]
    result = sg.find('Version',filters,['user'])
    # pprint(result[0])
    # pprint(result[0]['user']['name'])

    names = []
    names_count = {}
    for i in range(0,len(result)):
        # 这三步是抽取用户名中英文部分，中文部分是乱码，暂时先去掉
        a = result[i]['user']['name'][::-1]
        b = a.split(' ')
        c = b[0]+' '+b[1]
        
        names.append(c[::-1])

    # 列表去重，直接创建集合得到去重结果
    names_single = set(names)

    # 以字典格式创建用户名及对应数量，得到一个集合
    for i in names_single:
        count = 0
        for j in names:
            if i==j:
                count += 1
        # names_count[i].encode()
        names_count[i] = count

    # 以数量大小进行列表排序，需先把数量值放到前面
    f = zip(names_count.values(), names_count.keys())
    g = sorted(f, reverse=True)

    # 输出结果
    pprint(g)