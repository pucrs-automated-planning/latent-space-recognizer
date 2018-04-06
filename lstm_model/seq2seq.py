# coding: utf-8
from utils import *
from keras.utils import to_categorical
from keras.preprocessing.text import one_hot


def seq2one_model():
    pass


def read_data():

    # Get files from path.
    files = os.listdir(DATA_PATH)

    # Set a dictionary to save data divided by domain.
    data_dict = dict()

    for file in files:
        # For each file, read data and create a structure (X, Y) for it.
        print("Extracting data from: %s" % file) # TODO: Change print to log.

        # Dictionary keys are the domain names.
        filename, _ = os.path.splitext(file)

        # Get correct path to file.
        file_path = os.path.join(DATA_PATH, file)
            
        # Create structure.
        data_dict[filename] = read_dataset(file_path)

    return data_dict


def preprocess_data(data, key):

    new_x, new_y = [], []

    # Convert data to the proper input of lstm.
    x, y = data
    print(x[0])

    # Check how many different state exist.
    vocab = list(set([st_i for seq_st in x for st_i in seq_st]))
    
    # Get the biggest sequence of states.
    max_len = max(x, key=len)
    
    for seq_st in x:
        new_seq_st = []

        for st in seq_st:

            new_seq_st.append(one_hot(st, len(vocab)))

        new_x.append(new_seq_st)

    for y_i in y:
        new_y.append(one_hot(y_i, len(y)))

    print(new_x[0], new_y[0])
    sys.exit(1)


if __name__ == "__main__":

    data_dict = read_data()

    print("Dictionary ready, checking keys: {}".format(data_dict.keys()))

    for key in data_dict:

        preprocess_data(data_dict[key], key)
