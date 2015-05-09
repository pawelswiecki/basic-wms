print(" # test.py")

from os import getcwd, remove

from basic_wms.model import db_model
from basic_wms.model import db_api


# deletes database file if it exists
cwd = getcwd()
try:
    remove(cwd + "/basic_wms/model/" + db_model.DB_FILENAME)    
except FileNotFoundError:
    print("File not found")

db_model.db.create_all()

db_api.new_warehouse(name="Warehouse 1", location="address123")
db_api.new_warehouse(name="Warehouse 2", location="address314")
db_api.new_warehouse(name="Warehouse 3", location="address4321")

db_api.new_supplier(VATIN="1234-5456-444", name="Company 1", location="address X")
db_api.new_supplier(VATIN="9695-3766-333", name="Company 2", location="address Y")
db_api.new_supplier(VATIN="1010-2020-030", name="Company 3", location="address Z")

db_api.new_item_type(name="keyboard", item_model="X-PRO 2", manufacturer="HiTex",
                     unit_of_measure="EA")

db_api.new_item_type(name="cell phone", item_model="3310", manufacturer="Nokia",
                     unit_of_measure="EA")

db_api.new_item_type(name="water", item_model="fresh", manufacturer="Coca-Cola",
                     unit_of_measure="liter")


# warehouse1 = db_api.get_warehouses()

# print(warehouse1)

# db_model.db.get_engine(app).dispose()

# print(next(warehouse1))

# warehouse1.close()

# print(db_api.get_warehouses().close())