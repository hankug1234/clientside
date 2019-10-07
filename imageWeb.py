import dash
import json
import dash_core_components as dcc
import dash_html_components as html
from requests import get
import re
import flask
from dash.dependencies import Input, Output,ClientsideFunction
import plotly.graph_objects as go
from collections import deque
from flask_restful import Resource,Api,reqparse
from dash.exceptions import PreventUpdate
import cv2
import base64

es = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=es, routes_pathname_prefix='/show/')


image = cv2.imread("assets/image1.jpg")
img = cv2.imencode('.jpg',image)[1].tobytes()
encoded_image = base64.b64encode(img)


app.layout = html.Div(
[html.Img(src='data:image/jpg;base64,{}'.format(encoded_image.decode()),id='img',width='300px',height='300px')
    ,dcc.Interval(id='interval',interval=500,n_intervals=0)
    ,html.Div(['helloooo'],id='text')]
)

app.clientside_callback(ClientsideFunction(namespace='clientside', function_name='update')
                        ,Output('img','src'),[Input('interval','n_intervals')])

'''
@app.callback(Output('img','src'),[Input('interval','n_intervals')])
def update(n):
    if(n==0):
        raise PreventUpdate
    data = get('http://127.0.0.1:5007/data').json()
    if(data['data'] == '404'):
        raise PreventUpdate
    else:
        encoded_image = bytes(data['data']['image'])
    return 'data:image/jpg;base64,{}'.format(encoded_image.decode())
'''


if __name__ == '__main__':
    app.run_server(debug=False,port=5005)