from flask import Flask
import pandas as pd
import pickle

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello World!"

@app.route("/df")
def show_df():
    df = pd.read_csv('../data/train_titanic.csv')
    return df.head().to_html()

@app.route('/greet/<name>')
def greet(name):
    '''Say hello to your first parameter'''
    return f"Hello, {name}!"



if __name__ == '__main__':
    app.run(debug=True)
