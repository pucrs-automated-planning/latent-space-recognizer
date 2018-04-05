# coding: utf-8
import os

#Constants.
DATA_PATH = '../lstm_dataset'


def read_dataset(data_path):
    # Read and structure data for training.
    files = os.listdir(data_path)

    X, Y = [], []

    for file in files:
        print("Extracting data from: %s" % file) # TODO: Change print to log.

        # Get correct path to file.
        file_path = os.path.join(data_path, file)
        print("File path: %s" % file_path)

        # Extract file lines.
        lines = open(file_path, 'r').readlines()

        for line in lines:
            # Divide inputs and output.
            x, y = line.split("@")
            print("X: %s\nY: %s" % (x, y))
            inputs = x.split(";")


if __name__ == "__main__":

    read_dataset(DATA_PATH)
