# coding: utf-8
import os
import sys

#Constants.
DATA_PATH = '../lstm_dataset'
ST_SIZE = 36 # Set the flatten state length.
SAVE_MODELS_PATH = 'models'

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
            if not len(st):
                continue

            assert (len(st))
            states.append(st)
            
        # Process class.
        y = eval(y)#''.join(y.strip('[]\n').split(', '))

        X.append(states[:-1]) # Removing the last state because it is the proper goal.
        Y.append(y)

    return X, Y

if __name__ == "__main__":

    example = os.path.join(DATA_PATH, 'hanoi.csv')

    x, y = read_dataset(example)
    print(x[0])
    print(y[0])
