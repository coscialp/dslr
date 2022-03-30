#!/usr/bin/env python
# -*- coding: UTF8 -*-
"""This is a program will print the describe on dataset"""


import os, sys


"""Add packages dir on pythonpath"""
fpath = os.path.join(os.path.dirname(__file__), 'LibAI')
sys.path.append(fpath)


from LibAI.libmath import Stat
from LibAI.libparser import CSV


def print_all(describe):
    for k, v in describe.items():
        print(v)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Wrong number of arguments!\nUsage:\tpython3 describe.py [PATH OF CSV]', file=sys.stderr)
        exit(1)
    dataset = CSV.open(sys.argv[-1])
    describe = {
        'title': "\t|",
        'count': "Count\t|",
        'mean': "Mean\t|",
        'std': "Std\t|",
        'min': "Min\t|",
        '25%': "25%\t|",
        '50%': "50%\t|",
        '75%': "75%\t|",
        'max': "Max\t|",
        }
    for data in dataset[6:]:
        describe['title'] += '%*s |' % (len(data['name'])+ 4, data['name'])
        describe['count'] += '%*d |' % (len(data['name'])+ 4, Stat.count(data['data']))
        describe['mean'] += '%*.3f |' % (len(data['name'])+ 4, Stat.mean(data['data']))
        describe['std'] += '%*.3f |' % (len(data['name'])+ 4, Stat.std(data['data']))
        describe['min'] += '%*.3f |' % (len(data['name'])+ 4, Stat.min(data['data']))
        describe['max'] += '%*.3f |' % (len(data['name'])+ 4, Stat.max(data['data']))
        describe['25%'] += '%*.3f |' % (len(data['name'])+ 4, Stat.percentiles(data['data'], 25))
        describe['75%'] += '%*.3f |' % (len(data['name'])+ 4, Stat.percentiles(data['data'], 75))
        describe['50%'] += '%*.3f |' % (len(data['name'])+ 4, Stat.median(data['data']))


    print_all(describe)
    
