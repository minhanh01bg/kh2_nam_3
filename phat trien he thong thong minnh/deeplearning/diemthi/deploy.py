import pickle
from flask import Flask, request, json, jsonify
import numpy as np
#  load the model
from tensorflow.keras.models import load_model
app = Flask(__name__)
# ---the filename of the saved model---
filename = 'model.h5'
# ---load the saved model---
model = load_model(filename)


@app.route('/scores/v1/predict', methods=['POST'])
def predict():
    # ---get the features to predict---
    features = request.json
    # ---create the features list for prediction---
    features_list = [int(features["10"]), int(features["20_1"]), int(features["20_2"])]
    # ---get the prediction class---
    prediction = model.predict([features_list])
    # ---dự đoán xác suất(probabilities)---
    # confidence = model.predict_proba([features_list])
    # ---tính toán để phản hồi lại client---
    response = {}
    response['prediction'] = int(prediction[0])
    #response['confidence'] = str(round(np.amax(confidence[0]) * 100, 2)) #độ tin cậy
    return jsonify(response)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
