import db_model


# CREATORS
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

def new_item_type(name, model, unit_of_measure):
    """ Adds new item type to db and returns it."""
    item_type = db_model.ItemType(name=name, model=model,
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


# INDIVIDUAL GETTERS
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


# GROUP GETTERS
def get_warehouses():
    """ Yields all warehouses."""
    warehouses = db_model.Warehouse.query.all()
    for warehouse in warehouses:
        yield warehouse

def get_suppliers():
    """ Yields all suppliers."""
    suppliers = db_model.Supplier.query.all()
    for supplier in suppliers:
        yield supplier

def get_item_types():
    """ Yields all item_types."""
    item_types = db_model.ItemType.query.all()
    for item_type in item_types:
        yield item_type

def get_item_batches():
    """ Yields all item_batches."""
    item_batches = db_model.ItemBatch.query.all()
    for item_batch in item_batches:
        yield item_batch