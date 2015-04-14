from os import remove

from db_model import *

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

ib1 = ItemBatch(quantity=100, warehouse=w1, supplier=s3, item_type=i1)
db.session.add(ib1)

db.session.commit()

#############################

bob = Warehouse.query.filter_by(_id=1).one()
print(bob.name)

bob.name = "ZIEWAK"
db.session.add(bob)
db.session.commit()

bob2 = Warehouse.query.filter_by(_name="warehouse1").one()
print(bob2.name)
