# here we'll list all encoders we'll use prior training the data and for decoding I guess

# list of library to import
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from keras.utils import to_categorical
from sklearn.model_selection import train_test_split



# need to tokenize the new input

def tokenizer(text, max_len = 160):
    ''' text = list of strings   '''
    tokenizer = Tokenizer()
    tokenizer.fit_on_texts(text)
    sequences = tokenizer.texts_to_sequences(text)
    text_padded = pad_sequences(sequences, maxlen=max_len)
    vocab_size = len(tokenizer.word_index) + 1
    
    print("✅ Tokenizer initialized")
    return tokenizer, text_padded, vocab_size

# need to hot encode the labels of our y

def hot_encode(y, num_classes = None):
    ''' y = list of labels
        num_classes = number of classes
    '''
    num_classes = y.nunique()
    label_to_index = {label: idx for idx, label in enumerate(sorted(set(y)))}
    y_numerical = [label_to_index[label] for label in y]

    # One-hot encode the numerical labels
    num_classes = len(label_to_index)
    y_one_hot = to_categorical(y_numerical, num_classes)
    
    print("✅ Labels hot encoded")
    return y_one_hot, y_numerical

# let's split the data into training and testing sets

def split_data(text_padded, y_one_hot, test_size = 0.25, random_state = 42):
    ''' text_padded = padded text '''
    X_train, X_test, y_train, y_test = train_test_split(text_padded, y_one_hot, test_size=test_size, random_state=random_state)
    
    print("✅ Data splitted")
    return X_train, X_test, y_train, y_test