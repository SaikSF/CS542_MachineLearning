# -*- coding: utf-8 -*-

from scipy.io import loadmat
import pandas as pd
import numpy as np
from keras.layers import Dense, Dropout
from keras.models import  Sequential

data = loadmat('SplitSleepDataset.mat')

train_data = data['trainingData']
train_labels_raw = data['trainingLabel']

test_data = data['testingData']
test_labels_raw = data['testingLabel']

# Adding label 4 to test set
np.append(test_data, train_data[338])
np.append(test_labels_raw, train_labels_raw[338])

train_labels = []
for label in train_labels_raw:
    train_labels.append(label[0])
train_labels = np.asarray(train_labels)
train_labels = pd.get_dummies(train_labels)
train_labels = train_labels.values
print(train_labels.shape)

test_labels = []
for label in test_labels_raw:
    test_labels.append(label[0])

model = Sequential()
model.add(Dense(1000, activation='relu'))
model.add(Dropout(0.1))
model.add(Dense(500, activation='tanh'))
model.add(Dropout(0.1))
model.add(Dense(6, activation='sigmoid'))
model.compile(loss = 'categorical_crossentropy',
              optimizer = 'rmsprop',
              metrics = ['accuracy'])
model.fit(train_data, train_labels, batch_size=10, epochs=20)

yhat = model.predict(test_data, verbose=0)
yhat = np.argmax(yhat, axis=1)
print('Accuracy on test set:', np.mean(yhat == test_labels))

# Figuring out location of label 4. Hardcoded the position in the script. `
#cnt= 0
#for i in range(len(train_labels_raw)):
#    if train_labels_raw[i] == 4:
#        print(i)