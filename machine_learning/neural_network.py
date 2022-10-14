import tensorflow as tf
import numpy as np
from tensorflow import keras

"""This simple linear Network has been trained to predict Y in equation Y = 0.5*X +0.5"""

xs = np.array([1.0, 2.0, 3.0, 4.0, 5.0, 6.0,7.0], dtype=float)
ys = np.array([1.0, 1.5, 2.0, 2.5, 3.0, 3.5,4.0], dtype=float)

model = tf.keras.Sequential([keras.layers.Dense(units=1, input_shape=[1],activation='relu'),
                            keras.layers.Dense(units=5, activation='relu'),
                            keras.layers.Dense(units=5, activation='relu'),
                            keras.layers.Dense(units=5, activation='relu'),
                            keras.layers.Dense(units=1,activation='linear')])
model.compile(optimizer='sgd', loss='mean_squared_error')

history=model.fit(xs, ys, epochs=500,verbose=1)

print(model.predict([9.0]))

a = int(input("Enter the value of X : "))
print(model.predict([a]))