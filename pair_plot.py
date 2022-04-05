#!/usr/bin/env python
# -*- coding: UTF8 -*-
"""This is a program will print the pair plot"""


import os, sys


"""Add packages dir on pythonpath"""
fpath = os.path.join(os.path.dirname(__file__), 'LibAI')
sys.path.append(fpath)


from matplotlib import pyplot as plt
from LibAI.libgraphics import Graphics
from LibAI.libparser import CSV


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Wrong number of arguments!\nUsage:\tpython3 describe.py [PATH OF CSV]', file=sys.stderr)
        exit(1)

    dataset = CSV.open(sys.argv[1])

    Graphics.pairplot(dataset, 'Hogwarts House')
    Graphics.show()