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

print()
print("TESTS")

print("  #aa", db_api.WarehouseCRUD.create(name="Warehouse 1", location="address123") == 1)
print("  #ab", db_api.WarehouseCRUD.create(name="Warehouse 1", location="asd") is None)
print("  #ac", db_api.WarehouseCRUD.create(name="Warehouse 2", location="address314") == 2)
print("  #ad", db_api.WarehouseCRUD.create(name="Warehouse 3", location="address4321") == 3)

print("  #ba", db_api.SupplierCRUD.create(VATIN="1234-5456-444", name="Company 1", location="address X") == 1)
print("  #bb", db_api.SupplierCRUD.create(VATIN="1234-5456-444", name="Company 102", location="address ASD") is None)
print("  #bc", db_api.SupplierCRUD.create(VATIN="9695-3766-333", name="Company 2", location="address Y") == 2)
print("  #bd", db_api.SupplierCRUD.create(VATIN="1010-2020-030", name="Company 3", location="address Z") == 3)

print("  #ca", db_api.ItemTypeCRUD.create(name="keyboard", item_model="X-PRO 2", manufacturer="HiTex", unit_of_measure="EA") == 1)
print("  #cb", db_api.ItemTypeCRUD.create(name="cell phone", item_model="3310", manufacturer="Nokia", unit_of_measure="EA") == 2)
print("  #cc", db_api.ItemTypeCRUD.create(name="water", item_model="fresh", manufacturer="Coca-Cola", unit_of_measure="liter")== 3)


warehouses = db_api.WarehouseCRUD.get_all()
warehouse1 = next(warehouses)
warehouse2 = next(warehouses)
warehouse3 = next(warehouses)

suppliers = db_api.SupplierCRUD.get_all()
supplier1 = next(suppliers)
supplier2 = next(suppliers)
supplier3 = next(suppliers)

item_types = db_api.ItemTypeCRUD.get_all()
item_type1 = next(item_types)
item_type2 = next(item_types)
item_type3 = next(item_types)


# print("adding batches:")
batch1_id = db_api.ItemBatchCRUD.create(quantity=150, warehouse_id=1,
                               supplier_id=1, item_type_id=1)
batch2_id = db_api.ItemBatchCRUD.create(quantity=56, warehouse_id=2,
                               supplier_id=2, item_type_id=2)
batch3_id = db_api.ItemBatchCRUD.create(quantity=566, warehouse_id=3,
                               supplier_id=3, item_type_id=3)

print("  #01", db_api.ItemBatchCRUD.get_one(batch1_id)['supplier_id'] == 1)
print("  #02", db_api.ItemBatchCRUD.get_one(batch2_id)['supplier_id'] == 2)
print("  #03", db_api.ItemBatchCRUD.get_one(batch3_id)['supplier_id'] == 3)

print("  #04", db_api.ItemBatchCRUD.get_one(batch1_id)['warehouse_id'] == 1)
print("  #05", db_api.ItemBatchCRUD.get_one(batch2_id)['warehouse_id'] == 2)
print("  #06", db_api.ItemBatchCRUD.get_one(batch3_id)['warehouse_id'] == 3)

print("  #07", db_api.ItemBatchCRUD.get_one(batch1_id)['item_type_id'] == 1)
print("  #08", db_api.ItemBatchCRUD.get_one(batch2_id)['item_type_id'] == 2)
print("  #09", db_api.ItemBatchCRUD.get_one(batch3_id)['item_type_id'] == 3)

# print("updating warehouse:")
warehouses = db_api.WarehouseCRUD.get_all()
warehouse1 = next(warehouses)
warehouse1_id = warehouse1['id']
print("  #10", db_api.WarehouseCRUD.update(warehouse1_id, name="Warehouse 2") is False)
print("  #1A", db_api.WarehouseCRUD.update(warehouse1_id, name="Frank") is True)
print("  #11", db_api.WarehouseCRUD.get_one(warehouse1_id)['name'] == "Frank")



print("  #12", db_api.WarehouseCRUD.update(warehouse1_id, location="new address") is not None)
print("  #13", db_api.WarehouseCRUD.get_one(warehouse1_id)['location'] == "new address")

print("  #14", db_api.WarehouseCRUD.update(warehouse1_id, name="Bob", location="newer address") is not None)
print("  #15", db_api.WarehouseCRUD.get_one(warehouse1_id)['location'] == "newer address")
print("  #16", db_api.WarehouseCRUD.get_one(warehouse1_id)['name'] == "Bob")


