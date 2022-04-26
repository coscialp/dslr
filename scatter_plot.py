#!/usr/bin/env python
# -*- coding: UTF8 -*-
"""This is a program will print the scatter plot"""


import os, sys


"""Add packages dir on pythonpath"""
fpath = os.path.join(os.path.dirname(__file__), 'LibAI')
sys.path.append(fpath)


from matplotlib import pyplot as plt
from LibAI.libgraphics import Graphics
from LibAI.libparser import CSV


if __name__ == '__main__':
    if len(sys.argv) != 2 and len(sys.argv) != 4:
        print('Wrong number of arguments!\nUsage:\tpython3 describe.py [PATH OF CSV] [NAME OF X AXIS] [NAME OF Y AXIS]', file=sys.stderr)
        exit(1)

    if len(sys.argv) == 2:
        column = ['Astronomy', 'Defense Against the Dark Arts']
    else:
        column = sys.argv[2:]

    dataset = CSV.open(sys.argv[1])


    try:
        data_gryffindor = CSV.filter(dataset, column, where='Hogwarts House', filters=['Gryffindor'])
        data_slytherin = CSV.filter(dataset, column, where='Hogwarts House', filters=['Slytherin'])
        data_ravenclaw = CSV.filter(dataset, column, where='Hogwarts House', filters=['Ravenclaw'])
        data_hufflepuff = CSV.filter(dataset, column, where='Hogwarts House', filters=['Hufflepuff'])

        graph = Graphics()
    
        graph.plot(data_ravenclaw[0], data_ravenclaw[1], character='.')
        graph.plot(data_hufflepuff[0], data_hufflepuff[1], character='.')
        graph.plot(data_slytherin[0], data_slytherin[1], character='.')
        graph.plot(data_gryffindor[0], data_gryffindor[1], character='.')

        plt.legend(['Ravenclaw', 'Hufflepuff', 'Slytherin', 'Grynffindor'])

        graph.show()
    except IndexError:
        print('Error: This entry does not exist.')