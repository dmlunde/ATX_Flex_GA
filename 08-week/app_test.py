import plotly.graph_objs as go
import pandas as pd
import plotly.express as px
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']



app = dash.Dash(__name__, external_stylesheets=external_stylesheets)


# input_ = 'PetalWidth'
# df_mean = df.groupby('Name')[input_].mean().to_frame().reset_index()
#
# fig = px.bar(data_frame=df_mean, x='Name', y=input_)

app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),
    dcc.RadioItems(
        options=[
            {'label': 'SepalLength', 'value': 'SepalLength'},
            {'label': 'SepalWidth', 'value': 'SepalWidth'},
            {'label': 'PetalLength', 'value': 'PetalLength'},
        ],
        value='SepalLength',
        id='radio-input1',
    ),

    dcc.RadioItems(
        options=[
            {'label': 'SepalLength', 'value': 'SepalLength'},
            {'label': 'SepalWidth', 'value': 'SepalWidth'},
            {'label': 'PetalLength', 'value': 'PetalLength'},
            ],
        value='SepalLength',
        id='radio-input2',
    ),

    html.Div(children='''
        Dash: A web application framework for Python.
    '''),

    dcc.Graph(
        id='predictions-plot'
),
])

@app.callback(
    Output('predictions-plot', 'figure'),
    [Input('radio-input1', 'value'),
    Input('radio-input2', 'value')]
)
def update_chart(cola, colb):
    df = pd.read_csv('../data/iris.csv')
    return px.scatter(df, x=cola, y=colb, color='Name')


if __name__ == '__main__':
    app.run_server(debug=True, port = 8000)
