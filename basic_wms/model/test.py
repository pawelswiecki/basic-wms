from os import remove

from basic_wms.model import db_api
from basic_wms.model import db_model


db_api.new_warehouse(name="Yawn", location="address123")

# suppliers = db_api.get_suppliers


#############################

# db_model.db.create_all()  
# s1 = db_model.Supplier(VATIN="12345643", name="company1", location="address...")
# db_model.db.session.add(s1)

# s2 = db_model.Supplier(VATIN="87654", name="company2", location="address...")
# db_model.db.session.add(s2)

# s3 = db_model.Supplier(VATIN="653547634", name="company3", location="address...")
# db_model.db.session.add(s3)

# i1 = db_model.ItemType(name="keyboard", item_model="x15", unit_of_measure="each")
# db_model.db.session.add(i1)

# w1 = db_model.Warehouse(name="warehouse1", location="some address ...")
# db_model.db.session.add(w1)

# w2 = db_model.Warehouse(name="warehouse2", location="some address 2...")
# db_model.db.session.add(w2)

# w3 = db_model.Warehouse(name="warehouse3", location="some address 3...")
# db_model.db.session.add(w3)

# ib1 = db_model.ItemBatch(quantity=100, warehouse=w1, supplier=s3, item_type=i1)
# db_model.db.session.add(ib1)

# db_model.db.session.commit()

#############################


# new_w = db_api.new_warehouse(name='frank', location='address123')
# new_s = db_api.new_supplier(VATIN="63643235", name="Supplier1234", location="random address")
# new_it = db_api.new_item_type(name='mouse', item_model='45T-X', unit_of_measure='each')
# new_ib = db_api.new_item_batch(quantity=10, warehouse=new_w, supplier=new_s, item_type=new_it)

# print(new_ib.id_)

# db_api.delete_item_batch(id_=1)

# print([w for w in db_api.get_item_batches(with_deleted=False)])
# print()
# print([w for w in db_api.get_item_batches(with_deleted=True)])
# print()

# db_api.undelete_item_batch(id_=1)

# print([w for w in db_api.get_item_batches(with_deleted=False)])
# # print([w for w in db_api.get_item_types()])
# # print([w for w in db_api.get_item_batches()])




