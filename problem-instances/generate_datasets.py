#!/usr/bin/env python3
import os
import sys
import argparse
import numpy as np
import importlib
from scipy import misc
from itertools import permutations
sys.path.append('../')

if __name__ == '__main__':
        
    parser = argparse.ArgumentParser()
    parser.add_argument('dataset', help="Dataset name (valid one, please).")
    args = parser.parse_args()

    dataset_name = args.dataset
    p = importlib.import_module('latplan.puzzles.puzzle_{}'.format(dataset_name))
    p.setup()
    
    # Set the number of samples.
    if not os.path.isdir(dataset_name):
        os.makedirs(dataset_name)

    if dataset_name == 'mnist':
        numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        height = 3
        width = 3
        perm = permutations(numbers, width * height)

        puzzles = []

        for num_order in perm:
            puzzles.append(list(num_order))#np.array(list(num_order)).reshape((1,3*3)))
            
        g = p.generate(np.array(puzzles), height=height, width=width)

        for i, matrx in g:
            puzzle_name = ''.join(map(str, puzzles[i]))
            puzzle_path = os.path.join(dataset_name, '%s.jpg' % puzzle_name)
            misc.imsave(puzzle_path, matrx)