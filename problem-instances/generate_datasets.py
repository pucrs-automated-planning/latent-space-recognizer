#!/usr/bin/env python3
import os
import sys
import argparse
import numpy as np
import importlib
from scipy import misc
from itertools import permutations, product
sys.path.append('../')


def get_mnist(p, dataset_name):
    numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    height = 3
    width = 3
    perm = permutations(numbers, width * height)

    puzzles = []

    for num_order in perm:
        puzzles.append(list(num_order))#np.array(list(num_order)).reshape((1,3*3)))
        
    g = p.generate(np.array(puzzles), height=height, width=width)

    for i in range(g.shape[0]):
        puzzle_name = [0]*len(numbers)
        for k, j in enumerate(puzzles[i]):
            puzzle_name[j] = k

        puzzle_name = ''.join(map(str, puzzle_name))
        puzzle_path = os.path.join(dataset_name, '%s.jpg' % puzzle_name)
        misc.imsave(puzzle_path, g[i])


def get_lightsout(p, dataset_name, instances):        
    size = 4
    steps = 5
    numbers = [-1, 1]
    prod = product(numbers, repeat=size*size)

    puzzles = []

    for num_order in prod:
        puzzles.append(list(num_order))#np.array(list(num_order)).reshape((1,3*3)))
        
    g = p.generate(np.array(puzzles))

    for i in range(g.shape[0]):
        puzzle_name = ''.join(map(str, puzzles[i]))
        puzzle_path = os.path.join(dataset_name, '%s.jpg' % puzzle_name.replace('-1', '0'))
        misc.imsave(puzzle_path, g[i])


if __name__ == '__main__':
        
    parser = argparse.ArgumentParser()
    parser.add_argument('dataset', help="Dataset name (valid one, please).")
    parser.add_argument('--type', help="Lightsout type (digital or twisted).")
    parser.add_argument('--instances', help="Number of instances to generate.",
        type=int)
    args = parser.parse_args()

    dataset_name = args.dataset
    
    # Set the number of samples.
    if not os.path.isdir(dataset_name):
        os.makedirs(dataset_name)

    if dataset_name == 'mnist':
        p = importlib.import_module('latplan.puzzles.puzzle_{}'.format(
            dataset_name))
        p.setup()
        get_mnist(p, dataset_name)

    elif dataset_name == 'hanoi':
        pass #get_hanoi(p)

    elif dataset_name == 'lightsout':
        p = importlib.import_module('latplan.puzzles.{}_{}'.format(
            dataset_name, args.type))
        p.setup()
        if not args.instances:
            print("You must pass instances as argument.")
            sys.exit(1)

        get_lightsout(p, dataset_name, args.instances)
