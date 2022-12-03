import keras

class ClassificationHead(keras.Model):
    def __init__(self, num_classes=2, multilabel=False):
        super().__init__()
        num_units = 1 if num_classes == 2 else num_classes
        activation = 'sigmoid' if num_classes == 2 or multilabel == True else 'softmax'
        self.dense = keras.layers.Dense(num_units, activation=activation)

    def call(self, inputs):
        return self.dense(inputs)

if __name__ == "__main__":
    inputs = keras.Input()
    features = keras.layers.Dense(64, activation='relu')(inputs)
    outputs = ClassificationHead(num_classes=10)(features)
    model = keras.Model(inputs=inputs, outputs=outputs)