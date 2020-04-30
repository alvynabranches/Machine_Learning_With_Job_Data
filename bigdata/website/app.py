import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import pandas as pd
from datetime import date, datetime

app = dash.Dash()
server = app.server

app.title = 'Big Data Project'

app.layout = html.Main([
    html.Header(['Display Jobs'], style={'width':'100%','display':'block','text-align':'center'}),
    html.Div([
        html.Label(['Title'], style={'width': '10%', 'display': 'inline-table'}),
        dcc.Input(id='title', style={})
    ], style={}),
    html.Br(),
    html.Div([
        html.Label(['Location'], style={'width': '10%', 'display': 'inline-table'}),
        dcc.Input(id='location', style={})
    ], style={}),
    html.Br(),
    html.Div([
        html.Label(['Company'], style={'width': '10%', 'display': 'inline-table'}),
        dcc.Input(id='company', style={})
    ], style={}),
    html.Br(),
    html.Div([
        html.Label(['Description'], style={'width': '10%', 'display': 'inline-table'}),
        dcc.Input(id='description', style={})
    ], style={}),
    html.Br(),
    html.Div([
        html.Label(['Salary'], style={'width': '10%', 'display': 'inline-table'}),
        dcc.Input(id='salary', style={})
    ], style={}),
    html.Br(),
    html.Div([
        html.Label(['Time'], style={'width': '10%', 'display': 'inline-table'}),
        dcc.Input(id='time', style={})
    ], style={}),
    html.Br(),
    html.Div([
        html.Label(['Sort By'], style={'width': '10%', 'display': 'inline-table'}),
        dcc.RadioItems(
            id='sortby',
            options=[
                {'label': 'Any', 'value': 'random'}, 
                {'label': 'Title', 'value': 'Title'}, 
                {'label': 'Company', 'value': 'Company'}, 
                {'label': 'Description', 'value': 'Description'}, 
                {'label': 'Salary', 'value': 'Salary'}, 
                {'label': 'Time', 'value': 'Time'}, ],
            value='random',
            style={}
        )
    ]),
    html.Br(),
    html.Div([
        html.P(id='displayarea', style={'align': 'center', 'text-align': 'center'})
    ])
])

@app.callback(Output('displayarea', 'children'), 
    [
        Input('title', 'value'),
        Input('location', 'value'),
        Input('company', 'value'),
        Input('description', 'value'),
        Input('salary', 'value'),
        Input('time', 'value'),
        Input('sortby', 'value')
    ]
)
def show_filtered_data(title, location, company, description, salary, time, sortby):
    if sortby == 'random':
        where = f'''Title = "%{title}%" and Location = "%{location}%" and Company = "%{company}%" 
        and Description = "%{description}%" and Salary = "%{salary}%" and Time = "%{time}%"'''
        return # f'{where}'
    else:
        where = f'''Title = "%{title}%" and Location = "%{location}%" and Company = "%{company}%" 
        and Description = "%{description}%" and Salary = "%{salary}%" and Time = "%{time}%"'''
        sort = f'''{sortby} asc'''
        return # [html.P([f'{where}', html.Br(), f'{sort}'])]

if __name__ == '__main__':
    app.run_server()