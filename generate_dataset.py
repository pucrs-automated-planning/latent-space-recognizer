#!/usr/bin/env python3
import os
import sys
import argparse
import numpy as np
import importlib
from scipy import misc
from itertools import permutations
import time
sys.path.append('../../')

if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('dataset', help="Dataset name (valid one, please).")
    args = parser.parse_args()

    dataset_name = args.dataset
    dataset_name = 'mnist'
    p = importlib.import_module('latplan.puzzles.puzzle_{}'.format(dataset_name))
    p.setup()

    dataset_name = 'mnist-test'
    # Set the number of samples.
    if not os.path.isdir(dataset_name):
        os.makedirs(dataset_name)


    if dataset_name == 'mnist-test':
        numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        height = 3
        width = 3
        perm = permutations(numbers, width * height)

        puzzles = []

        for num_order in perm:
            puzzles.append(list(num_order))#np.array(list(num_order)).reshape((1,3*3)))
        
        model = p.generate_model_leo(np.array(puzzles[0]).reshape(1,3*3), height=height, width=width)
        print(len(puzzles))

        for i, puzzle in enumerate(puzzles):
            #print('Iter:', i, puzzle)
            puzzle = [1,2,3,7,0,8,5,4,6]
            curr = time.time()
            if dataset_name == 'mnist-test':
                print(np.array(puzzle).reshape(1,3*3))
            g = model.predict(np.array(puzzle).reshape(1,3*3))
            #print(time.time() - curr)
            puzzle_name = ''.join(map(str, puzzle))
            puzzle_path = os.path.join(dataset_name, '%s.jpg' % puzzle_name)
            misc.imsave(puzzle_path, g[0])
            if dataset_name == 'mnist-test':
                break
            