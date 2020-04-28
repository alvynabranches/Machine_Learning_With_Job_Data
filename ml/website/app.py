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
        html.Label(['Education'], id='educationlabel'),
        dcc.RadioItems(
            id='education',
            options=[
                {'label': 'Tenth', 'value': 'Education_Tenth'}, 
                {'label': 'Twelvth', 'value': 'Education_Twelvth'},
                {'label': 'Bachelors', 'value':'Education_Bachelors'},
                {'label': 'Masters', 'value': 'Education_Masters'},
                {'label': 'Doctorate', 'value': 'Education_Doctorate'}
            ],
            value='Education_Bachelors',
            style={'width': '85%', 'display': 'inline-table'}
        ),
        html.Br(),
        html.Label(['Experience'], id='experiencelabel'),
        dcc.RadioItems(
            id='experience',
            options=[
                {'label': 'XP_Fresher', 'value': 'XP_Fresher'},
                {'label': 'XP_Experience', 'value': 'XP_Experience'}
            ],
            value=regressors_str[0],
            style={'width': '85%', 'display': 'inline-table'}
        ),
    ]),
    html.Br(),
    html.Div([
        html.P(id='prediction')
    ], style={}),
    html.Br(),
    html.Div([
        html.P(id='accuracy')
    ], style={}),
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

@app.callback(Output('educationlabel', 'style'), [Input('plottype', 'value')])
def show_educationlabel(plot):
    if plot == plots[0]:
        return {'width': '12%', 'display': 'inline-table'}
    elif plot == plots[1]:
        return {'width': '12%', 'display': 'inline-table'}

@app.callback(Output('education', 'style'), [Input('plottype', 'value')])
def show_education(plot):
    if plot == plots[0]:
        return {'width': '85%', 'display': 'inline-table'}
    elif plot == plots[1]:
        return {'width': '85%', 'display': 'inline-table'}

@app.callback(Output('experiencelabel', 'style'), [Input('plottype', 'value')])
def show_experiencelabel(plot):
    if plot == plots[0]:
        return {'width': '12%', 'display': 'inline-table'}
    elif plot == plots[1]:
        return {'width': '12%', 'display': 'none'}

@app.callback(Output('experience', 'style'), [Input('plottype', 'value')])
def show_experience(plot):
    if plot == plots[0]:
        return {'width': '85%', 'display': 'inline-table'}
    elif plot == plots[1]:
        return {'width': '85%', 'display': 'none'}

@app.callback(
    Output('prediction', 'children'), 
    [
        Input('plottype', 'value'), 
        Input('location', 'value'), 
        Input('jobtitle', 'value'),
        Input('education', 'value'),
        Input('experience', 'value')
    ]
)
def update_prediction(plot, location, job, education, experience):
    if plot == plots[0]:
        return 
    elif plot == plots[1]:
        return 

@app.callback(
    Output('accuracy', 'children'), 
    [
        Input('plottype', 'value'), 
        Input('location', 'value'), 
        Input('jobtitle', 'value'),
        Input('algorithm', 'value')
    ]
)
def update_accuracy(plot, location, job, algorithm):
    if plot == plots[0]:
        x = df[df['Monthly_Salary'] != 0][['Education_Tenth', 'Education_Twelvth', 'Education_Bachelors', 'Education_Masters', 'Education_Doctorate', 'XP_Experience', 'XP_Fresher']].values
        y = df[df['Monthly_Salary'] != 0]['Monthly_Salary'].values
        for i in range(len(regressors_str)):
            if regressors_str[i] == algorithm:
                return raccuracy(regressors[i], x, y)
    elif plot == plots[1]:
        x = df[['Education_Tenth', 'Education_Twelvth', 'Education_Bachelors', 'Education_Masters', 'Education_Doctorate']].values
        y = df['Title_New'].astype('category').cat.codes.values
        for i in range(len(classifiers_str)):
            if classifiers_str[i] == algorithm:
                return caccuracy(classifiers[i], x, y) 