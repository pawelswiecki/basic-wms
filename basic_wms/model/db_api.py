print(" # db_api.py")

from basic_wms.model import db_model

# TO DO
# - make functions more abstract to avoid code repetition
# - write Update functions

                                  ############
                                  #  CREATE  #
                                  ############

def new_warehouse(name, location):
    """ Adds new warehouse to db and returns it."""
    warehouse = db_model.Warehouse(name=name, location=location)
    db_model.db.session.add(warehouse)
    db_model.db.session.commit()
    return warehouse

def new_supplier(VATIN, name, location):
    """ Adds new supplier to db and returns it."""
    supplier = db_model.Supplier(VATIN=VATIN, name=name, location=location)
    db_model.db.session.add(supplier)
    db_model.db.session.commit()
    return supplier

def new_item_type(name, item_model, manufacturer, unit_of_measure):
    """ Adds new item type to db and returns it."""
    item_type = db_model.ItemType(name=name, item_model=item_model,
                                  manufacturer=manufacturer,
                                  unit_of_measure=unit_of_measure)
    db_model.db.session.add(item_type)
    db_model.db.session.commit()
    return item_type

def new_item_batch(quantity, warehouse, supplier, item_type):
    """ Adds new item batch to db and returns it."""
    item_batch = db_model.ItemBatch(quantity=quantity, warehouse=warehouse,
                                    supplier=supplier, item_type=item_type)
    db_model.db.session.add(item_batch)
    db_model.db.session.commit()
    return item_batch



                                  ############
                                  #   READ   #
                                  ############

# individual getters
def get_warehouse(id_):
    """
    Returns individual warehouse with given *id* 
    or None if there is no such a warehouse.
    """
    query1 = db_model.Warehouse.query.filter_by(_id=id_)
    if query1.count() > 0:
        return query1.one()
    else:
        return None

def get_supplier(id_):
    """
    Returns individual supplier with given *id*
    or None if there is no such a supplier.
    """
    query1 = db_model.Supplier.query.filter_by(_id=id_)
    if query1.count() > 0:
        return query1.one()
    else:
        return None

def get_item_type(id_):
    """
    Returns individual item_type with given *id*
    or None if there is no such an item_type.
    """
    query1 = db_model.ItemType.query.filter_by(_id=id_)
    if query1.count() > 0:
        return query1.one()
    else:
        return None

def get_item_batch(id_):
    """
    Returns individual item_batch with given *id*
    or None if there is no such an item_type.
    """
    query1 = db_model.ItemBatch.query.filter_by(_id=id_)
    if query1.count() > 0:
        return query1.one()
    else:
        return None

# group getters
def get_warehouses(with_deleted=False):
    """ Yields all warehouses."""
    warehouses = db_model.Warehouse.query.all()
    for warehouse in warehouses:
        if with_deleted or not warehouse.deleted:
            yield warehouse

def get_suppliers(with_deleted=False):
    """ Yields all suppliers."""
    suppliers = db_model.Supplier.query.all()
    for supplier in suppliers:
        if with_deleted or not supplier.deleted:
            yield supplier

def get_item_types(with_deleted=False):
    """ Yields all item_types."""
    item_types = db_model.ItemType.query.all()
    for item_type in item_types:
        if with_deleted or not item_type.deleted:
            yield item_type

def get_item_batches(with_deleted=False):
    """ Yields all item_batches."""
    item_batches = db_model.ItemBatch.query.all()
    for item_batch in item_batches:
        if with_deleted or not item_batch.deleted:
            yield item_batch


                                  ############
                                  #  UPDATE  #
                                  ############

def update_warehouse(id_, name=None, location=None):
    """ Updates in db name and/or location of a warehouse with given *id_*
    and returns it."""
    warehouse = get_warehouse(id_)

    if name:
        warehouse.name = name
    if location:
        warehouse.location = location

    db_model.db.session.add(warehouse)
    db_model.db.session.commit()
    return warehouse

