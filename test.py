import tensorflow as tf
from tensorflow import keras
import numpy as np

import_model = keras.models.load_model('chopsticks_model')
predict = import_model.predict(np.array([1, 1, 1, 1]))
print(predict)