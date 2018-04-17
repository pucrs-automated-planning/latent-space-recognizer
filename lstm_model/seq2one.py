# coding: utf-8
import random
from utils import *
from copy import deepcopy
from keras.layers import Embedding, LSTM, Dense, Activation
from keras.models import Sequential, load_model
from keras.utils import to_categorical
from keras.callbacks import EarlyStopping
from keras.callbacks import ModelCheckpoint
from keras.preprocessing.text import one_hot
from sklearn.model_selection import train_test_split

random.seed(12)


def _start(gpu):
    import os
    import tensorflow as tf

    os.environ["CUDA_DEVICE_ORDER"]="PCI_BUS_ID"   # see issue #152
    os.environ["CUDA_VISIBLE_DEVICES"]=str(gpu)
    config = tf.ConfigProto()
    config.gpu_options.allow_growth=True
    sess = tf.Session(config=config)
    
    return 'Done!'

_start(0) 


def seq2one_model(vocab, max_len):
    
    model = Sequential()

    # Creating encoder network
    model.add(Embedding(vocab, 1000, input_length=max_len, mask_zero=True))
    model.add(LSTM(512))
    model.add(Dense(ST_SIZE))
    model.add(Activation('sigmoid'))
    model.compile(loss='binary_crossentropy',
            optimizer='rmsprop',
            metrics=['accuracy'])
    print model.summary()
    return model


def read_data():

    # Get files from path.
    files = os.listdir(DATA_PATH)

    # Set a dictionary to save data divided by domain.
    data_dict = dict()

    for file in files:
        # For each file, read data and create a structure (X, Y) for it.
        print("Extracting data from: %s" % file) # TODO: Change print to log.

        # Dictionary keys are domain names.
        filename, _ = os.path.splitext(file)

        # Get correct path to file.
        file_path = os.path.join(DATA_PATH, file)
            
        # Create structure.
        data_dict[filename] = read_dataset(file_path)

    return data_dict

# TODO: Save dictionaries for both x and y in order to represent data after training.
def generate_x_dict(x_dict, vocab):
    # Generate a numeric representation for states.
    for i, word in enumerate(vocab, 1):
        x_dict[word] = i


# def generate_y_dict(y_dict, y):
#     # Generate a numeric representation for classes.
#     set_y = set(y)

#     for i, word in enumerate(set_y):
#         if word not in y_dict:
#             y_dict[word] = i


def preprocess_data(data, key):
    
    x_dict = dict()
    # y_dict = dict()

    new_x, new_y = [], []

    # Convert data to the proper input of lstm.
    x, y = data

    # Check how many different state exist.
    vocab = list(set([st_i for seq_st in x for st_i in seq_st]))
    generate_x_dict(x_dict, vocab)
    
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

    # Generate a dict for representing y states.
    # generate_y_dict(y_dict, y)

    # for y_i in y:
    #     # Convert each state into its new representation.
    #     new_y.append(y_dict[y_i])

    # Turn everything one hot encoding for softmax classification.
    # new_y = to_categorical(new_y, num_classes=len(set(new_y)))

    X_train, X_test, y_train, y_test = train_test_split(new_x, y, test_size=0.2, random_state=42)

    return X_train, X_test, y_train, y_test, len(vocab), max_len


def train_model(model, x, y, save_path):

    # Callbacks for training.
    model_check = ModelCheckpoint(save_path, monitor='val_loss', verbose=1, save_best_only=True, save_weights_only=False, mode='auto', period=1)
    early = EarlyStopping(monitor='val_loss', min_delta=0, patience=2, verbose=1, mode='auto')

    model.fit(x=x, y=y, epochs=100000, batch_size=2, verbose=1, callbacks=[model_check, early], validation_split=0.1, steps_per_epoch=None)


def test_model(model, x, y, saved_model):

    test_model = load_model(saved_model) # Load the best model to test.
    loss, acc = test_model.evaluate(x=x, y=y, batch_size=2, verbose=1)

    print('Test loss / test accuracy = {:.4f} / {:.4f}'.format(loss, acc))

if __name__ == "__main__":

    batch_size = 1
    data_dict = read_data()

    print("Dictionary ready, checking keys: {}".format(data_dict.keys()))

    for key in data_dict:
        print("Processing domain: %s" % key)
        print("This domain has %d samples and - distinct classes." % len(data_dict[key][0]))#, len(set(data_dict[key][1]))))
        X_train, X_test, y_train, y_test, vocab, max_len = preprocess_data(data_dict[key], key)
        model = seq2one_model(vocab, max_len)

        save_model_path = 'models/' + key + '_model.h5' # Set the path to save the best model.

        train_model(model, X_train, y_train, save_model_path)
        test_model(model, X_test, y_test, save_model_path)