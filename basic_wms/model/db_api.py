print(" # db_api.py")

# from abc import ABCMeta, abstractmethod

from sqlalchemy.exc import IntegrityError

from basic_wms.model import db_model


class BaseCRUD():
    """
    An abstract base class.
    """
    @staticmethod
    def create(name, location):
        """
        Adds entity to current persistent data-collection
        and returns its *id* or None in case of IntegrityError.
        """
        raise NotImplementedError('*create* method not implemented')

    @staticmethod
    def get_one(id_):
        """
        Returns dictionary with data about entity with *id_* id:
        {'id': int, 'deleted': bool, 'name': str, 'location': str}.
        """
        raise NotImplementedError('*get_one* method not implemented')

    @staticmethod
    def get_all(with_deleted=False):
        """
        Yields all entities in serialized form:
        {'id': int, 'deleted': bool, 'name': str, 'location': str}.
        """
        raise NotImplementedError('*get_all* method not implemented')


    @staticmethod
    def update(id_, name=None, location=None):
        """
        Updates in db name and/or location of an entity with given *id_*.
        In case of IntegrityError returns False, otherwise returns True.
        """
        raise NotImplementedError('*update* method not implemented')

    @staticmethod
    def delete(id_):
        """
        Marks entity with given *id* as deleted.
        Returns True if successful, False if it was already deleted.
        """
        raise NotImplementedError('*delete* method not implemented')

    @staticmethod
    def undelete(id_):
        """
        Marks entity with given *id* as not deleted.
        Returns True if successful, False if it wasn't deleted.
        """
        raise NotImplementedError('*undelete* method not implemented')


class WarehouseCRUD(BaseCRUD):
    @staticmethod
    def create(name, location):
        """
        Adds warehouse to database and returns its *id* or None in case
        of IntegrityError.
        """
        assert isinstance(name, str),\
            'WarehouseCRUD.create(): name should be a string'
        assert isinstance(location, str),\
            'WarehouseCRUD.create(): location should be a string'

        warehouse = db_model.WarehouseSQLA(name=name, location=location)
        db_model.db.session.add(warehouse)
        if db_commit_with_integrity_handling(db_model.db.session):
            return warehouse.id_
        else:
            return None

    @staticmethod
    def get_one(id_):
        """
        Returns dictionary with data about warehouse with *id_* id:
        {'id': int, 'deleted': bool, 'name': str, 'location': str}.
        """
        return db_model.WarehouseSQLA.get_one(id_).serialize

    @staticmethod
    def get_all(with_deleted=False):
        """
        Yields all warehouses in serialized form:
        {'id': int, 'deleted': bool, 'name': str, 'location': str}.
        """
        warehouses = db_model.WarehouseSQLA.get_all()
        for warehouse in warehouses:
            if not warehouse.deleted or with_deleted:
                yield warehouse.serialize

    @staticmethod
    def update(id_, name=None, location=None):
        """
        Updates in db name and/or location of a warehouse with given *id_*.
        In case of IntegrityError returns False, otherwise returns True.
        """
        # creating dictionary of all arguments, but *id_*
        kwargs = locals()
        kwargs.pop("id_")

        entity = db_model.WarehouseSQLA.get_one(id_)
        for key, value in kwargs.items():
            if value is not None:
                setattr(entity, key, value)
        db_model.db.session.add(entity)
        return db_commit_with_integrity_handling(db_model.db.session)

    @staticmethod
    def delete(id_):
        """
        Marks warehouse with given *id* as deleted.
        Returns True if successful, False if it was already deleted.
        """
        warehouse = db_model.WarehouseSQLA.get_one(id_=id_)
        if not warehouse.deleted:
            warehouse.deleted = True
            db_model.db.session.add(warehouse)
            db_model.db.session.commit()
            return True
        else:
            return False

    @staticmethod
    def undelete(id_):
        """
        Marks warehouse with given *id* as not deleted.
        Returns True if successful, False if it wasn't deleted.
        """
        warehouse = db_model.WarehouseSQLA.get_one(id_=id_)
        if warehouse.deleted:
            warehouse.deleted = False
            db_model.db.session.add(warehouse)
            db_model.db.session.commit()
            return True
        else:
            return False


