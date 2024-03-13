# here we'll put all the models that we'll use for the project
import os
#list of library needed
from tensorflow import keras
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, LSTM, Dense
from tensorflow.keras import optimizers
from tensorflow.keras.callbacks import EarlyStopping

# model to label a new input we'll use rnn 

def rnn_model(input_dim, embedding_dim, input_length):
    ''' input_dim = vocab_size 
        output_dim = embedding_dim
        input_length = max_len
    '''
    model = Sequential()
    model.add(Embedding(input_dim=input_dim, embedding_dim = embedding_dim, input_length=input_length))
    model.add(LSTM(64))
    model.add(Dense(300, activation='relu', input_dim=vocab_size))
    model.add(Dense(150, activation='relu',))
    model.add(Dense(120, activation='relu',))
    model.add(Dense(120, activation='relu',))
    model.add(Dense(num_classes, activation='softmax'))
    
    print("✅ Model initialized")
    return model

# let's compile the model

def compile_model(model, learning_rate = 0.001, loss = 'categorical_crossentropy', metrics = 'accuracy'):
    optimizer = optimizers.Adam(learning_rate=learning_rate)
    model.compile(
        optimizer=optimizer,
        loss= loss,
        metrics = metrics)
    
    print("✅ Model compiled")
    return model

# let's train the model

def train_model(model, X_train, y_train, validation_data=None, validation_split = 0.25, batch_size = 32, epochs = 20, verbose = 0, patience = 5):
    
    es = EarlyStopping(
        monitor="accuracy",
        patience=patience,
        restore_best_weights=True,
        verbose= verbose
    )
    
    history = model.fit(
        X_train, y_train,
        validation_data=validation_data,
        validation_split = validation_split,
        batch_size=batch_size,
        epochs=epochs,
        callbacks=[es]
        verbose = verbose
    )
    
    print(f"✅ Model trained with {epochs} epochs")
    
    save_dir = '../model_registry'
    model_filename = 'my_model.h5'
    model_path = os.path.join(save_dir, model_filename)
    model.save(model_path)
    

    return model, history

# let's evaluate the model

def evaluate_model(model, X_test, y_test):
    score = model.evaluate(X_test, y_test, verbose=0)
    print(f"✅ Model evaluated with {score[1]} accuracy")
    if score > 'x':
        save_dir = 'model_registry'
        model_filename = 'my_model.h5'
        model_path = os.path.join(save_dir, model_filename)
        model.save(model_path)
    return score

