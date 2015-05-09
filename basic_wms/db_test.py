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


warehouses = db_api.get_warehouses()
warehouse1 = next(warehouses)
warehouse2 = next(warehouses)
warehouse3 = next(warehouses)

suppliers = db_api.get_suppliers()
supplier1 = next(suppliers)
supplier2 = next(suppliers)
supplier3 = next(suppliers)

item_types = db_api.get_item_types()
item_type1 = next(item_types)
item_type2 = next(item_types)
item_type3 = next(item_types)

print()
print("TESTS")
print("adding batches:")
batch1 = db_api.new_item_batch(150, warehouse1, supplier1, item_type1)
batch2 = db_api.new_item_batch(56, warehouse2, supplier2, item_type2)
batch3 = db_api.new_item_batch(566, warehouse3, supplier3, item_type3)

print("  01.", batch1.supplier.id_ == 1)
print("  02.", batch2.supplier.id_ == 2)
print("  03.", batch3.supplier.id_ == 3)

print("  04.", batch1.warehouse.id_ == 1)
print("  05.", batch2.warehouse.id_ == 2)
print("  06.", batch3.warehouse.id_ == 3)
  
print("  07.", batch1.item_type.id_ == 1)
print("  08.", batch2.item_type.id_ == 2)
print("  09.", batch3.item_type.id_ == 3)

print("updating warehouse:")
warehouses = db_api.get_warehouses()
warehouse1 = next(warehouses)
warehouse1_id = warehouse1.id_
db_api.update_warehouse(warehouse1_id, name="Frank")
print("  10.", db_api.get_warehouse(warehouse1_id).name == "Frank")
db_api.update_warehouse(warehouse1_id, location="new address")
print("  11.", db_api.get_warehouse(warehouse1_id).location == "new address")

db_api.update_warehouse(warehouse1_id, name="Bob", location="newer address")
print("  12.", db_api.get_warehouse(warehouse1_id).location == "newer address")
print("  13.", db_api.get_warehouse(warehouse1_id).name == "Bob")