class SupplierCRUD(BaseCRUD):
    @staticmethod
    def create(VATIN, name, location):
        """
        Adds supplier to database and returns its *id* or None in case
        of IntegrityError.
        """
        assert isinstance(VATIN, str),\
            'SupplierCRUD.create(): VATIN should be a string'
        assert isinstance(name, str),\
            'SupplierCRUD.create(): name should be a string'
        assert isinstance(location, str),\
            'SupplierCRUD.create(): location should be a string'

        supplier = db_model.SupplierSQLA(VATIN=VATIN, name=name,
                                         location=location)
        db_model.db.session.add(supplier)
        if db_commit_with_integrity_handling(db_model.db.session):
            return supplier.id_
        else:
            return None


    @staticmethod
    def get_one(id_):
        """
        Returns dictionary with serialized object's fields:
        {'id': int, 'deleted': bool, 'VATIN': str, 'name': str,
         'location': str}.
        """
        return db_model.SupplierSQLA.get_one(id_).serialize

    @staticmethod
    def get_all(with_deleted=False):
        """
        Yields all suppliers in serialized form:
         {'id': int, 'deleted': bool, 'VATIN': str, 'name': str,
         'location': str}.
        """
        suppliers = db_model.SupplierSQLA.get_all()
        for supplier in suppliers:
            if not supplier.deleted or with_deleted:
                yield supplier.serialize

    @staticmethod
    def update(id_, VATIN=None, name=None, location=None):
        """
        Updates in db VATIN and/or name and/or location of a supplier
        with given *id_*.
        In case of IntegrityError returns False, otherwise returns True.
        """
        # creating dictionary of all arguments, but *id_*
        kwargs = locals()
        kwargs.pop("id_")

        entity = db_model.SupplierSQLA.get_one(id_)
        for key, value in kwargs.items():
            if value is not None:
                setattr(entity, key, value)
        db_model.db.session.add(entity)
        return db_commit_with_integrity_handling(db_model.db.session)

    @staticmethod
    def delete(id_):
        """
        Marks supplier with given *id* as deleted.
        Returns True if successful, False if it was already deleted.
        """
        supplier = db_model.SupplierSQLA.get_one(id_=id_)
        if not supplier.deleted:
            supplier.deleted = True
            db_model.db.session.add(supplier)
            db_model.db.session.commit()
            return True
        else:
            return False

    @staticmethod
    def undelete(id_):
        """
        Marks supplier with given *id* as not deleted.
        Returns True if successful, False if it wasn't deleted.
        """
        supplier = db_model.SupplierSQLA.get_one(id_=id_)
        if supplier.deleted:
            supplier.deleted = False
            db_model.db.session.add(supplier)
            db_model.db.session.commit()
            return True
        else:
            return False


class ItemTypeCRUD(BaseCRUD):
    @staticmethod
    def create(name, item_model, manufacturer, unit_of_measure):
        """
        Adds new item type to db and returns its *id* or None in case of
        IntegrityError.
        """
        assert isinstance(item_model, str),\
            'ItemTypeCRUD.create(): item_model should be a string'
        assert isinstance(manufacturer, str),\
            'ItemTypeCRUD.create(): manufacturer should be a string'
        assert isinstance(unit_of_measure, str),\
            'ItemTypeCRUD.create(): unit_of_measure should be a string'

        item_type = db_model.ItemTypeSQLA(name=name, item_model=item_model,
                                          manufacturer=manufacturer,
                                          unit_of_measure=unit_of_measure)
        db_model.db.session.add(item_type)
        if db_commit_with_integrity_handling(db_model.db.session):
            return item_type.id_
        else:
            return None

    @staticmethod
    def get_one(id_):
        """
        Returns dictionary with serialized object's fields:
        {'id': int, 'deleted': bool, 'name': str, 'item_model': str,
         'manufacturer': str, 'unit_of_measure': str}.
        """
        return db_model.ItemTypeSQLA.get_one(id_).serialize

    @staticmethod
    def get_all(with_deleted=False):
        """
        Yields all item_types in serialized form:
        {'id': int, 'deleted': bool, 'name': str, 'item_model': str,
         'manufacturer': str, 'unit_of_measure': str}.
        """
        item_types = db_model.ItemTypeSQLA.get_all()
        for item_type in item_types:
            if not item_type.deleted or with_deleted:
                yield item_type.serialize

    @staticmethod
    def update(id_, name=None, item_model=None, manufacturer=None,
                         unit_of_measure=None):
        """
        Updates in db name and/or item_model and/or manufacturer
        and/or unit_of_measure of an item_type with given *id_*.
        In case of IntegrityError returns False, otherwise returns True.
        """
        # creating dictionary of all arguments, but *id_*
        kwargs = locals()
        kwargs.pop("id_")

        entity = db_model.ItemTypeSQLA.get_one(id_)
        for key, value in kwargs.items():
            if value is not None:
                setattr(entity, key, value)
        db_model.db.session.add(entity)
        return db_commit_with_integrity_handling(db_model.db.session)

    @staticmethod
    def delete(id_):
        """
        Marks item_type with given *id* as deleted.
        Returns True if successful, False if it was already deleted.
        """
        item_type = db_model.ItemTypeSQLA.get_one(id_=id_)
        if not item_type.deleted:
            item_type.deleted = True
            db_model.db.session.add(item_type)
            db_model.db.session.commit()
            return True
        else:
            return False

    @staticmethod
    def undelete(id_):
        """
        Marks item_type with given *id* as not deleted.
        Returns True if successful, False if it wasn't deleted.
        """
        item_type = db_model.ItemTypeSQLA.get_one(id_=id_)
        if item_type.deleted:
            item_type.deleted = False
            db_model.db.session.add(item_type)
            db_model.db.session.commit()
            return True
        else:
            return False


