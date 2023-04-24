import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Activation
# Generate dummy training dataset
import tensorflow.compat.v1 as tf
tf.disable_control_flow_v2()
np.random.seed(2018)
x_train = np.random.random((6000,10))
y_train = np.random.randint(2, size=(6000, 1))
# Generate dummy validation dataset
x_val = np.random.random((2000,10))
y_val = np.random.randint(2, size=(2000, 1))
# Generate dummy test dataset
x_test = np.random.random((2000,10))
y_test = np.random.randint(2, size=(2000, 1))
#Define the model architecture
model = Sequential()
model.add(Dense(64, input_dim=10,activation = "relu")) #Layer 1
model.add(Dense(32,activation = "relu")) #Layer 2
model.add(Dense(16,activation = "relu")) #Layer 3
model.add(Dense(8,activation = "relu")) #Layer 4
model.add(Dense(4,activation = "relu")) #Layer 5
model.add(Dense(1,activation = "sigmoid")) #OutputLayer
#Configure the model
# Compile xác định loss function, the optimizer và the metrics
model.compile(optimizer='Adam',loss='binary_crossentropy',metrics=['accuracy'])
#Train the model
model.fit(x_train, y_train, batch_size=64, epochs=10,validation_data=(x_val,y_val))
# epochs số lần lặp lại => epochs càng lớn, model được train nhiều hơn
#evaluate(x=None, y=None, batch_size=None, verbose=1,sample_weight=None, steps=None)
print(model.evaluate(x_test,y_test))
print(model.metrics_names)
#print 10 predictions
pred = model.predict(x_test)
pred[:10]
