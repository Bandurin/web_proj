#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, render_template
from itertools import cycle



import subprocess

app = Flask(__name__)
app.config.from_object('config')
state_cycle = cycle(['on', 'off'])


@app.route("/")
def index():
        return render_template("index.html")

@app.route("/")
def camera(state=None):
    if state == 'on':
        subprocess.call(['/home/pi/mjpg-streamer/start.sh'],shell=False)
    if state == 'off':
        subprocess.call(['killall -9 mjpg-streamer'],shell=False)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)


