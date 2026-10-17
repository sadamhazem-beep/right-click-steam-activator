# build f8e1dd479f
# (auto) 29f82f
from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return 'ok'
