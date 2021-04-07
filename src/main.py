from aws_xray_sdk.core import xray_recorder, patch_all
from aws_xray_sdk.ext.flask.middleware import XRayMiddleware

from flask import Flask
import requests

app = Flask(__name__)

xray_recorder.configure(service='sample-flask-xray-app')
plugins = ('ECSPlugin', 'EC2Plugin')
xray_recorder.configure(plugins=plugins)
patch_all()
XRayMiddleware(app, xray_recorder)

@app.route('/')
def index_handler():
    return "Hello there!"

@app.route('/ip')
def ip_handler():
    resp = requests.get('https://checkip.amazonaws.com')
    if not resp.ok:
        return f"Error: HTTP {resp.status_code}"
    return f"Sever IP is: {resp.text}"

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=80)