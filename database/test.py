from os import remove

from db_model import *
from db_helpers import *

# remove db file if it exists
try:
    remove(DB_FILENAME)
except FileNotFoundError:
    pass

#############################

db.create_all()  
s1 = Supplier(VATIN="12345643", name="company1", location="address...")
db.session.add(s1)

s2 = Supplier(VATIN="87654", name="company2", location="address...")
db.session.add(s2)

s3 = Supplier(VATIN="653547634", name="company3", location="address...")
db.session.add(s3)

i1 = ItemType(name="keyboard", model="x15", unit_of_measure="each")
db.session.add(i1)

w1 = Warehouse(name="warehouse1", location="some address ...")
db.session.add(w1)

w2 = Warehouse(name="warehouse2", location="some address 2...")
db.session.add(w2)

w3 = Warehouse(name="warehouse3", location="some address 3...")
db.session.add(w3)

ib1 = ItemBatch(quantity=100, warehouse=w1, supplier=s3, item_type=i1)
db.session.add(ib1)

db.session.commit()

#############################


new_w = new_warehouse(name='frank', location='address123')
new_s = new_supplier(VATIN="63643235", name="Supplier1234", location="random address")
new_it = new_item_type(name='mouse', model='45T-X', unit_of_measure='each')
new_ib = new_item_batch(quantity=10, warehouse=new_w, supplier=new_s, item_type=new_it)

print(new_ib.warehouse.id)



print(new_ib.warehouse.id)

