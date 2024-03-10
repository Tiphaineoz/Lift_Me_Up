# that's where we'll put everything together 
# ie: do the final preprocessing / train / eval / predict

from ml_logic.models import rnn_model, compile_model, train_model
from ml_logic.encoders import tokenizer, hot_encode, split_data
from tensorflow.keras.preprocessing.sequence import pad_sequences
from base_data.psychology_dataset import labeled_df

text = labeled_df['question']
y = labeled_df['Result']

def train_model_input(text, y, max_len = 160, learning_rate = 0.001, loss = 'categorical_crossentropy', metrics = 'accuracy', validation_split = 0.25, batch_size = 32, epochs = 20, verbose = 0, patience = 5, test_size = 0.25, random_state = 42):
    ''' text = list of strings
        y = list of labels
    '''
    tokenizer, text_padded, vocab_size = tokenizer(text, max_len = max_len)
    y_one_hot, y_numerical = hot_encode(y)
    X_train, X_test, y_train, y_test = split_data(text_padded, y_one_hot, test_size = test_size, random_state = random_state)
    
    model = rnn_model(input_dim = vocab_size, embedding_dim = 300, input_length = max_len)
    model = compile_model(model, learning_rate = learning_rate, loss = loss, metrics = metrics)
    model, history = train_model(model, X_train, y_train, validation_data=(X_test, y_test), validation_split = validation_split, batch_size = batch_size, epochs = epochs, verbose = verbose, patience = patience)
    
    return model, history, tokenizer, vocab_size, max_len, y_numerical

def predict_input_label(model, tokenizer, new_text, y_numerical, max_len = 160):
    ''' model = trained model
        tokenizer = tokenizer
        text = list of strings
    '''
    sequences = tokenizer.texts_to_sequences(new_text)
    text_padded = pad_sequences(sequences, maxlen=max_len)
    y_pred = model.predict(text_padded)
    predicted_labels_numerical = np.argmax(y_pred, axis=1)
    predicted_labels = [y_numerical[idx] for idx in predicted_labels_numerical]
    
    print("✅ Predicted label! First one is:", predicted_labels[0])
    
    return predicted_labels

