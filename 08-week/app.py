import plotly.graph_objs as go
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.express as px
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
df = pd.read_csv('../data/iris.csv')
fig = px.scatter(df, x='SepalWidth', y='SepalLength', color='Name')
### anywhere before app.layout create your figure
app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),
    html.Div(children='''
        Dash: A web application framework for Python.
    '''),
    dcc.Graph(
        id='example-graph',
        figure = fig ### this is the figure you created earlier
    )
])
if __name__ == '__main__':
    app.run_server(debug=True)
