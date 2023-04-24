import pickle
from flask import Flask, request, json, jsonify
import numpy as np

app = Flask(__name__)
# ---the filename of the saved model---
filename = 'diabetes.sav'
# ---load the saved model---
loaded_model = pickle.load(open(filename, 'rb'))


@app.route('/diabetes/v1/predict', methods=['POST'])
def predict():
    # ---get the features to predict---
    features = request.json
    # ---create the features list for prediction---
    features_list = [features["Glucose"], features["BMI"], features["Age"]]
    # ---get the prediction class---
    prediction = loaded_model.predict([features_list])
    # ---dự đoán xác suất(probabilities)---
    confidence = loaded_model.predict_proba([features_list])
    # ---tính toán để phản hồi lại client---
    response = {}
    response['prediction'] = int(prediction[0])
    response['confidence'] = str(round(np.amax(confidence[0]) * 100, 2)) #độ tin cậy
    return jsonify(response)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
