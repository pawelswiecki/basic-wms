print(" # db_api.py")

# from abc import ABCMeta, abstractmethod

from sqlalchemy.exc import IntegrityError

from basic_wms.model import db_model


class CRUDsAbstractBase:
    """
    Kinda abstract base class.
    """
    @classmethod
    def create(cls, *args, **kwargs):
        raise NotImplementedError('*create* method not implemented')

    @classmethod
    def get_one(cls, id_):
        raise NotImplementedError('*get_one* method not implemented')

    @classmethod
    def get_all(cls, with_deleted=False):
        raise NotImplementedError('*get_all* method not implemented')

    @classmethod
    def update(cls, id_, **kwargs):
        raise NotImplementedError('*update* method not implemented')

    @classmethod
    def delete(cls, id_):
        raise NotImplementedError('*delete* method not implemented')

    @classmethod
    def undelete(cls, id_):
        raise NotImplementedError('*undelete* method not implemented')


class CRUDsCommonFields(CRUDsAbstractBase):
    # SQLA_class gets overwritten by children's class
    SQLA_class = None

    @classmethod
    def create(cls, *args, **kwargs):
        raise NotImplementedError('*create* method not implemented')

    @classmethod
    def get_one(cls, id_):
        """
        Returns dictionary with data about an entity with *id_* id.
        In case of Warehouse:
            {'id': int, 'deleted' : bool, 'name': str, 'location': str}.

        In case of Supplier:
            {'id': int, 'deleted': bool, 'VATIN': str, 'name': str,
             'location': str}.

        In case of ItemType:
            {'id': int, 'deleted': bool, 'name': str, 'item_model': str,
             'manufacturer': str, 'unit_of_measure': str}.

        In case of ItemBatch:
            {'id': int, 'deleted': bool, 'quantity': str,
             'warehouse_id': int, 'supplier_id': int, 'item_type_id': int}.
        """
        try:
            return cls.SQLA_class.get_one(id_).serialize
        except AttributeError:
            raise AttributeError("*SQLA_class* - a class of relevant SQL"
                                 "Alchemy model - should be defined in "
                                 "this CRUD method: {}.".format(cls))

    @classmethod
    def get_all(cls, with_deleted=False):
        """
        Yields all entities in serialized form.
        In case of Warehouse:
            {'id': int, 'deleted' : bool, 'name': str, 'location': str}.

        In case of Supplier:
            {'id': int, 'deleted': bool, 'VATIN': str, 'name': str,
             'location': str}.

        In case of ItemType:
            {'id': int, 'deleted': bool, 'name': str, 'item_model': str,
             'manufacturer': str, 'unit_of_measure': str}.

        In case of ItemBatch:
            {'id': int, 'deleted': bool, 'quantity': str,
             'warehouse_id': int, 'supplier_id': int, 'item_type_id': int}.
        """
        try:
            items = cls.SQLA_class.get_all()
        except AttributeError:
            raise AttributeError("*SQLA_class* - a class of relevant SQL"
                                 "Alchemy model - should be defined in "
                                 "this CRUD method: {}.".format(cls))
        for item in items:
            if not item.deleted or with_deleted:
                yield item.serialize

    @classmethod
    def update(cls, id_, **kwargs):
        raise NotImplementedError('*update* method not implemented')

    @classmethod
    def delete(cls, id_):
        """
        Marks an entity with given *id* as deleted.
        Returns True if successful, False if it was already deleted.
        """
        try:
            item = cls.SQLA_class.get_one(id_=id_)
        except AttributeError:
            raise AttributeError("*SQLA_class* - a class of relevant SQL"
                                 "Alchemy model - should be defined in "
                                 "this CRUD method: {}.".format(cls))
        if not item.deleted:
            item.deleted = True
            db_model.db.session.add(item)
            db_model.db.session.commit()
            return True
        else:
            return False

    @classmethod
    def undelete(cls, id_):
        """
        Marks entity with given *id* as not deleted.
        Returns True if successful, False if it wasn't deleted.
        """
        try:
            item = cls.SQLA_class.get_one(id_=id_)
        except AttributeError:
            raise AttributeError("*SQLA_class* - a class of relevant SQL"
                                 "Alchemy model - should be defined in "
                                 "this CRUD method: {}.".format(cls))
        if item.deleted:
            item.deleted = False
            db_model.db.session.add(item)
            db_model.db.session.commit()
            return True
        else:
            return False

