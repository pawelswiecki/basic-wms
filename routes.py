import sys

import model.db_model
import model.db_helpers

from flask import Flask
from sqlalchemy import create_engine

engine = create_engine('sqlite:///restaurantmenu.db')

app = Flask(__name__)

@app.route('/')
def hello():
    return("Hello, world!")

if __name__ == "__main__":
    app.debug = True
    app.run(host = '0.0.0.0', port = 5000)