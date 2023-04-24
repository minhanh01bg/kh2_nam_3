#Import required packages
from keras.models import Sequential
from keras.layers import Dense
# import tensorflow.compat.v1 as tf
# tf.disable_control_flow_v2()
import numpy as np
# import tensorflow.compat.v1 as tf
# tf.disable_control_flow_v2()
# Getting the data ready
# Generate train dummy data for 1000 Students and dummy testfor 500
#Columns :Age, Hours of Study &Avg Previous test scores
np.random.seed(2018) #Setting seed for reproducibility
train_data, test_data = np.random.random((1000, 3)),np.random.random((500, 3))
#Generate dummy results for 1000 students : Whether Passed (1) or Failed (0)
labels = np.random.randint(2, size=(1000, 1))
#Defining the model structure with the required layers,

# ofneurons, activation function and optimizers
# tạo model với sequential
model = Sequential()
# tạo layer với 5 neuron, activation function là relu, đầu vào là 3
model.add(Dense(5, input_dim=3, activation='relu'))
model.add(Dense(4, activation='relu'))
model.add(Dense(1, activation='sigmoid'))
# Compile xác định loss function, the optimizer và the metrics
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
#Train the model and make predictions
model.fit(train_data, labels, epochs=10, batch_size=32)
#Make predictions from the trained model