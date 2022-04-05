#!/usr/bin/env python
# -*- coding: UTF8 -*-
"""This is a program will print the histogram"""


import os, sys


"""Add packages dir on pythonpath"""
fpath = os.path.join(os.path.dirname(__file__), 'LibAI')
sys.path.append(fpath)


from matplotlib import pyplot as plt
from LibAI.libgraphics import Graphics
from LibAI.libparser import CSV


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Wrong number of arguments!\nUsage:\tpython3 describe.py [PATH OF CSV] [OPTION]', file=sys.stderr)
        exit(1)

    if len(sys.argv) == 2:
        column = ['Care of Magical Creatures']
    else:
        column = sys.argv[2:]

    dataset = CSV.open(sys.argv[1])


    data_gryffindor = CSV.filter(dataset, column, where='Hogwarts House', filters=['Gryffindor'])
    data_slytherin = CSV.filter(dataset, column, where='Hogwarts House', filters=['Slytherin'])
    data_ravenclaw = CSV.filter(dataset, column, where='Hogwarts House', filters=['Ravenclaw'])
    data_hufflepuff = CSV.filter(dataset, column, where='Hogwarts House', filters=['Hufflepuff'])

    graph = Graphics()

    graph.hist(data_gryffindor[0], '', c='red', a=0.5)
    graph.hist(data_hufflepuff[0], '', c='yellow', a=0.5)
    graph.hist(data_ravenclaw[0], '', c='blue', a=0.5)
    graph.hist(data_slytherin[0], '', c='green', a=0.5)

    plt.legend(['Grynffindor', 'Hufflepuff', 'Ravenclaw', 'Slytherin'])

    graph.show()