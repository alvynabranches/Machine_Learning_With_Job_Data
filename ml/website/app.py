import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import pandas as pd
from datetime import date, datetime
from ml.preprocessing.preprocess_data import text_to_date
from __init__ import preprocessed_dataset


df = pd.read_excel(preprocessed_dataset)

df['Time'] = df['Time'].apply(text_to_date)
