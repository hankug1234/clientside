import cv2
import re
from requests import post
import numpy as np
import json
import time
import base64


filename = 'assets/image1.jpg'
image = cv2.imread(filename)
img = cv2.imencode('.jpg',cv2.resize(image,dsize=(300,300),interpolation=cv2.INTER_AREA))[1].tobytes()

filename2 = 'assets/image2.jpg'
image2 = cv2.imread(filename2)
img2 = cv2.imencode('.jpg',cv2.resize(image2,dsize=(300,300),interpolation=cv2.INTER_AREA))[1].tobytes()


a = list(base64.b64encode(img))
b = list(base64.b64encode(img2))




for i in range(1,100):
 if (i%2) == 0:
     data={'image':a,'rate':{'cpu':1.0,'gpu':2.0}}
     post('http://127.0.0.1:5007/data', data={'data': json.dumps(data)})
 else:
     data={'image':b,'rate':{'cpu':1.0,'gpu':2.0}}
     post('http://127.0.0.1:5007/data',data={'data':json.dumps(data)})
 time.sleep(0.5)

