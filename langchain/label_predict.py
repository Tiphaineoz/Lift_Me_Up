# import libraries
import tensorflow as tf
import numpy as np
import pickle
import json
from tensorflow.keras.preprocessing.sequence import pad_sequences
from keras.utils import to_categorical
from tensorflow.keras.models import load_model
#from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing import sequence

# import from within the code
from model_registry import *

# need to tokenize the new input
def tokenizer_padding(input, max_len = 160):
    tokenizer_path = 'model_registry/tokenizer.pickle'
    with open(tokenizer_path, 'rb') as handle:
        tokenizer = pickle.load(handle)
    input_token = tokenizer.texts_to_sequences([input])
    input_pad = pad_sequences(input_token, maxlen=max_len)
    return input_pad

def predict_label(input):
    new_input_pad = tokenizer_padding(input)
    model_path = 'model_registry/rnn_saved_model.h5'
    model = load_model(model_path)
    predicted_probabilities = model.predict(new_input_pad)
    # Convert the predicted probabilities to class labels
    predicted_labels_numerical = np.argmax(predicted_probabilities, axis=1)
    # Convert numerical labels back to string labels
    json_path = 'model_registry/feeling_labels.json'
    with open(json_path, 'r') as f:
        label_list = json.load(f)
    predicted_labels = [label_list[str(idx)] for idx in predicted_labels_numerical]
    return predicted_labels[0]

