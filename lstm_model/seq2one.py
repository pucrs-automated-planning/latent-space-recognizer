# coding: utf-8
from utils import *
from copy import deepcopy
from keras.utils import to_categorical
from keras.preprocessing.text import one_hot


x_dict = dict()
y_dict = dict()

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


def generate_x_dict(vocab):
    global x_dict    

    for i, word in enumerate(vocab, 1):
        x_dict[word] = i


def generate_y_dict(y):
    global x_dict
    global y_dict

    y_dict = deepcopy(x_dict)

    set_y = set(y)

    for i, word in enumerate(set_y, 1):
        if word not in y_dict:
            y_dict[word] = i


def preprocess_data(data, key):
    global x_dict
    global y_dict

    new_x, new_y = [], []

    # Convert data to the proper input of lstm.
    x, y = data

    # Check how many different state exist.
    vocab = list(set([st_i for seq_st in x for st_i in seq_st]))
    generate_x_dict(vocab)    
    
    # Get the biggest sequence of states.
    max_len = len(max(x, key=len))
    
    for seq_st in x:
        new_seq_st = []

        for st in seq_st:
            new_seq_st.append(x_dict[st])

        if len(new_seq_st) < max_len:
            # Zero padding.
            new_seq_st = new_seq_st + ((max_len - len(new_seq_st)) * [0])

        new_x.append(new_seq_st)

    generate_y_dict(y)

    for y_i in y:
        new_y.append(y_dict[y_i])
    
    for j in range(len(new_x)):
    
        print(new_x[j], new_y[j])
#    sys.exit(1)


if __name__ == "__main__":

    data_dict = read_data()

    print("Dictionary ready, checking keys: {}".format(data_dict.keys()))

    for key in data_dict:
        print(key)
        preprocess_data(data_dict[key], key)
        sys.exit(0)
