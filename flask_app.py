# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_table
import pandas as pd
from dash.dependencies import Input, Output

df = pd.read_csv('assets/NSW_Pop_Proj.csv', index_col="Sydney Metropolitan LGAs")

LGAs = df.index

labels_for_drop = []

for i in LGAs:
    labels_for_drop.append({'label': i, 'value': i})

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
            style={
                'display':'flex',
                'width':'100%',
                'justify-content':'center'
            },

            children=html.Div(
                style={
                    'width':'50%'
                    
                },

                children=[
                    dcc.Graph(
                        id='proj_graph',
                        figure={
                            'data': [
                                {'x': [2011, 2016, 2021, 2026, 2031, 2036], 'y': [7218550, 7709400, 8194450, 8633200, 9030000, 9379600], 'type': 'line', 'name': 'DPE'}
                                # {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': 'ABS'},
                            ],
                            'layout': {
                                'title': 'Dash Data Visualization'
                            }
                        }
                    ),

                    dcc.Dropdown(
                        id="LGA_Dropdown",
                        options=labels_for_drop,
                        multi=True,
                        value=["Burwood"]
                    )
                ],
            )
        ),
        

        # dash_table.DataTable(
        #     id='table',
        #     columns=[{"name": i, "id": i} for i in df.columns],
        #     data=df.to_dict("rows")
        # )
    ]
)

@app.callback(
    Output(component_id='proj_graph', component_property='figure'),
    [Input(component_id='LGA_Dropdown', component_property='value')]
)
def update_output_div(input_value):
    LGA_List = []
    for i in input_value:
        LGA_List.append(i)
    return  {
        'data': [{
            'x': [2011, 2016, 2021, 2026, 2031, 2036],
            'y': 
                [
                    df.loc[LGA_List,"2011"].sum(), 
                    df.loc[LGA_List,"2016"].sum(),
                    df.loc[LGA_List,"2021"].sum(),
                    df.loc[LGA_List,"2026"].sum(),
                    df.loc[LGA_List,"2031"].sum(),
                    df.loc[LGA_List,"2036"].sum()
                ], 
            'type': 'line',
            'name': 'DPE'
        }],
        'layout': {
            'title': "Population Projection 2011 - 2036"
        }
    }

if __name__ == '__main__':
    app.run_server(debug=True)

