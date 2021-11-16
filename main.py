#Modified by smartbuilds.io
#Date: 27.09.20
#Desc: This web application serves a motion JPEG stream
# main.py
# import the necessary packages


import time
import threading
import os



# App Globals (do not edit)
# app = Flask(__name__)

from app import app


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=False)
    


