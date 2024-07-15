from flask import Flask, render_template, request
import joblib
import numpy as np

# Load the pre-trained model
model = joblib.load('Houses-scraping-and-exploration-main/prediction_model.pkl')

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    nor = int(request.form['input1'])
    Number_of_rooms = (nor - 1) / 5
    Kitchen_type = int(request.form['input2'])
    m = float(request.form['input3'])
    m2 = (m  - 15) / 184
    region = request.form['input4']
    
    regions = ['Praha', 'Jihomoravský','Jihočeský', 'Karlovarský', 'Královéhradecký', 'Liberecký',
       'Moravskoslezský', 'Olomoucký', 'Pardubický', 'Plzeňský',
       'Středočeský', 'Zlínský', 'Vysočina', 'Ústecký']
    
    idx = regions.index(region)
    
    input_data = [[Number_of_rooms, Kitchen_type, m2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    input_data[0][idx + 3] = 1

    prediction = int(model.predict(input_data))
    if Kitchen_type == 0:
        Kitchen_type = 'kk'

    return render_template('result.html', prediction=prediction, region=region, Kitchen_type = Kitchen_type,  Number_of_rooms=nor , m2=m)


if __name__ == '__main__':
    app.run(debug=True)