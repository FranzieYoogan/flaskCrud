from turtle import pd
from flask import Flask
from run import search
from markupsafe import escape
from db import *
app = Flask(__name__)

@app.route("/", methods=['GET'])
def hello_world():

    # return "<p>Hello, World!</p>"
    return  f'<h1 style="color: pink;">{escape((json_output.replace('"','').replace("[","").replace("]","") ))}</h1>'

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=3001)