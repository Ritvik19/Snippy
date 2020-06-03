import numpy as np
import pandas as pd

from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout
from keras.callbacks import EarlyStopping, ModelCheckpoint

from keras.preprocessing.image import ImageDataGenerator
from keras.preprocessing import image

from keras import backend as K


def recall_m(y_true, y_pred):
        true_positives = K.sum(K.round(K.clip(y_true * y_pred, 0, 1)))
        possible_positives = K.sum(K.round(K.clip(y_true, 0, 1)))
        recall = true_positives / (possible_positives + K.epsilon())
        return recall

def precision_m(y_true, y_pred):
        true_positives = K.sum(K.round(K.clip(y_true * y_pred, 0, 1)))
        predicted_positives = K.sum(K.round(K.clip(y_pred, 0, 1)))
        precision = true_positives / (predicted_positives + K.epsilon())
        return precision

def f1_m(y_true, y_pred):
    precision = precision_m(y_true, y_pred)
    recall = recall_m(y_true, y_pred)
    return 2*((precision*recall)/(precision+recall+K.epsilon()))


es = EarlyStopping(monitor='loss', mode='min', verbose=1)
filepath = "model.h5"
ckpt = ModelCheckpoint(filepath, monitor='loss', verbose=1, save_best_only=True, mode='min')

image_size = (90, 60)

datagen = ImageDataGenerator(rescale = 1./255,
                                   shear_range = 0.2,
                                   zoom_range = 0.2,
                                   horizontal_flip = True,
                                   validation_split=0.3)

training_set = datagen.flow_from_directory('/Train Images',
                                                 target_size = image_size,
                                                 batch_size = 32,
                                                 class_mode = 'binary',
                                                 subset='training')

validation_set = datagen.flow_from_directory('/Train Images',
                                                 target_size = image_size,
                                                 batch_size = 32,
                                                 class_mode = 'binary',
                                                 subset='validation')


def cnn(image_size):
    classifier = Sequential()
    classifier.add(Conv2D(32, (3, 3), input_shape = (*image_size, 3), activation = 'relu'))
    classifier.add(Dropout(0.2))
    classifier.add(Conv2D(32, (3, 3), activation = 'relu'))
    classifier.add(MaxPooling2D(pool_size = (2, 2)))
    classifier.add(Flatten())
    classifier.add(Dense(units = 128, activation = 'relu'))
    classifier.add(Dropout(0.2))
    classifier.add(Dense(units = 1, activation = 'sigmoid'))
    classifier.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['acc',f1_m,precision_m, recall_m])
    return classifier


neuralnetwork = cnn(image_size)


neuralnetwork.summary()


neuralnetwork.fit_generator(training_set,
                         steps_per_epoch = 8000,
                         epochs = 25,
                         validation_data = validation_set,
                         validation_steps = 2000, 
                         callbacks=[es, ckpt])
                         
                         
# Predictions

import numpy as np
import pandas as pd
from keras.preprocessing import image
from keras.models import load_model
from keras import backend as K

def recall_m(y_true, y_pred):
        true_positives = K.sum(K.round(K.clip(y_true * y_pred, 0, 1)))
        possible_positives = K.sum(K.round(K.clip(y_true, 0, 1)))
        recall = true_positives / (possible_positives + K.epsilon())
        return recall

def precision_m(y_true, y_pred):
        true_positives = K.sum(K.round(K.clip(y_true * y_pred, 0, 1)))
        predicted_positives = K.sum(K.round(K.clip(y_pred, 0, 1)))
        precision = true_positives / (predicted_positives + K.epsilon())
        return precision

def f1_m(y_true, y_pred):
    precision = precision_m(y_true, y_pred)
    recall = recall_m(y_true, y_pred)
    return 2*((precision*recall)/(precision+recall+K.epsilon()))

neuralnetwork = load_model('model.h5', custom_objects={'f1_m':f1_m, 'precision_m':precision_m, 'recall_m':recall_m})

test_image = image.load_img(f'/Test Images/{image_path}', target_size = (90, 60))
test_image = image.img_to_array(test_image)
test_image = np.expand_dims(test_image, axis = 0)
class_index = neuralnetwork.predict(test_image)[0][0]
probability = neuralnetwork.predict_proba(test_image)[0][0]