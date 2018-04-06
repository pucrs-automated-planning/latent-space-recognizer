# coding: utf-8
import os
import sys

#Constants.
DATA_PATH = '../lstm_dataset'
ST_SIZE = 36 # Set the flatten state length.


def read_dataset(file_path):
    # Read and structure data for training.

    X, Y = [], []

    lines = open(file_path, 'r').readlines()

    for line in lines:

        states = []

        # Divide inputs and output.
        x, y = line.split("@")
        # print("X: %s\nY: %s" % (x, y))
        inputs = x.split(";")

        for inp in inputs:
            # Process inputs.
            st = ''.join(inp.strip('[]').split(', '))
            assert (len(st))
            states.append(st)
            
        # Process class.
        y = ''.join(y.strip('[]\n').split(', '))

        X.append(states)
        Y.append(y)

    return X, Y

if __name__ == "__main__":

    example = os.path.join(DATA_PATH, 'hanoi.csv')

    x, y = read_dataset(example)
    print(x[0])
    print(y[0])