class ItemBatchCRUD(BaseCRUD):
    @staticmethod
    def create(quantity, warehouse_id, supplier_id, item_type_id):
        """
        Adds new item batch to db and returns its *id* or None in case of
        IntegrityError.
        """
        assert isinstance(quantity, int),\
            'ItemBatchCRUD.create(): quantity should be an integer'
        assert isinstance(warehouse_id, int),\
            'ItemBatchCRUD.create(): warehouse_id should be an integer'
        assert isinstance(supplier_id, int),\
            'ItemBatchCRUD.create(): supplier_id should be an integer'
        assert isinstance(item_type_id, int),\
            'ItemBatchCRUD.create(): item_type_id should be an integer'

        warehouse = db_model.WarehouseSQLA.get_one(warehouse_id)
        supplier = db_model.SupplierSQLA.get_one(supplier_id)
        item_type = db_model.ItemTypeSQLA.get_one(item_type_id)

        item_batch = db_model.ItemBatchSQLA(quantity=quantity, warehouse=warehouse,
                                            supplier=supplier, item_type=item_type)
        db_model.db.session.add(item_batch)
        if db_commit_with_integrity_handling(db_model.db.session):
            return item_batch.id_
        else:
            return None

    @staticmethod
    def get_one(id_):
        """
        Returns dictionary with serialized object's fields:
        {'id': int, 'deleted': bool, 'quantity': str,
         'warehouse_id': int, 'supplier_id': int, 'item_type_id': int}.
        """
        return db_model.ItemBatchSQLA.get_one(id_).serialize

    @staticmethod
    def get_all(with_deleted=False):
        """
        Yields all item_batches in serialized form:
        {'id': int, 'deleted': bool, 'quantity': str,
         'warehouse_id': int, 'supplier_id': int, 'item_type_id': int}.
        """
        item_batches = db_model.ItemBatchSQLA.get_all()
        for item_batch in item_batches:
            if not item_batch.deleted or with_deleted:
                yield item_batch.serialize

    @staticmethod
    def update(id_, quantity=None, warehouse_id=None,
                          supplier_id=None, item_type_id=None):
        """
        Updates in db quantity_id and/or warehouse_id and/or supplier_id
        and/or item_type of an item_batch with given *id_*.
        In case of IntegrityError returns False, otherwise returns True.
        """
        warehouse = db_model.WarehouseSQLA.get_one(warehouse_id)
        supplier = db_model.SupplierSQLA.get_one(supplier_id)
        item_type = db_model.ItemTypeSQLA.get_one(item_type_id)

        # creating dictionary of all relevant variables
        kwargs = dict()
        for i in ('warehouse', 'supplier', 'item_type'):
            kwargs[i] = locals()[i]

        entity = db_model.ItemBatchSQLA.get_one(id_)
        for key, value in kwargs.items():
            if value is not None:
                setattr(entity, key, value)

        db_model.db.session.add(entity)
        return db_commit_with_integrity_handling(db_model.db.session)

    @staticmethod
    def delete(id_):
        """
        Marks item_batch with given *id* as deleted.
        Returns True if successful, False if it was already deleted.
        """
        item_batch= db_model.ItemBatchSQLA.get_one(id_=id_)
        if not item_batch.deleted:
            item_batch.deleted = True
            db_model.db.session.add(item_batch)
            db_model.db.session.commit()
            return True
        else:
            return False

    @staticmethod
    def undelete(id_):
        """
        Marks item_batch with given *id* as not deleted.
        Returns True if successful, False if it wasn't deleted.
        """
        item_batch = db_model.ItemBatchSQLA.get_one(id_=id_)
        if item_batch.deleted:
            item_batch.deleted = False
            db_model.db.session.add(item_batch)
            db_model.db.session.commit()
            return True
        else:
            return False


def db_commit_with_integrity_handling(db_session):
    """
    Takes SQLAlchemy session. Returns False if there was an IntegrityError
    during commit, otherwise returns True.
    """
    try:
        db_session.commit()
    except IntegrityError:
        db_session.rollback()
        return False
    return True