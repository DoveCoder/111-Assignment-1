
#!/usr/bin/env python3
# _*_ coding: utf8 _*_
"""Sample hello world Flask app"""

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1>Hello, World!<h1>"