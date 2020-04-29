# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 10:17:48 2019

@author: jasa
"""

import csv
import dash
import dash_html_components as html
import dash_core_components as dcc

with open('c:\_PRACA\V300_csv\WC22100700_V300_FT_PL1Llevel.csv') as csvfile:
    datareader = csv.reader(csvfile,delimiter=',', quotechar='"')
    
    i=0
    meas0=[]
    for row in datareader:
        if i > 0:
            meas0.append(row[3])
        i+=1

app = dash.Dash(__name__)

app.layout = html.Div([
    html.Div([
        dcc.Graph(
            id='example-graph',
            figure={
                'data': [
                    {'y': meas0, 'type': 'box', 'name': 'box-plot'},
                    {'y': meas0, 'type': 'box', 'name': 'box-plot2'},
                ],
                'layout': {
                    'title': 'Dash Data Visualization'
                }
            }
        )
    ], style={'width': '50%', 'display': 'inline-block'}),
    html.Div([
        dcc.Graph(
            id='example-graph2',
            figure={
                'data': [
                    {'y': meas0, 'type': 'box', 'name': 'box-plot'},
                    {'y': meas0, 'type': 'box', 'name': 'box-plot2'},
                ],
                'layout': {
                    'title': 'Dash Data Visualization'
                }
            }
        )
    ], style={'width': '50%', 'display': 'inline-block'}),
    html.Div([
        dcc.Graph(
            id='example-graph3',
            figure={
                'data': [
                    {'y': meas0, 'type': 'box', 'name': 'box-plot'},
                    {'y': meas0, 'type': 'box', 'name': 'box-plot2'},
                ],
                'layout': {
                    'title': 'Dash Data Visualization'
                }
            }
        )
    ], style={'width': '50%', 'display': 'inline-block'}),
    html.Div([
        dcc.Graph(
            id='example-graph4',
            figure={
                'data': [
                    {'y': meas0, 'type': 'box', 'name': 'box-plot'},
                    {'y': meas0, 'type': 'box', 'name': 'box-plot2'},
                ],
                'layout': {
                    'title': 'Dash Data Visualization'
                }
            }
        )
    ], style={'width': '50%', 'display': 'inline-block'})])

if __name__ == '__main__':
    app.run_server(port=8051, debug=True) 
