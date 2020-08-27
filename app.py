import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    int_features = [x for x in request.form.values()]
    killPlace = int_features[1]
    maxPlace =int_features[5]
    kills =int_features[11]
    totalDistance =int_features[2]
    killPlaceOverMaxPlace = float(killPlace)/float(maxPlace)
    killsOverDistance = float(kills)/float(totalDistance)
    fin_features = [int_features[0], int_features[1], int_features[2], int_features[3], int_features[4], killPlaceOverMaxPlace, killsOverDistance, int_features[6], int_features[7],int_features[8], int_features[9], int_features[10], int_features[11]]
    for feat in fin_features:
        print(feat)
    final_features = [np.array(fin_features)]
    print(final_features)
    prediction = model.predict(final_features)
    print(prediction)
    output = round(prediction[0], 2)

    return render_template('index.html', prediction_text='{} %'.format(output*100))
@app.route('/predict_api',methods=['POST'])
def predict_api():
    '''
    For direct API calls trought request
    '''
    data = request.get_json(force=True)
    prediction = model.predict([np.array(list(data.values()))])

    output = prediction[0]
    return jsonify(output)

if __name__ == "__main__":
    app.run(debug=True)