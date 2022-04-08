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


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Wrong number of arguments!\nUsage:\tpython3 describe.py [PATH OF CSV]', file=sys.stderr)
        exit(1)

    dataset = CSV.open(sys.argv[1])
    np_min = np.array([Stat.min(data['data']) for data in dataset[Entries.Arithmancy.value:]])
    np_max = np.array([Stat.max(data['data']) for data in dataset[Entries.Arithmancy.value:]])

    for i, d in enumerate(dataset):
        if d['name'] == 'Hogwarts House':
            for j, house in enumerate(d['data']):
                if house == House.Gryffindor.name:
                    dataset[i]['data'][j] = House.Gryffindor.value
                elif house == House.Slytherin.name:
                    dataset[i]['data'][j] = House.Slytherin.value
                elif house == House.Ravenclaw.name:
                    dataset[i]['data'][j] = House.Ravenclaw.value
                elif house == House.Hufflepuff.name:
                    dataset[i]['data'][j] = House.Hufflepuff.value
        elif Math.isfloat(d['data'][0]) and d['name'] != 'Index':
            dataset[i]['data'] = Algorithm.normalize(d['data'])         


    X = np.array([data['data'] for data in dataset[Entries.Arithmancy.value:]]).T
    for i in range(13):
        X[: , i] = np.nan_to_num(X[: , i], Stat.mean(X[:, i]))

    y = np.array([int(house) for house in dataset[Entries.Hogwarts_House.value]['data']])
    theta = Algorithm.one_for_all(X, y, 4, 0.8, 500, 900, 500)
    
    with open('theta.npy', 'wb') as file:
        np.save(file, np_min)
        np.save(file, np_max)
        for W, b in theta:
            np.save(file, W)
            np.save(file, b)

    # with open('theta.npy', 'rb') as file:
    #     mn = np.load(file)
    #     mx = np.load(file)
    #     print(f'mn = {mn}\nmx = {mx}')
    #     for i in range(4):
    #         W = np.load(file)
    #         b = np.load(file)
    #         print(f'W = {W}')
    #         print(f'b = {b}')
    #         print('-------------------------')

