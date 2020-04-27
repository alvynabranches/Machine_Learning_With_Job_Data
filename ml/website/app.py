import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

import plotly.graph_objs as go

import pandas as pd

from datetime import date, datetime

from ml.preprocessing.preprocess_data import text_to_date

from ml.algorithms.base_classifiers import classifiers, classifiers_str
from ml.algorithms.base_classifiers import predict as cpredict, accuracy as caccuracy
from ml.algorithms.base_regressors import regressors, regressors_str
from ml.algorithms.base_regressors import predict as rpredict, accuracy as raccuracy

from __init__ import preprocessed_dataset

df = pd.read_excel(preprocessed_dataset)
df['Time'] = df['Time'].apply(text_to_date)
df = df[df['Title_New'].notnull()]

plots = ['Qualification, Experience vs Salary', 'Education vs Job title']

external_stylesheets = ['style.css']

app = dash.Dash(external_stylesheets=external_stylesheets)
server = app.server
app.title = 'ML Mini Project'
app.layout = html.Main([
    html.Header('Job Prediction', style={'width':'100%','display':'block','text-align':'center'}),
    html.Div([
        html.Label(['Plot type'], style={'width': '12%', 'display': 'inline-table'}),
        dcc.Dropdown(
            id='plottype',
            options=[{'label': e, 'value': e} for e in plots],
            value=plots[0],
            style={'width': '85%', 'display': 'inline-table'}
        )
    ], style={'width': '100%'}),
    html.Br(),
    html.Div([
        html.Label(['Job Title'], style={'width': '12%', 'display': 'inline-table'}),
        dcc.Dropdown(
            id='jobtitle',
            options=[{'label': str(e), 'value': e} for e in df['Title_New'].unique()],
            value=df[df['Title_New'].notnull()]['Title_New'].unique()[0],
            style={'width': '85%', 'display': 'inline-table'}
        )
    ]),
    html.Br(),
    html.Div([
        html.Label(['Location'], style={'width': '12%', 'display': 'inline-table'}),
        dcc.Dropdown(
            id='location',
            options=[{'label': e, 'value': e} for e in df['Location'].unique()],
            value=df['Location'].unique()[0],
            style={'width': '85%', 'display': 'inline-table'}
        )
    ]),
    html.Br(),
    html.Div([
        html.Label(['Algorithm'], style={'width': '12%', 'display': 'inline-table'}),
        dcc.Dropdown(
            id='algorithm',
            # options=[{'label': e, 'value': e} for e in regressors_str],
            # value=regressors_str[0],
            style={'width': '85%', 'display': 'inline-table'}
        )
    ]),
    html.Br(),
    html.Div([
        html.Label(['Options'], style={'width': '12%', 'display': 'inline-table'}),
        dcc.RadioItems(
            id='algorithm',
            # options=[{'label': e, 'value': e} for e in regressors_str],
            # value=regressors_str[0],
            style={'width': '85%', 'display': 'inline-table'}
        )
    ]),
    html.Br(),
    html.Div(id='prediction'),
    html.Br(),
    html.Div(id='accuracy'),
    html.Br()
])

@app.callback(Output('algorithm', 'options'), [Input('plottype', 'value')]) 
def dropdowns(plot):
    if plot == plots[0]:
        return [{'label': e, 'value': e} for e in regressors_str]
    elif plot == plots[1]:
        return [{'label': e, 'value': e} for e in classifiers_str]

@app.callback(Output('algorithm', 'value'), [Input('plottype', 'value')]) 
def dropdowns(plot):
    if plot == plots[0]:
        return regressors_str[0]
    elif plot == plots[1]:
        return classifiers_str[0]

