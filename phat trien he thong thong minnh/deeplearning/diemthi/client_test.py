import json
import requests


def predict_scores(a, b, c):
    url = 'http://127.0.0.1:5000/scores/v1/predict'
    data = {"10": a, "20_1": b, "20_2": c}
    data_json = json.dumps(data)
    headers = {'Content-type': 'application/json'}
    response = requests.post(url, data=data_json, headers=headers)
    result = json.loads(response.text)
    return result


if __name__ == "__main__":
    predictions = predict_scores(7, 7, 8)
    # print("Diabetic" if predictions["prediction"] == 1 else "NotDiabetic")
    print("prediction: ", predictions["prediction"])
    #print("Confidence: " + predictions["confidence"] + "%")