class WarehouseCRUD(CRUDsCommonFields):
    SQLA_class = db_model.WarehouseSQLA

    @classmethod
    def create(cls, name, location):
        """
        Adds warehouse to database and returns its *id* or None in case
        of IntegrityError.
        """
        assert isinstance(name, str),\
            'WarehouseCRUD.create(): name should be a string'
        assert isinstance(location, str),\
            'WarehouseCRUD.create(): location should be a string'

        warehouse = cls.SQLA_class(name=name, location=location)
        db_model.db.session.add(warehouse)
        if _db_commit_with_integrity_handling(db_model.db.session):
            return warehouse.id_
        else:
            return None

    @classmethod
    def update(cls, id_, name=None, location=None):
        """
        Updates in db name and/or location of a warehouse with given *id_*.
        In case of IntegrityError returns False, otherwise returns True.
        """
        # creating dictionary of all arguments, but *id_*
        kwargs = locals()
        kwargs.pop("id_")

        entity = _update_entity(entity=cls.SQLA_class.get_one(id_),
                                kwargs=kwargs)
        db_model.db.session.add(entity)
        return _db_commit_with_integrity_handling(db_model.db.session)

class SupplierCRUD(CRUDsCommonFields):
    SQLA_class = db_model.SupplierSQLA

    @classmethod
    def create(cls, VATIN, name, location):
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

        supplier = cls.SQLA_class(VATIN=VATIN, name=name,
                                  location=location)
        db_model.db.session.add(supplier)
        if _db_commit_with_integrity_handling(db_model.db.session):
            return supplier.id_
        else:
            return None

    @classmethod
    def update(cls, id_, VATIN=None, name=None, location=None):
        """
        Updates in db VATIN and/or name and/or location of a supplier
        with given *id_*.
        In case of IntegrityError returns False, otherwise returns True.
        """
        # creating dictionary of all arguments, but *id_*
        kwargs = locals()
        kwargs.pop("id_")

        entity = _update_entity(entity=cls.SQLA_class.get_one(id_),
                                kwargs=kwargs)
        db_model.db.session.add(entity)
        return _db_commit_with_integrity_handling(db_model.db.session)


class ItemTypeCRUD(CRUDsCommonFields):
    SQLA_class = db_model.ItemTypeSQLA

    @classmethod
    def create(cls, name, item_model, manufacturer, unit_of_measure):
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

        item_type = cls.SQLA_class(name=name, item_model=item_model,
                                   manufacturer=manufacturer,
                                   unit_of_measure=unit_of_measure)
        db_model.db.session.add(item_type)
        if _db_commit_with_integrity_handling(db_model.db.session):
            return item_type.id_
        else:
            return None

    @classmethod
    def update(cls, id_, name=None, item_model=None, manufacturer=None,
               unit_of_measure=None):
        """
        Updates in db name and/or item_model and/or manufacturer
        and/or unit_of_measure of an item_type with given *id_*.
        In case of IntegrityError returns False, otherwise returns True.
        """
        # creating dictionary of all arguments, but *id_*
        kwargs = locals()
        kwargs.pop("id_")

        entity = _update_entity(entity=cls.SQLA_class.get_one(id_),
                                kwargs=kwargs)
        db_model.db.session.add(entity)
        return _db_commit_with_integrity_handling(db_model.db.session)


class ItemBatchCRUD(CRUDsCommonFields):
    SQLA_class = db_model.ItemBatchSQLA

    @classmethod
    def create(cls, quantity, warehouse_id, supplier_id, item_type_id):
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

        warehouse = WarehouseCRUD.SQLA_class.get_one(warehouse_id)
        supplier = SupplierCRUD.SQLA_class.get_one(supplier_id)
        item_type = ItemTypeCRUD.SQLA_class.get_one(item_type_id)

        item_batch = cls.SQLA_class(quantity=quantity, warehouse=warehouse,
                                    supplier=supplier, item_type=item_type)
        db_model.db.session.add(item_batch)
        if _db_commit_with_integrity_handling(db_model.db.session):
            return item_batch.id_
        else:
            return None

    @classmethod
    def update(cls, id_, quantity=None, warehouse_id=None,
               supplier_id=None, item_type_id=None):
        """
        Updates in db quantity_id and/or warehouse_id and/or supplier_id
        and/or item_type of an item_batch with given *id_*.
        In case of IntegrityError returns False, otherwise returns True.
        """
        warehouse = WarehouseCRUD.SQLA_class.get_one(warehouse_id)
        supplier = SupplierCRUD.SQLA_class.get_one(supplier_id)
        item_type = ItemTypeCRUD.SQLA_class.get_one(item_type_id)

        # creating dictionary of all relevant variables
        kwargs = dict()
        for i in ('warehouse', 'supplier', 'item_type'):
            kwargs[i] = locals()[i]

        entity = _update_entity(entity=cls.SQLA_class.get_one(id_),
                                kwargs=kwargs)
        db_model.db.session.add(entity)
        return _db_commit_with_integrity_handling(db_model.db.session)


# HELPER METHODS
def test_wrapper(func, cls):
    def inner(_, *args, **kwargs):
        print("Arguments were: {}, {}".format(args, kwargs))
        return func(cls, *args, **kwargs)
    return inner

def _db_commit_with_integrity_handling(db_session):
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

def _update_entity(entity, kwargs):
    for key, value in kwargs.items():
        if value is not None:
            setattr(entity, key, value)
    return entity