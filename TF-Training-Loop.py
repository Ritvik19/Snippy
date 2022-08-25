with tf.GradientTape() as tape:
    logits = model(X)
    loss = loss_fn(y, logits)
gradients tape.gradient(loss, model.trainable_weights)
optimizer.apply_gradients(zip(gradients, model.trainable_weights))