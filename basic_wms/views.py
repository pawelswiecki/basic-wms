print(" # views.py")

from sqlalchemy import create_engine

# from basic_wms import app

from basic_wms import app
import basic_wms.model.db_model
import basic_wms.model.db_api

# testing dabatase api - DELETES DATABASE
import basic_wms.db_test

@app.route('/')
def hello():
    return("Hello, world!")
    