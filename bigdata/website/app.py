import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import pandas as pd
from datetime import date, datetime
from pymongo import MongoClient

from __init__ import spark_mongo_server_connection_string, ip_address, port_no, db_name, col_name
# from pyspark.sql import SparkSession
# from pyspark import SparkContext,SparkConf
# conf = SparkConf().set("spark.jars.packages", "org.mongodb.spark:mongo-spark-connector_2.11:2.3.2")
# sc = SparkContext(conf=conf)

# spark = SparkSession.builder.appName("MongoDBIntegration").config("spark.mongodb.input.uri", spark_mongo_server_connection_string).config("spark.mongodb.output.uri", spark_mongo_server_connection_string).getOrCreate()

mongo = MongoClient(ip_address, port_no)
col = mongo[db_name][col_name]

app = dash.Dash()
server = app.server

app.title = 'Big Data Project'

app.layout = html.Main([
    html.Header(['Display Jobs'], style={'width':'100%','display':'block','text-align':'center'}),
    html.Div([
        html.Label(['Title'], style={'width': '10%', 'display': 'inline-table'}),
        dcc.Input(id='title', value='', style={})
    ], style={}),
    html.Br(),
    html.Div([
        html.Label(['Location'], style={'width': '10%', 'display': 'inline-table'}),
        dcc.Input(id='location', value='', style={})
    ], style={}),
    html.Br(),
    html.Div([
        html.Label(['Company'], style={'width': '10%', 'display': 'inline-table'}),
        dcc.Input(id='company', value='', style={})
    ], style={}),
    html.Br(),
    html.Div([
        html.Label(['Description'], style={'width': '10%', 'display': 'inline-table'}),
        dcc.Input(id='description', value='', style={})
    ], style={}),
    html.Br(),
    html.Div([
        html.Label(['Salary'], style={'width': '10%', 'display': 'inline-table'}),
        dcc.Input(id='salary', value='', style={})
    ], style={}),
    html.Br(),
    html.Div([
        html.Label(['Time'], style={'width': '10%', 'display': 'inline-table'}),
        dcc.Input(id='time', value='', style={})
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
    where = f'''Title like "%{title}%" and Location like "%{location}%" and Company like "%{company}%" 
        and Description like "%{description}%" and Salary like "%{salary}%" and Time like "%{time}%"'''
    if sortby == 'random':
        # spark.read.format("com.mongodb.spark.sql.DefaultSource").option("spark.mongodb.input.uri", "mongodb://localhost:27017/jobDB.webscrappingdata")\
        #     .load().select('Title', 'Location', 'Company', 'Description', 'Salary', 'Time').show()
        return 
    else:
        # spark.read.format("com.mongodb.spark.sql.DefaultSource").option("spark.mongodb.input.uri", "mongodb://localhost:27017/jobDB.webscrappingdata")\
        #     .load().select('Title', 'Location', 'Company', 'Description', 'Salary', 'Time').where(where).sort(sortby).show()
        return 