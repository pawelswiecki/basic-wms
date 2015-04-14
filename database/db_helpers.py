import db_model


# INDIVIDUAL GETTERS
def get_warehouse(id_):
    """ Returns individual warehouse with given *id* or None."""
    query = db_model.Warehouse.query.filter_by(_id=id_)
    if query.count() > 0:
        return query.one()
    else:
        return None

def get_supplier(id_):
    """ Returns individual supplier with given *id* or None."""
    query = db_model.Supplier.query.filter_by(_id=id_)
    if query.count() > 0:
        return query.one()
    else:
        return None

def get_item_type(id_):
    """ Returns individual item_type with given *id* or None."""
    query = db_model.ItemType.query.filter_by(_id=id_)
    if query.count() > 0:
        return query.one()
    else:
        return None

def get_item_batch(id_):
    """ Returns individual item_batch with given *id* or None."""
    query = db_model.ItemBatch.query.filter_by(_id=id_)
    if query.count() > 0:
        return query.one()
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