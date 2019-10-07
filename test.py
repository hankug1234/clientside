import json
import re
from flask import Flask,request
from flask_restful import Resource,Api,reqparse
from collections import deque
from flask_cors import CORS

app = Flask(__name__)
api = Api(app)
CORS(app)
queue = deque(maxlen=5)
queue.append("hellow world")

class Data(Resource):
    def get(self):
        if (len(queue) != 0):
            ra = queue.popleft()
        else:
            ra = '404'
        return {'data': ra}
    def post(self):
        return

api.add_resource(Data,'/data')
if __name__ == '__main__':
    app.run(debug=False,port=5005)