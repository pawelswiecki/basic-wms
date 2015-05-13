print(" # db_api.py")

from inspect import getmembers

from basic_wms.model import db_model


                                ###############
                                #  WAREHOUSE  #
                                ###############

def new_warehouse(name, location):
    """ Adds new warehouse to db and returns it."""
    warehouse = db_model.WarehouseSQLA(name=name, location=location)
    db_model.db.session.add(warehouse)
    db_model.db.session.commit()
    return warehouse


def get_warehouse(id_):
    """
    Returns individual warehouse with given *id*
    or None if there is no such a warehouse.
    """
    query1 = db_model.WarehouseSQLA.query.filter_by(_id=id_)
    if query1.count() > 0:
        return query1.one()
    else:
        return None


def get_warehouses(with_deleted=False):
    """ Yields all warehouses."""
    warehouses = db_model.WarehouseSQLA.query.all()
    for warehouse in warehouses:
        if not warehouse.deleted or with_deleted:
            yield warehouse


def update_warehouse(id_, **kwargs):
    """ Updates in db name and/or location of a warehouse with given *id_*
    and returns it.
    Returns None if at least one of argument's name does not match object's
    fields."""

    # checks if arguments in *kwargs* are indeed properties of Warehouse class
    if all(key in property_list(db_model.WarehouseSQLA) for key in kwargs):
        entity = get_warehouse(id_)
        for key, value in kwargs.items():
            setattr(entity, key, value)

        db_model.db.session.add(entity)
        db_model.db.session.commit()
        return entity
    else:
        return None


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


                                ##############
                                #  SUPPLIER  #
                                ##############


def new_supplier(VATIN, name, location):
    """ Adds new supplier to db and returns it."""
    supplier = db_model.SupplierSQLA(VATIN=VATIN, name=name, location=location)
    db_model.db.session.add(supplier)
    db_model.db.session.commit()
    return supplier


def get_supplier(id_):
    """
    Returns individual supplier with given *id*
    or None if there is no such a supplier.
    """
    query1 = db_model.SupplierSQLA.query.filter_by(_id=id_)
    if query1.count() > 0:
        return query1.one()
    else:
        return None


def get_suppliers(with_deleted=False):
    """ Yields all suppliers."""
    suppliers = db_model.SupplierSQLA.query.all()
    for supplier in suppliers:
        if not supplier.deleted or with_deleted:
            yield supplier


def update_supplier(id_, **kwargs):
    """ Updates in db VATIN/name/location of a supplier with given *id_*
    and returns it.
    Returns None if at least one of argument's name does not match object's
    fields."""

    # checks if arguments in *kwargs* are indeed properties of Supplier class
    if all(key in property_list(db_model.SupplierSQLA) for key in kwargs):
        entity = get_supplier(id_)
        for key, value in kwargs.items():
            setattr(entity, key, value)

        db_model.db.session.add(entity)
        db_model.db.session.commit()
        return entity
    else:
        return None


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


                                ###############
                                #  ITEM TYPE  #
                                ###############


def new_item_type(name, item_model, manufacturer, unit_of_measure):
    """ Adds new item type to db and returns it."""
    item_type = db_model.ItemTypeSQLA(name=name, item_model=item_model,
                                  manufacturer=manufacturer,
                                  unit_of_measure=unit_of_measure)
    db_model.db.session.add(item_type)
    db_model.db.session.commit()
    return item_type


def get_item_type(id_):
    """
    Returns individual item_type with given *id*
    or None if there is no such an item_type.
    """
    query1 = db_model.ItemTypeSQLA.query.filter_by(_id=id_)
    if query1.count() > 0:
        return query1.one()
    else:
        return None


def get_item_types(with_deleted=False):
    """ Yields all item_types."""
    item_types = db_model.ItemTypeSQLA.query.all()
    for item_type in item_types:
        if not item_type.deleted or with_deleted:
            yield item_type


def update_item_type(id_, **kwargs):
    """ Updates in db name/item_model/manufacturer/unit_of_measure
    of an item_type with given *id_* and returns it.
    Returns None if at least one of argument's name does not match object's
    fields."""

    # checks if arguments in *kwargs* are indeed properties of ItemType class
    if all(key in property_list(db_model.ItemTypeSQLA) for key in kwargs):
        entity = get_item_type(id_)
        for key, value in kwargs.items():
            setattr(entity, key, value)

        db_model.db.session.add(entity)
        db_model.db.session.commit()
        return entity
    else:
        return None


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

                                ################
                                #  ITEM BATCH  #
                                ################


def new_item_batch(quantity, warehouse, supplier, item_type):
    """ Adds new item batch to db and returns it."""
    item_batch = db_model.ItemBatchSQLA(quantity=quantity, warehouse=warehouse,
                                    supplier=supplier, item_type=item_type)
    db_model.db.session.add(item_batch)
    db_model.db.session.commit()
    return item_batch


def get_item_batch(id_):
    """
    Returns individual item_batch with given *id*
    or None if there is no such an item_type.
    """
    query1 = db_model.ItemBatchSQLA.query.filter_by(_id=id_)
    if query1.count() > 0:
        return query1.one()
    else:
        return None


def get_item_batches(with_deleted=False):
    """ Yields all item_batches."""
    item_batches = db_model.ItemBatchSQLA.query.all()
    for item_batch in item_batches:
        if not item_batch.deleted or with_deleted:
            yield item_batch


def update_item_batch(id_, **kwargs):
    """ Updates in db quantity/warehouse/supplier/item_type
    of an item_batch with given *id_* and returns it.
    Returns None if at least one of argument's name does not match object's
    fields."""
    
    # checks if arguments in *kwargs* are indeed properties of ItemBatch class
    if all(key in property_list(db_model.ItemBatchSQLA) for key in kwargs):
        entity = get_item_batch(id_)
        for key, value in kwargs.items():            
            setattr(entity, key, value)

        db_model.db.session.add(entity)
        db_model.db.session.commit()
        return entity
    else:
        return None


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


                                #############
                                #  HELPERS  #
                                #############


def property_list(cls):
    """
    Return list of properties of *cls* class
    (from: http://stackoverflow.com/questions/1215408).
    """
    return [name for (name, value) in
            getmembers(cls, lambda v: isinstance(v, property))]