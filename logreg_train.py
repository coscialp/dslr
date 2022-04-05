"""This is a training program of logistic regression"""


import os, sys


"""Add packages dir on pythonpath"""
fpath = os.path.join(os.path.dirname(__file__), 'LibAI')
sys.path.append(fpath)


import numpy as np
from matplotlib import pyplot as plt
from LibAI.libgraphics import Graphics
from LibAI.libparser import CSV


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Wrong number of arguments!\nUsage:\tpython3 describe.py [PATH OF CSV]', file=sys.stderr)
        exit(1)

    dataset = CSV.open(sys.argv[1])

    for name, data in dataset:
        if name == 'Hogwarts House':
            for house in data:
                pass