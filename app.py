from flask import Flask, render_template, request
import os
import numpy as np
from src.pilotproject.pipeline.prediction_pipeline import PredictionPipeline

app = Flask(__name__)

@app.route('/', methods=['GET'])
def homepage():
    """
    Renders the homepage with the input form.
    """
    return render_template("index.html")


@app.route('/train', methods=['GET'])
def training():
    """
    Triggers the training pipeline by running the main script.
    """
    os.system('python main.py')
    return 'Training Successful'


@app.route('/predict', methods=['GET', 'POST'])
def predict_route():
    """
    Handles prediction logic:
    - Accepts user input via POST request.
    - Prepares data for model input.
    - Calls the prediction pipeline.
    - Renders prediction results or error message.
    """
    if request.method == 'POST':
        try:
            # Extract user input from form
            fixed_acidity = float(request.form['fixed_acidity'])
            volatile_acidity = float(request.form['volatile_acidity'])
            citric_acid = float(request.form['citric_acid'])
            residual_sugar = float(request.form['residual_sugar'])
            chlorides = float(request.form['chlorides'])
            free_sulfur_dioxide = float(request.form['free_sulfur_dioxide'])
            total_sulfur_dioxide = float(request.form['total_sulfur_dioxide'])
            density = float(request.form['density'])
            pH = float(request.form['pH'])
            sulphates = float(request.form['sulphates'])
            alcohol = float(request.form['alcohol'])

            # Combine input into a single row
            data = np.array([
                fixed_acidity,
                volatile_acidity,
                citric_acid,
                residual_sugar,
                chlorides,
                free_sulfur_dioxide,
                total_sulfur_dioxide,
                density,
                pH,
                sulphates,
                alcohol
            ]).reshape(1, -1)

            # Run prediction pipeline
            obj = PredictionPipeline()
            pred = obj.initiate_prediction(data)

            return render_template('results.html', prediction=str(pred))

        except Exception as e:
            print('The Exception message is:', e)
            return 'Something went wrong during prediction.'
        
    else:
        return render_template('index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
