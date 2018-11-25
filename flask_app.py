# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html



external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(children=[
    html.H1(children='Projection Comparison'),

    html.Div(children='''
        Dash: A web application framework for Python.
    '''),

    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': [2011, 2016, 2021, 2026, 2031, 2036], 'y': [7218550, 7709400, 8194450, 8633200, 9030000, 9379600], 'type': 'line', 'name': 'DPE'}
                # {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': 'ABS'},
            ],
            'layout': {
                'title': 'Dash Data Visualization'
            }
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)

