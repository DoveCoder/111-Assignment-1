
#!/usr/bin/env python3
# _*_ coding: utf8 _*_
"""Sample hello world Flask app"""

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1>Hello, World!<h1>"

@app.route("/products")
def products():
    product_list = {"Apples", "Oranges", "Bananas"}
    bullet_list = "".join(
        "<li>%s<li>" % product for product in product_list
    )
    return "<ul>%s<ul>" % bullet_list