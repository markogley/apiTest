
# A very simple Flask Hello World app for you to get started with...

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    x = 2
    y = 4
    z = x + y
    return ' %d what the heck!' % z

