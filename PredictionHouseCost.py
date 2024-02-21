import numpy as np
import tensorflow as tf
import keras

def house(cost):
    xs = np.array([0, 1, 2, 3, 4, 5])
    ys = np.array([50, 100, 150, 200, 250, 300])
    model = keras.Sequential([keras.layers.Dense(units=1, input_shape=[1])])
    model.compile(optimizer='sgd', loss='mean_squared_error')
    model.fit(xs, ys, epochs=600)
    return model.predict(cost)

prediction = house([7])
print(prediction)