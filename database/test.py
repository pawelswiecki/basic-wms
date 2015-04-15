from os import remove

import db_helpers
import db_model

# remove db file if it exists
try:
    remove(db_model.DB_FILENAME)
except FileNotFoundError:
    pass

#############################

db_model.db.create_all()  
s1 = db_model.Supplier(VATIN="12345643", name="company1", location="address...")
db_model.db.session.add(s1)

s2 = db_model.Supplier(VATIN="87654", name="company2", location="address...")
db_model.db.session.add(s2)

s3 = db_model.Supplier(VATIN="653547634", name="company3", location="address...")
db_model.db.session.add(s3)

i1 = db_model.ItemType(name="keyboard", item_model="x15", unit_of_measure="each")
db_model.db.session.add(i1)

w1 = db_model.Warehouse(name="warehouse1", location="some address ...")
db_model.db.session.add(w1)

w2 = db_model.Warehouse(name="warehouse2", location="some address 2...")
db_model.db.session.add(w2)

w3 = db_model.Warehouse(name="warehouse3", location="some address 3...")
db_model.db.session.add(w3)

ib1 = db_model.ItemBatch(quantity=100, warehouse=w1, supplier=s3, item_type=i1)
db_model.db.session.add(ib1)

db_model.db.session.commit()

#############################


new_w = db_helpers.new_warehouse(name='frank', location='address123')
new_s = db_helpers.new_supplier(VATIN="63643235", name="Supplier1234", location="random address")
new_it = db_helpers.new_item_type(name='mouse', item_model='45T-X', unit_of_measure='each')
new_ib = db_helpers.new_item_batch(quantity=10, warehouse=new_w, supplier=new_s, item_type=new_it)

print(new_ib.id_)


# print([w for w in get_suppliers()])
# print([w for w in get_item_types()])
# print([w for w in get_item_batches()])




