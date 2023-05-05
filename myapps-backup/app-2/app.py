import json
import flask
from time import sleep
import logging
import socket

app = flask.Flask(__name__)
app.config["DEBUG"] = True
logging.basicConfig(level=logging.INFO)

@app.route('/hello')
def hello():
    hostname = socket.gethostname()
    return f'Hello World! from APP 2 and node {hostname}'

@app.route('/get', methods=['GET'])
def getMethod():
    jsonReq = flask.request.json
    jsonResp = {}
    try:
        logging.info(jsonReq)
    except IOError as identifier:
        print(identifier)
    return jsonResp

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
