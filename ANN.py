from keras.models import Sequential
from keras.layers import Dense, Dropout
from keras.callbacks import EarlyStopping, ModelCheckpoint
from keras import optimizers
# optimizers.SGD()
# optimizers.RMSProp()
# optimizers.Adagrad()
# optimizers.Adadelta()
# optimizers.Adam()

es = EarlyStopping(monitor='loss', mode='min', verbose=1)
filepath = "model.h5"
ckpt = ModelCheckpoint(filepath, monitor='loss', verbose=1, save_best_only=True, mode='min')

def build_network():
    model = Sequential()
    model.add(Dense(160,input_dim=40, activation='relu'))
    model.add(Dropout(0.2))
    model.add(Dense(320, activation='relu'))
    model.add(Dropout(0.2))
    model.add(Dense(365, activation='relu'))
    model.add(Dropout(0.2))
    model.add(Dense(125, activation='relu'))
    model.add(Dropout(0.2))
    model.add(Dense(25, activation='relu'))
    model.add(Dropout(0.2))
    model.add(Dense(1, activation='sigmoid'))
    model.compile(loss='binary_crossentropy', optimizer=, metrics=['accuracy'])
    model.summary()
    return model

model = build_network()

model.fit(scaled_data, train_label[0], validation_split=0.3, epochs=25, callbacks=[es, ckpt])


from keras.models import load_model
new_model = load_model("model.h5")