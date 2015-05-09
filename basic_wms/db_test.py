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
# print("adding batches:")
batch1 = db_api.new_item_batch(quantity=150, warehouse=warehouse1, 
                               supplier=supplier1, item_type=item_type1)
batch2 = db_api.new_item_batch(quantity=56, warehouse=warehouse2, 
                               supplier=supplier2, item_type=item_type2)
batch3 = db_api.new_item_batch(quantity=566, warehouse=warehouse3, 
                               supplier=supplier3, item_type=item_type3)

print("  01.", batch1.supplier.id_ == 1)
print("  02.", batch2.supplier.id_ == 2)
print("  03.", batch3.supplier.id_ == 3)

print("  04.", batch1.warehouse.id_ == 1)
print("  05.", batch2.warehouse.id_ == 2)
print("  06.", batch3.warehouse.id_ == 3)
  
print("  07.", batch1.item_type.id_ == 1)
print("  08.", batch2.item_type.id_ == 2)
print("  09.", batch3.item_type.id_ == 3)

# print("updating warehouse:")
warehouses = db_api.get_warehouses()
warehouse1 = next(warehouses)
warehouse1_id = warehouse1.id_
print(db_api.update_warehouse(warehouse1_id, name="Frank"))
print("  10.", db_api.get_warehouse(warehouse1_id).name == "Frank")
print(db_api.update_warehouse(warehouse1_id, location="new address"))
print("  11.", db_api.get_warehouse(warehouse1_id).location == "new address")

print(db_api.update_warehouse(warehouse1_id, name="Bob", location="newer address"))
print("  12.", db_api.get_warehouse(warehouse1_id).location == "newer address")
print("  13.", db_api.get_warehouse(warehouse1_id).name == "Bob")
print("  14.", db_api.update_warehouse(warehouse1_id, asdqqweqw="qwe") is None)

# print("updating supplier:")
suppliers = db_api.get_suppliers()
supplier1 = next(suppliers)
supplier1_id = supplier1.id_
print(db_api.update_supplier(supplier1_id, VATIN="000000"))
print("  15.", db_api.get_supplier(supplier1_id).VATIN == "000000")
print(db_api.update_supplier(supplier1_id, name="New Name of the Company"))
print("  16.", db_api.get_supplier(supplier1_id).name == "New Name of the Company")

# print("updating item type:")
item_types = db_api.get_item_types()
item_type1 = next(item_types)
item_type1_id = item_type1.id_
print(db_api.update_item_type(item_type1_id, name="mouse", item_model="1001",
                              manufacturer="Logitech"))
print("  17.", db_api.get_item_type(item_type1_id).name == "mouse")
print("  18.", db_api.get_item_type(item_type1_id).item_model == "1001")
print("  19.", db_api.get_item_type(item_type1_id).manufacturer == "Logitech")
print("  20.", db_api.update_item_type(item_type1_id, asdqqweqw="qwe") is None)

# print("updating item batch:")
item_batches = db_api.get_item_batches()
item_batch1 = next(item_batches)

item_types = db_api.get_item_types()
next(item_types)
item_type2 = next(item_types)

suppliers = db_api.get_suppliers()
next(suppliers)
supplier2 = next(suppliers)

warehouses = db_api.get_warehouses()
next(warehouses)
warehouse2 = next(warehouses)

item_batch1_id = item_batch1.id_

print("  21.", db_api.get_item_batch(item_batch1_id).warehouse.id_ == 1)
print("  22.", db_api.get_item_batch(item_batch1_id).supplier.id_ == 1)
print("  23.", db_api.get_item_batch(item_batch1_id).item_type.id_ == 1)
print(db_api.update_item_batch(item_batch1_id, quantity=12345,
                              warehouse=warehouse2, supplier=supplier2,
                              item_type=item_type2))

print("  24.", db_api.get_item_batch(item_batch1_id).warehouse.id_ == 2)
print("  25.", db_api.get_item_batch(item_batch1_id).supplier.id_ == 2)
print("  26.", db_api.get_item_batch(item_batch1_id).item_type.id_ == 2)