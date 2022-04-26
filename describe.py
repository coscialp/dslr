#!/usr/bin/env python
# -*- coding: UTF8 -*-
"""This is a program will print the describe on dataset"""


import os, sys


"""Add packages dir on pythonpath"""
fpath = os.path.join(os.path.dirname(__file__), 'LibAI')
sys.path.append(fpath)


from LibAI.libmath import Math, Stat
from LibAI.libparser import CSV


def print_all(describe):
    for k, v in describe.items():
        print(v)


if __name__ == '__main__':
    if len(sys.argv) < 2 or len(sys.argv) > 3:
        print('Wrong number of arguments!\nUsage:\tpython3 describe.py [PATH OF CSV] [OPTION]', file=sys.stderr)
        exit(1)
    if len(sys.argv) == 3 and sys.argv[2] != '--filters':
        print('Bad option\nUsage:\tpython3 describe.py [PATH OF CSV] [OPTION]', file=sys.stderr)
        exit(1)

    dataset = CSV.open(sys.argv[1])

    if len(sys.argv) == 3:
        print('Which column do you want to pick? (say end for end)')
        column = []
        while 1:
            str = input()
            if str == 'end':
                break
            if str == 'all':
                column = None
                break
            column.append(str)

        print('Which filters do you want to use? (say end for end)')
        while 1:
            filters = []
            str = input()
            if str == 'end':
                break
            if str == 'all':
                filters = None
                break
            filters.append(str)

        print('Which column do you want to use for filters?')
        where = input()
        
        dataset = CSV.filter(dataset, columns=column, where=where, filters=filters)

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

    for data in dataset:
        if Math.isfloat(data['data'][0]) and data['name'] != 'Index' and data['name'] != 'Hogwarts House':
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
    
