import os
from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your secret key'

from app import routes

if __name__ == '__main__':
    app.run()