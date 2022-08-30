from keras.models import Sequential
from keras.laeyrs import Dense, Dropout, LSTM, Embedding
from keras.callbacks import EarlyStopping, ModelCheckpoint
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from keras import optimizers

# optimizers.SGD()
# optimizers.RMSProp()
# optimizers.Adagrad()
# optimizers.Adadelta()
# optimizers.Adam()

vocabulary_size = 7500
pad_length = 1000
tokenizer = Tokenizer(num_words=vocabulary_size)
tokenizer.fit_on_texts(X)
sequences = tokenizer.texts_to_sequences(X)
padded_sequences = pad_sequences(sequences, maxlen=pad_length)

es = EarlyStopping(monitor="loss", mode="min", verbose=1)
filepath = "model.h5"
ckpt = ModelCheckpoint(
    filepath, monitor="loss", verbose=1, save_best_only=True, mode="min"
)


def build_network():
    model = Sequential()
    model.add(Embedding(vocabulary_size, 1024, input_length=pad_length))
    model.add(LSTM(1024, dropout=0.2, recurrent_dropout=0.2))
    model.add(Dense(160, input_dim=40, activation="relu"))
    model.add(Dropout(0.2))
    model.add(Dense(320, activation="relu"))
    model.add(Dropout(0.2))
    model.add(Dense(365, activation="relu"))
    model.add(Dropout(0.2))
    model.add(Dense(125, activation="relu"))
    model.add(Dropout(0.2))
    model.add(Dense(25, activation="relu"))
    model.add(Dropout(0.2))
    model.add(Dense(1, activation="sigmoid"))
    model.compile(loss="binary_crossentropy", optimizer="adam", metrics=["accuracy"])
    model.summary()
    return model


model = build_network()

model.fit(
    scaled_data, train_label[0], validation_split=0.3, epochs=25, callbacks=[es, ckpt]
)


from keras.models import load_model

new_model = load_model("model.h5")
