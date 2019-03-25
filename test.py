import tensorflow as tf
from tensorflow import keras
import numpy as np

#mnist = keras.datasets.mnist
#(x_train, y_train), (x_test, y_test) = mnist.load_data()

#print([x_test])

import_model = keras.models.load_model('chopsticks_model')
predict = import_model.predict(np.array([[2, 3, 1, 0]]))
print(np.argmax(predict[0]))