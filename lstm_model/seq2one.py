# coding: utf-8
import os
import sys
import random
import pickle
import argparse
import numpy as np
from utils import *
from keras.utils import to_categorical
from keras.preprocessing.text import one_hot
from keras.models import Sequential, load_model
from sklearn.model_selection import train_test_split
from keras.callbacks import EarlyStopping, ModelCheckpoint
from keras.layers import Embedding, LSTM, Dense, Activation

random.seed(12)


# Set the gpu to use.
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
    return model


def read_data(data_path):

    # Get files from path.
    files = os.listdir(data_path)

    # Set a dictionary to save data divided by domain.
    data_dict = dict()

    for file in files:
        # For each file, read data and create a structure (X, Y) for it.
        print("Extracting data from: %s" % file) # TODO: Change print to log.

        # Dictionary keys are domain names.
        filename, _ = os.path.splitext(file)

        # Get correct path to file.
        file_path = os.path.join(data_path, file)
            
        # Create structure.
        data_dict[filename] = read_dataset(file_path)

    return data_dict

# TODO: Save dictionaries for both x and y in order to represent data after training.
def generate_x_dict(x_dict, vocab):
    # Generate a numeric representation for states.
    for i, word in enumerate(vocab, 1):
        x_dict[word] = i


def save_obj(obj, domain, obj_type):
    # Save dictionary made to the specific domain.
    output_path = os.path.join(SAVE_MODELS_PATH, domain + "_"+obj_type+".pkl")
    pickle.dump(obj, open(output_path, 'w'))


def preprocess_data(data, key):
    
    x_dict = dict()
    # y_dict = dict()

    new_x, new_y = [], []

    # Convert data to the proper input of lstm.
    x, y = data

    # Check how many different state exist.
    vocab = list(set([st_i for seq_st in x for st_i in seq_st]))
    generate_x_dict(x_dict, vocab)
    save_obj(x_dict, key, 'dict')
    
    # Get the biggest sequence of states.
    max_len = len(max(x, key=len))
    save_obj(max_len, key, 'max_len')

    for seq_st in x:
        new_seq_st = []

        for st in seq_st:
            new_seq_st.append(x_dict[st])

        if len(new_seq_st) < max_len:
            # Zero padding.
            new_seq_st = new_seq_st + ((max_len - len(new_seq_st)) * [0])

        new_x.append(new_seq_st)

    X_train, X_test, y_train, y_test = train_test_split(new_x, y, test_size=0.2, random_state=42)

    return X_train, X_test, y_train, y_test, len(vocab), max_len


def train_model(model, x, y, save_path):

    # Callbacks for training.
    model_check = ModelCheckpoint(save_path, monitor='val_loss', verbose=1, save_best_only=True, save_weights_only=False, mode='auto', period=1)
    early = EarlyStopping(monitor='val_loss', min_delta=0, patience=2, verbose=1, mode='auto')

    model.fit(x=np.array(x), y=np.array(y), epochs=100000, batch_size=2, verbose=1, callbacks=[model_check, early], validation_split=0.1, steps_per_epoch=None)


def evaluate_model(model, x, y, saved_model):
    # Measure accuracy given a model.
    eval_model = load_model(saved_model) # Load the best model to test.
    loss, acc = eval_model.evaluate(x=np.array(x), y=np.array(y), batch_size=2, verbose=1)

    print('Test loss / test accuracy = {:.4f} / {:.4f}'.format(loss, acc))


def hamming_sum(s0, s1):                                                                                       
    if len(s0) != len(s1):
        raise ValueError()
    return sum(c0 != c1 for (c0, c1) in zip(s0, s1))


def test_model(saved_model, dict_path, len_path, data_path):
    # TODO: Save the output to a file.
    model = load_model(saved_model)
    x_dict = pickle.load(open(dict_path, 'r'))
    max_len = pickle.load(open(len_path, 'r'))

    X, y = read_dataset(data_path)

    for ind, states in enumerate(X):
        seq = np.zeros((max_len))
        for i, state in enumerate(states):
            if i >= max_len:
                continue
            seq[i] = x_dict.get(state, -1)
        pred = np.round(model.predict(seq.reshape(1, max_len), verbose=1))
        print(pred)
        print("Hamming Distance: %d" % hamming_sum(y[ind], pred[0].tolist()))


def train(data_path):

    data_dict = read_data(data_path)

    print("Dictionary ready, checking keys: {}".format(data_dict.keys()))

    for key in data_dict:
        print("Processing domain: %s" % key)
        print("This domain has %d samples and - distinct classes." % len(data_dict[key][0]))#, len(set(data_dict[key][1]))))
        X_train, X_test, y_train, y_test, vocab, max_len = preprocess_data(data_dict[key], key)
        model = seq2one_model(vocab, max_len)

        save_model_path = os.path.join(SAVE_MODELS_PATH, key + '_model.h5') # Set the path to save the best model.

        train_model(model, X_train, y_train, save_model_path)
        evaluate_model(model, X_test, y_test, save_model_path)

if __name__ == "__main__":
    
    parser = argparse.ArgumentParser(description="Train/Test LSTM to recognize goals given observations.")
    parser.add_argument('action', metavar='mode', type=str, help="Either 'train' or 'test'")
    parser.add_argument('data_path', metavar='data', type=str, help="Path to file containing training or testing samples.")
    parser.add_argument('--model_path', help="Path to a .h5 saved model.")
    parser.add_argument('--model_dict', help="Path to the model corresponding dict. It has a name like this: <domain_name>_dict.pkl")
    parser.add_argument('--model_max_len', help="Path to the model corresponding max number of state sequences. It has a name like this: <domain_name>_max_len.pkl")

    args = parser.parse_args()

    if not os.path.exists(args.data_path):           
        print("Please! Provide a valid data path.")

    if args.action == 'train':

        train(args.data_path)

    elif args.action == 'test':

        if os.path.exists(args.model_path):

            if os.path.exists(args.model_dict):

                if os.path.exists(args.model_max_len):

                    test_model(args.model_path, args.model_dict, args.model_max_len, args.data_path)
                else:
                    print("File for model max len doesn't exist.")
            else:
                print("File for model dict doesn't exist.")
        else:
            print("File for model path doesn't exist.")
    else:
        print("Please! Inform if you want to either train or test LSTM.")

    # [1 0 1 0 1 1 1 1 0 1 1 0 1 0 1 1 1 1 0 1 0 0 1 0 1 1 1 1 0 1 0 1 0 0 0 1]
    # [0, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 0, 0, 0]