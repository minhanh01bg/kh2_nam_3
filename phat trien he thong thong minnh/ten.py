import tensorflow.compat.v1 as tf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sklearn.model_selection as train_test_split
import keras

x1 = tf.constant(1)
x2 = tf.constant(2)
z = tf.add(x1,x2)
print(tf.Session().run(z))