def update_warehouse2(id_, **kwargs):
    """ Updates in db name and/or location of a warehouse with given *id_*
    and returns it.
    Return None if argument's name does not match object's fields."""
    
    if all(key in ("name", "location") for key in kwargs):
        warehouse = get_warehouse(id_)
        for key, value in kwargs.items():            
            setattr(warehouse, key, value)

        db_model.db.session.add(warehouse)
        db_model.db.session.commit()
        return warehouse
    else:
        return None

# def update_supplier(id_, VATIN=None, name=None, location=None):
#     """ Updates a supplier in db and returns it."""
#     supplier = get_supplier(id_)
#     db_model.db.session.add(supplier)
#     db_model.db.session.commit()
#     return supplier

# def update_item_type(id_, name=None, item_model=None, manufacturer=None, unit_of_measure=None):
#     """ Updates a item in db and returns it."""
#     item_type = get_item_type(id_)
#     db_model.db.session.add(item_type)
#     db_model.db.session.commit()
#     return item_type

# def update_item_batch(id_, quantity=None, warehouse=None, supplier=None, 
#                       item_type=None):
#     """ Updates a item in db and returns it."""
#     item_batch = get_item_batch(id_)
#     db_model.db.session.add(item_batch)
#     db_model.db.session.commit()
#     return item_batch


                                  ############
                                  #  DELETE  #
                                  ############

def delete_warehouse(id_):    
    """
    Marks warehouse with given *id* as deleted. 
    Returns True if successful, False if it was already deleted.
    """
    warehouse = get_warehouse(id_=id_)
    if not warehouse.deleted:
        warehouse.deleted = True
        db_model.db.session.add(warehouse)
        db_model.db.session.commit()
        return True
    else:
        return False

def undelete_warehouse(id_):
    """
    Marks warehouse with given *id* as not deleted. 
    Returns True if successful, False if it wasn't deleted.
    """
    warehouse = get_warehouse(id_=id_)
    if warehouse.deleted:
        warehouse.deleted = False
        db_model.db.session.add(warehouse)
        db_model.db.session.commit()
        return True
    else:
        return False


def delete_supplier(id_):
    """
    Marks supplier with given *id* as deleted. 
    Returns True if successful, False if it was already deleted.
    """
    supplier = get_supplier(id_=id_)
    if not supplier.deleted:
        supplier.deleted = True
        db_model.db.session.add(supplier)
        db_model.db.session.commit()
        return True
    else:
        return False

def undelete_supplier(id_):
    """
    Marks supplier with given *id* as not deleted. 
    Returns True if successful, False if it wasn't deleted.
    """
    supplier = get_supplier(id_=id_)
    if supplier.deleted:
        supplier.deleted = False
        db_model.db.session.add(supplier)
        db_model.db.session.commit()
        return True
    else:
        return False

def delete_item_type(id_):
    """
    Marks item_type with given *id* as deleted. 
    Returns True if successful, False if it was already deleted.
    """
    item_type = get_item_type(id_=id_)
    if not item_type.deleted:
        item_type.deleted = True
        db_model.db.session.add(item_type)
        db_model.db.session.commit()
        return True
    else:
        return False

def undelete_item_type(id_):
    """
    Marks item_type with given *id* as not deleted. 
    Returns True if successful, False if it wasn't deleted.
    """
    item_type = get_item_type(id_=id_)
    if item_type.deleted:
        item_type.deleted = False
        db_model.db.session.add(item_type)
        db_model.db.session.commit()
        return True
    else:
        return False

def delete_item_batch(id_):
    """
    Marks item_batch with given *id* as deleted. 
    Returns True if successful, False if it was already deleted.
    """
    item_batch= get_item_batch(id_=id_)
    if not item_batch.deleted:
        item_batch.deleted = True
        db_model.db.session.add(item_batch)
        db_model.db.session.commit()
        return True
    else:
        return False

def undelete_item_batch(id_):
    """
    Marks item_batch with given *id* as not deleted. 
    Returns True if successful, False if it wasn't deleted.
    """
    item_batch = get_item_batch(id_=id_)
    if item_batch.deleted:
        item_batch.deleted = False
        db_model.db.session.add(item_batch)
        db_model.db.session.commit()
        return True
    else:
        return False