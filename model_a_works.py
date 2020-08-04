import tensorflow as tf
from tensorflow import keras


def train_model_a(train_images, train_labels):
    train_images = train_images / 255.0

    model = keras.Sequential([
        keras.layers.Flatten(input_shape=(28, 28)),
        keras.layers.Dense(128, activation='relu'),
        keras.layers.Dense(10)
    ])
    model.compile(optimizer='adam',
                  loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
                  metrics=['accuracy'])
    model.fit(train_images, train_labels, epochs=10)
    # test_loss, test_acc = model.evaluate(test_images, test_labels, verbose=2)
    #
    # print('\nTest accuracy:', test_acc)
    probability_model = tf.keras.Sequential([model,
                                             tf.keras.layers.Softmax()])

    return probability_model

    # predictions = probability_model.predict(test_images)
    # print(predictions[0])