# print("updating supplier:")
suppliers = db_api.SupplierCRUD.get_all()
supplier1 = next(suppliers)
supplier1_id = supplier1['id']
print("  #17", db_api.SupplierCRUD.update(supplier1_id, VATIN="000000") is True)
print("  #1A", db_api.SupplierCRUD.update(supplier1_id, VATIN="9695-3766-333") is False)
print("  #18", db_api.SupplierCRUD.get_one(supplier1_id)['VATIN'] == "000000")
print("  #19", db_api.SupplierCRUD.update(supplier1_id, name="New Name of the Company") is not None)
print("  #20", db_api.SupplierCRUD.get_one(supplier1_id)['name'] == "New Name of the Company")

# print("updating item type:")
item_types = db_api.ItemTypeCRUD.get_all()
item_type1 = next(item_types)
item_type1_id = item_type1['id']
print("  #21", db_api.ItemTypeCRUD.update(item_type1_id, name="mouse", item_model="1001",
                              manufacturer="Logitech") is True)
print("  #22", db_api.ItemTypeCRUD.get_one(item_type1_id)['name'] == "mouse")
print("  #23", db_api.ItemTypeCRUD.get_one(item_type1_id)['item_model'] == "1001")
print("  #24", db_api.ItemTypeCRUD.get_one(item_type1_id)['manufacturer'] == "Logitech")


# print("updating item batch:")
item_batches = db_api.ItemBatchCRUD.get_all()
item_batch1 = next(item_batches)

item_types = db_api.ItemTypeCRUD.get_all()
next(item_types)
item_type2 = next(item_types)

suppliers = db_api.SupplierCRUD.get_all()
next(suppliers)
supplier2 = next(suppliers)

warehouses = db_api.WarehouseCRUD.get_all()
next(warehouses)
warehouse2 = next(warehouses)

item_batch1_id = item_batch1['id']

print("  #25", db_api.ItemBatchCRUD.get_one(item_batch1_id)['warehouse_id'] == 1)
print("  #26", db_api.ItemBatchCRUD.get_one(item_batch1_id)['supplier_id'] == 1)
print("  #27", db_api.ItemBatchCRUD.get_one(item_batch1_id)['item_type_id'] == 1)
print("  #28", db_api.ItemBatchCRUD.update(item_batch1_id, quantity=12345,
                              warehouse_id=2, supplier_id=3, item_type_id=2) is True)

print("  #29", db_api.ItemBatchCRUD.get_one(item_batch1_id)['warehouse_id'] == 2)
print("  #30", db_api.ItemBatchCRUD.get_one(item_batch1_id)['supplier_id'] == 3)
print("  #31", db_api.ItemBatchCRUD.get_one(item_batch1_id)['item_type_id'] == 2)

# print("deleting:")
print("  #32", (item_batch1['id'] in [x['id'] for x in db_api.ItemBatchCRUD.get_all()]) == True)
print("  #33", db_api.ItemBatchCRUD.delete(item_batch1['id']) == True)
print("  #34", (item_batch1['id'] in [x['id'] for x in db_api.ItemBatchCRUD.get_all()]) == False)
print("  #35", db_api.ItemBatchCRUD.delete(item_batch1['id']) == False)
db_api.ItemBatchCRUD.undelete(item_batch1['id'])
print("  #36", db_api.ItemBatchCRUD.delete(item_batch1['id']) == True)

print("  #37", (item_type2['id'] in [x['id'] for x in db_api.ItemTypeCRUD.get_all()]) == True)
print("  #38", db_api.ItemTypeCRUD.delete(item_type2['id']) == True)
print("  #39", (item_type2['id'] in [x['id'] for x in db_api.ItemTypeCRUD.get_all()]) == False)
print("  #40", db_api.ItemTypeCRUD.delete(item_type2['id']) == False)
db_api.ItemTypeCRUD.undelete(item_type2['id'])
print("  #41", db_api.ItemTypeCRUD.delete(item_type2['id']) == True)

print("  #42", (supplier2['id'] in [x['id'] for x in db_api.SupplierCRUD.get_all()]) == True)
print("  #43", db_api.SupplierCRUD.delete(supplier2['id']) == True)
print("  #44", (supplier2['id'] in [x['id'] for x in db_api.SupplierCRUD.get_all()]) == False)
print("  #45", db_api.SupplierCRUD.delete(supplier2['id']) == False)
db_api.SupplierCRUD.undelete(supplier2['id'])
print("  #46", db_api.SupplierCRUD.delete(supplier2['id']) == True)

print("  #47", (warehouse2['id'] in [x['id'] for x in db_api.WarehouseCRUD.get_all()]) == True)
print("  #48", db_api.WarehouseCRUD.delete(warehouse2['id']) == True)
print("  #49", (warehouse2['id'] in [x['id'] for x in db_api.WarehouseCRUD.get_all()]) == False)
print("  #50", db_api.WarehouseCRUD.delete(warehouse2['id']) == False)
db_api.WarehouseCRUD.undelete(warehouse2['id'])
print("  #51", db_api.WarehouseCRUD.delete(warehouse2['id']) == True)
