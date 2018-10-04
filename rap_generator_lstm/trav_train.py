import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Dropout, LSTM
from keras.callbacks import ModelCheckpoint
from keras.utils import np_utils

filename = "lyrics.txt"
raw_text = open(filename).read()
raw_text = raw_text.lower()

chars = sorted(list(set(raw_text)))
char_to_int = dict((c,i) for i,c in enumerate(chars))

#print(chars)
#print(char_to_int)

n_chars = len(raw_text)
n_vocab = len(chars)

print("Total Characters: ", n_chars)
print("Total Vocab: ", n_vocab)

seq_length = 8
dataX = []
dataY = []
for i in range(0, n_chars - seq_length, 1):
        seq_in = raw_text[i:i + seq_length]
        seq_out = raw_text[i+seq_length]
        dataX.append([char_to_int[char] for char in seq_in])
        dataY.append([char_to_int[seq_out]])
n_patterns = len(dataX)
print("Total Patterns: ", n_patterns)

X = np.reshape(dataX, (n_patterns, seq_length, 1))

X = X / float(n_vocab)
y = np_utils.to_categorical(dataY)

model = Sequential()
model.add(LSTM(256, input_shape=(X.shape[1],X.shape[2]), return_sequences=True))
model.add(Dropout(0.2))
model.add(LSTM(256))
model.add(Dropout(0.2))
model.add(Dense(y.shape[1],activation='softmax'))
model.compile(loss='categorical_crossentropy', optimizer='adam')

filepath = "weights-improvement-{epoch:02d}--{loss:.4f}-bigger.hdf5"
checkpoint = ModelCheckpoint(filepath, monitor="loss", verbose=1, save_best_only=True, mode="min")
callbacks_list = [checkpoint]

model.fit(X, y, epochs=50, batch_size=64, callbacks=callbacks_list)