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

db_api.new_item_type(name="keyboard", item_model="", manufacturer="", unit_of_measure="")

# new_warehouse(name, location)
# new_supplier(VATIN, name, location)
# new_item_type(name, item_model, unit_of_measure)
# new_item_batch(quantity, warehouse, supplier, item_type)