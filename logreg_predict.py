"""This is a training program of logistic regression"""


import os, sys


"""Add packages dir on pythonpath"""
fpath = os.path.join(os.path.dirname(__file__), 'LibAI')
sys.path.append(fpath)


import numpy as np

from enum import Enum
from LibAI.libalgorithm import Algorithm
from LibAI.libparser import CSV
from LibAI.libmath import Math, Stat


class Entries(Enum):
    Index = 0
    Hogwarts_House = 1
    First_Name = 2
    Last_Name = 3
    Birthday = 4
    Best_Hand = 5
    Arithmancy = 6
    Astronomy = 7
    Herbology = 8
    Defense_Against_the_Dark_Arts = 9
    Divination = 10
    Muggle = 11
    Studies = 12
    Ancient_Runes = 13
    History_of_Magic = 14
    Transfiguration = 15
    Potions = 16
    Care_of_Magical_Creatures = 17
    Charms = 18
    Flying = 19


class House(Enum):
    Gryffindor = 0
    Slytherin = 1
    Ravenclaw = 2
    Hufflepuff = 3

def normalize(dataset, mn, mx):
    ret = []
    for data in dataset:
        ret.append((data - mn) / (mx - mn))
    return ret

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Wrong number of arguments!\nUsage:\tpython3 describe.py [PATH OF CSV] [PATH OF THETA FILE]', file=sys.stderr)
        exit(1)

    mx = []
    mn = []
    theta = []
    dataset = CSV.open(sys.argv[1])

    with open(sys.argv[2], 'rb') as file:
        mn = np.load(file)
        mx = np.load(file)
        for i in range(4):
            W = np.load(file)
            b = np.load(file)
            theta.append((W, b))
    
    for i, d in enumerate(dataset):
        if Math.isfloat(d['data'][0]) and d['name'] != 'Index' and d['name'] != 'Hogwarts House':
            dataset[i]['data'] = normalize(d['data'], mn[i - 6], mx[i - 6])

    # print(dataset)

    X = np.array([data['data'] for data in dataset[Entries.Arithmancy.value:]]).T
    for i in range(13):
        X[: , i] = np.nan_to_num(X[: , i], Stat.mean(X[:, i]))

    y = Algorithm.predict_one_for_all(X, theta, 4)
    with open('house.csv', 'w') as file:
        file.writelines('Index,Hogwarts House\n')
        for i, data in enumerate(y):
            house = ''
            if data == House.Gryffindor.value:
                house = House.Gryffindor.name
            elif data == House.Slytherin.value:
                house = House.Slytherin.name
            elif data == House.Ravenclaw.value:
                house = House.Ravenclaw.name
            elif data == House.Hufflepuff.value:
                house = House.Hufflepuff.name
            file.writelines(f'{i},{house}\n')
