from flask import Flask
import pandas as pd
import pickle
import flask
import numpy as np
app = Flask(__name__)
@app.route("/")
def hello():
    return "Hello World!"
@app.route('/df')
def show_df():
    df = pd.read_csv('../data/train_titanic.csv')
    return df.head().to_html()
@app.route('/greet/<name>')
def greet(name):
    '''Say hello to your first parameter'''
    return f"Hello, {name}!"
with open('./model_randomforest_titanic.p', 'rb') as picklefile:
    model = pickle.load(picklefile)
@app.route('/predict', methods=["GET"])
def predict():
    pclass = flask.request.args['pclass']
    sex = flask.request.args['sex']
    age = flask.request.args['age']
    fare = flask.request.args['fare']
    try:
        sibsp = flask.request.args['sibsp']
    except:
        sibsp = 0
    item = [pclass, sex, age, fare, sibsp]
    item = np.asarray(item)
    item = item.reshape(1,-1)
    score = model.predict_proba(item)
    results = {'survival chances': score[0,1], 'death chances': score[0,0]}
    return flask.jsonify(results)

@app.route('/page')
def page():
   with open("page_example.html", 'r') as viz_file:
       return viz_file.read()

@app.route('/result', methods=['POST'])
def result():
    '''Gets prediction using the HTML form'''
    if flask.request.method == 'POST':
        inputs = flask.request.form
        pclass = inputs['pclass'][0]
        sex = inputs['sex'][0]
        age = inputs['age'][0]
        fare = inputs['fare'][0]
        sibsp = inputs['sibsp'][0]

        item = np.array([pclass, sex, age, fare, sibsp])
        item = item.reshape(1,-1)
        score = model.predict_proba(item)
        results = {'survival chances': score[0,1], 'death chances': score[0,0]}
        return flask.jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)
