loss_fn = keras.losses.SparseCategoricalCrossentropy()
loss_tracker = keras.metrics.Mean(name="loss")

def training_step(self, data):
    X, y = data
    with tf.GradientTape() as tape:
        logits = self(X)
        loss = loss_fn(y, logits)
    gradients = tape.gradient(loss, self.trainable_weights)
    optimizer.apply_gradients(zip(gradients, self.trainable_weights))

    loss_tracker.update_state(loss)
    return {"loss": loss_tracker.result()}
