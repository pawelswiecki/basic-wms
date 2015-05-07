import sys

from sqlalchemy import create_engine

from basic_wms import app

import basic_wms.model.db_model
import basic_wms.model.db_api


engine = create_engine('sqlite:///restaurantmenu.db')

@app.route('/')
def hello():
    return("Hello, world!")
    