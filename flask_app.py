# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_table
import pandas as pd

df = pd.read_csv('assets/NSW_Pop_Proj.csv')

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(
    children=[
        html.H1(
            style={
                'text-align':'center', 
                'color':'rgb(33,150,243)'
            }, 
        
            children='Heading'
        ),

        html.Div(
            children='Second Heading'
        ),

        html.Div(
            style={
                'display':'flex',
                'width':'100%'
            },

            children=html.Div(
                style={
                    'width':'50%',
                    'justify-content':'center'
                },

                children=dcc.Graph(
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
            )
        ),

        dash_table.DataTable(
            id='table',
            columns=[{"name": i, "id": i} for i in df.columns],
            data=df.to_dict("rows")
        )
    ]
)

if __name__ == '__main__':
    app.run_server(debug=True)

