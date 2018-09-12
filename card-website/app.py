# Import required libraries
import os
from random import randint

import plotly.plotly as py
from plotly.graph_objs import *

import flask
import dash
from dash.dependencies import Input, Output, State, Event
import dash_core_components as dcc
import dash_html_components as html


from gu_analysis import leg_dict, amount

card = leg_dict

app = dash.Dash('Gods Unchained Legendaries')

text_style = dict(color='#444', fontFamily='sans-serif', fontWeight=300)
plotly_figure = dict(data=[dict(x=list(card.keys()), y=list(card.values()), type='bar')])

app.layout = html.Div([
        html.H2('Gods Unchained Legendaries', style=text_style),
        html.P('There are currently {} legendaries'.format(int(amount[3])), style=text_style),
        #dcc.Input(id='text1', placeholder='bar', value=''),
        dcc.Graph(id='plot1', figure=plotly_figure),
    ])



# Setup the app
# Make sure not to change this file name or the variable names below,
# the template is configured to execute 'server' on 'app.py'
server = flask.Flask(__name__)
server.secret_key = os.environ.get('secret_key', str(randint(0, 1000000)))
app = dash.Dash(__name__, server=server)


# Put your Dash code here


# Run the Dash app
if __name__ == '__main__':
    app.server.run(debug=True, threaded=True)
