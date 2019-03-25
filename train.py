import tensorflow as tf
from tensorflow import keras
import numpy as np

with open("output.txt") as f:
	content = f.readlines()

data = [x.strip() for x in content]

(x_train, y_train) = ([] * 5, [])

for d in data:
	if d != '':
		x_train.append([int(d[0]), int(d[2]), int(d[4]), int(d[6])])
		y_train.append(int(d[8:]))

x_train = np.array(x_train)
y_train = np.array(y_train)

model = keras.models.Sequential()
model.add(keras.layers.Flatten())

model.add(keras.layers.Dense(64, activation=tf.nn.relu))
model.add(keras.layers.Dense(13, activation=tf.nn.softmax))

model.compile(optimizer='adam',
			  loss='sparse_categorical_crossentropy',
			  metrics=['accuracy'])

model.fit(x_train, y_train, epochs=1)

model.save('chopsticks_model')

guess = np.array([[1,1,1,1]])

predictions = model.predict(guess)
print(np.argmax(predictions[0]))