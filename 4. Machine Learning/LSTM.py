# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 18:32:12 2019

@author: AvantikaDG
"""

from scipy.io import loadmat
import pandas as pd
import numpy as np
from keras.layers import Dense, Input, LSTM, Embedding, Dropout
from keras.layers import Bidirectional, GlobalMaxPool1D
from keras.models import  Sequential
from keras import initializers, regularizers, constraints, optimizers, layers


data = loadmat('SleepDataset.mat')

train_data = data['dataset'][:3000]
train_labels_raw = data['datalabels'][:3000]

test_data = data['dataset'][3001:]
test_labels_raw = data['datalabels'][3001:]

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
#test_labels = np.asarray(test_labels)
#test_labels = pd.get_dummies(test_labels)
#test_labels = test_labels.values

train_data = np.reshape(train_data, (train_data.shape[0], 1, train_data.shape[1]))
test_data = np.reshape(test_data, (test_data.shape[0], 1, test_data.shape[1]))

model = Sequential()
model.add(LSTM(1000, return_sequences=False, input_shape=(1, 903)))
model.add(Dropout(0.1))
model.add(Dense(500, activation='tanh'))
model.add(Dropout(0.1))
model.add(Dense(6, activation='sigmoid'))

model.compile(loss = 'categorical_crossentropy',
              optimizer = 'rmsprop',
              metrics = ['accuracy'])
model.fit(train_data, train_labels, batch_size=10, epochs=10)
#score = model.evaluate(test_data, test_labels, batch_size = 10)
yhat = model.predict(test_data, verbose=0)
yhat = np.argmax(yhat, axis=1)
print(np.mean(yhat == test_labels))
#
#train_freq = dict()
#for label in train_labels:
#    if label not in train_freq.keys():
#        train_freq[label] = 1
#    else:
#        train_freq[label] += 1
#
#test_freq = dict()
#for label in test_labels:
#    if label not in test_freq.keys():
#        test_freq[label] = 1
#    else:
#        test_freq[label] += 1
#        
#label_freq = dict()
#for label in data['datalabels']:
#    if label[0] not in label_freq.keys():
#        label_freq[label[0]] = 1
#    else:
#        label_freq[label[0]] += 1