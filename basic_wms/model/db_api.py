print(" # db_api.py")

from sqlalchemy.exc import IntegrityError

from basic_wms.model import db_model



# TODO
# - make that no ORM objects are leaking to user of this API

                                ###############
                                #  WAREHOUSE  #
                                ###############

class WarehouseCRUD:
    def __init__(self, name, location):
        """ Inits WarehouseCRUD object and adds new warehouse to db."""
        self._name = name
        assert isinstance(self._name, str), 'name should be a string'

        self._location = location
        assert isinstance(self._location, str), 'location should be a string'

        # self._id == None if there was IntegrityError
        self._id = self.create(self._name, self._location)
        
    @property
    def name(self):
        return self._name

    @property
    def location(self):
        return self._location

    @property
    def id_(self):
        return self._id

    @staticmethod
    def create(name, location):
        """
        Adds warehouse to database and returns its *id* or None in case
        of IntegrityError.
        """
        warehouse = db_model.WarehouseSQLA(name=name, location=location)
        db_model.db.session.add(warehouse)
        try:
            db_model.db.session.commit()
        except IntegrityError:
            db_model.db.session.rollback()
            return None
        return warehouse.id_

    @staticmethod
    def get_warehouse(id_):
        """
        Returns dictionary with data about warehouse with *id_* id:
        {'id': int, 'deleted': bool, 'name': str, 'location': str}.
        """
        return db_model.WarehouseSQLA.get_warehouse(id_).serialize

    @staticmethod
    def get_warehouses(with_deleted=False):
        """ Yields all warehouses."""
        warehouses = db_model.WarehouseSQLA.get_warehouses()
        for warehouse in warehouses:
            if not warehouse.deleted or with_deleted:
                yield warehouse

    @staticmethod
    def update_warehouse(id_, name=None, location=None):
        """
        Updates in db name and/or location of a warehouse with given *id_*.
        In case of IntegrityError returns False, otherwise returns True.
        """
        # creating dictionary of all arguments, but *id_*
        kwargs = locals()
        kwargs.pop("id_")

        entity = db_model.WarehouseSQLA.get_warehouse(id_)
        for key, value in kwargs.items():
            if value is not None:
                setattr(entity, key, value)
        db_model.db.session.add(entity)
        try:
            db_model.db.session.commit()
        except IntegrityError:
            db_model.db.session.rollback()
            return False
        return True

    @staticmethod
    def delete_warehouse(id_):
        """
        Marks warehouse with given *id* as deleted.
        Returns True if successful, False if it was already deleted.
        """
        warehouse = db_model.WarehouseSQLA.get_warehouse(id_=id_)
        if not warehouse.deleted:
            warehouse.deleted = True
            db_model.db.session.add(warehouse)
            db_model.db.session.commit()
            return True
        else:
            return False

    @staticmethod
    def undelete_warehouse(id_):
        """
        Marks warehouse with given *id* as not deleted.
        Returns True if successful, False if it wasn't deleted.
        """
        warehouse = db_model.WarehouseSQLA.get_warehouse(id_=id_)
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

class SupplierCRUD:
    def __init__(self, VATIN, name, location):
        """ Inits SupplierCRUD object and adds new supplier to db."""
        self._VATIN = VATIN
        assert isinstance(self._VATIN, str), 'VATIN should be a string'

        self._name = name
        assert isinstance(self._name, str), 'name should be a string'

        self._location = location
        assert isinstance(self._location, str), 'location should be a string'

        # self._id == None if there was IntegrityError
        self._id = self.create(self._VATIN, self._name, self._location)

    @property
    def VATIN(self):
        return self._VATIN

    @property
    def name(self):
        return self._name

    @property
    def location(self):
        return self._location

    @property
    def id_(self):
        return self._id

    @staticmethod
    def create(VATIN, name, location):
        """
        Adds supplier to database and returns its *id* or None in case
        of IntegrityError.
        """
        supplier = db_model.SupplierSQLA(VATIN=VATIN, name=name,
                                         location=location)
        db_model.db.session.add(supplier)
        try:
            db_model.db.session.commit()
        except IntegrityError:
            db_model.db.session.rollback()
            return None
        return supplier.id_


    @staticmethod
    def get_supplier(id_):
        """
        Returns dictionary with serialized object's fields:
        {'id': int, 'deleted': bool, 'VATIN': str, 'name': str,
         'location': str}.
        """
        return db_model.SupplierSQLA.get_supplier(id_).serialize

    @staticmethod
    def get_suppliers(with_deleted=False):
        """ Yields all suppliers."""
        suppliers = db_model.SupplierSQLA.get_suppliers()
        for supplier in suppliers:
            if not supplier.deleted or with_deleted:
                yield supplier

    @staticmethod
    def update_supplier(id_, VATIN=None, name=None, location=None):
        """
        Updates in db VATIN and/or name and/or location of a supplier
        with given *id_*.
        In case of IntegrityError returns False, otherwise returns True.
        """
        # creating dictionary of all arguments, but *id_*
        kwargs = locals()
        kwargs.pop("id_")

        entity = db_model.SupplierSQLA.get_supplier(id_)
        for key, value in kwargs.items():
            if value is not None:
                setattr(entity, key, value)
        db_model.db.session.add(entity)
        try:
            db_model.db.session.commit()
        except IntegrityError:
            db_model.db.session.rollback()
            return False
        return True

    @staticmethod
    def delete_supplier(id_):
        """
        Marks supplier with given *id* as deleted.
        Returns True if successful, False if it was already deleted.
        """
        supplier = db_model.SupplierSQLA.get_supplier(id_=id_)
        if not supplier.deleted:
            supplier.deleted = True
            db_model.db.session.add(supplier)
            db_model.db.session.commit()
            return True
        else:
            return False

    @staticmethod
    def undelete_supplier(id_):
        """
        Marks supplier with given *id* as not deleted.
        Returns True if successful, False if it wasn't deleted.
        """
        supplier = db_model.SupplierSQLA.get_supplier(id_=id_)
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


class ItemTypeCRUD:
    def __init__(self, name, item_model, manufacturer, unit_of_measure):
        """ Inits SupplierCRUD object and adds new supplier to db."""
        self._name = name
        assert isinstance(self._name, str), 'name should be a string'

        self._item_model= item_model
        assert isinstance(self._item_model, str),\
            'item_model should be a string'

        self._manufacturer = manufacturer
        assert isinstance(self._manufacturer, str),\
            'manufacturer should be a string'

        self._unit_of_measure = unit_of_measure
        assert isinstance(self._unit_of_measure, str),\
            'unit_of_measure should be a string'

        # self._id == None if there was IntegrityError
        self._id = self.create(self._name, self._item_model, self._manufacturer,
                               self._unit_of_measure)

    @property
    def name(self):
        return self._name

    @property
    def item_model(self):
        return self._item_model

    @property
    def manufacturer(self):
        return self._manufacturer

    @property
    def unit_of_measure(self):
        return self._unit_of_measure

    @property
    def id_(self):
        return self._id

    @staticmethod
    def create(name, item_model, manufacturer, unit_of_measure):
        """
        Adds new item type to db and returns its *id* or None in case of
        IntegrityError.
        """
        item_type = db_model.ItemTypeSQLA(name=name, item_model=item_model,
                                          manufacturer=manufacturer,
                                          unit_of_measure=unit_of_measure)
        db_model.db.session.add(item_type)
        try:
            db_model.db.session.commit()
        except IntegrityError:
            db_model.db.session.rollback()
            return None
        return item_type.id_

    @staticmethod
    def get_item_type(id_):
        """
        Returns dictionary with serialized object's fields:
        {'id': int, 'deleted': bool, 'name': str, 'item_model': str,
         'manufacturer': str, 'unit_of_measure': str}.
        """
        return db_model.ItemTypeSQLA.get_item_type(id_).serialize

    @staticmethod
    def get_item_types(with_deleted=False):
        """ Yields all item_types."""
        item_types = db_model.ItemTypeSQLA.get_item_types()
        for item_type in item_types:
            if not item_type.deleted or with_deleted:
                yield item_type

    @staticmethod
    def update_item_type(id_, name=None, item_model=None, manufacturer=None,
                         unit_of_measure=None):
        """
        Updates in db name and/or item_model and/or manufacturer
        and/or unit_of_measure of an item_type with given *id_*.
        In case of IntegrityError returns False, otherwise returns True.
        """
        # creating dictionary of all arguments, but *id_*
        kwargs = locals()
        kwargs.pop("id_")

        entity = db_model.ItemTypeSQLA.get_item_type(id_)
        for key, value in kwargs.items():
            if value is not None:
                setattr(entity, key, value)
        db_model.db.session.add(entity)
        try:
            db_model.db.session.commit()
        except IntegrityError:
            db_model.db.session.rollback()
            return False
        return True

    @staticmethod
    def delete_item_type(id_):
        """
        Marks item_type with given *id* as deleted.
        Returns True if successful, False if it was already deleted.
        """
        item_type = db_model.ItemTypeSQLA.get_item_type(id_=id_)
        if not item_type.deleted:
            item_type.deleted = True
            db_model.db.session.add(item_type)
            db_model.db.session.commit()
            return True
        else:
            return False

    @staticmethod
    def undelete_item_type(id_):
        """
        Marks item_type with given *id* as not deleted.
        Returns True if successful, False if it wasn't deleted.
        """
        item_type = db_model.ItemTypeSQLA.get_item_type(id_=id_)
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


class ItemBatchCRUD:
    def __init__(self, quantity, warehouse_id, supplier_id, item_type_id):
        """ Inits SupplierCRUD object and adds new supplier to db."""
        self._quantity = quantity
        assert isinstance(self._quantity, int),\
            'quantity should be an integer'

        self._warehouse_id = warehouse_id
        assert isinstance(self._warehouse_id, int),\
            'warehouse_id should be an integer'

        self._supplier_id = supplier_id
        assert isinstance(self._supplier_id, int),\
            'supplier_id should be an integer'

        self._item_type_id = item_type_id
        assert isinstance(self._item_type_id, int),\
            'item_type_id should be an integer'

        # self._id == None if there was IntegrityError
        self._id = self.create(self._quantity, self._warehouse_id,
                               self._supplier_id, self._item_type_id)

    @property
    def quantity(self):
        return self._quantity

    @property
    def warehouse_id(self):
        return self._warehouse_id

    @property
    def quantity(self):
        return self._quantity

    @property
    def supplier_id(self):
        return self._supplier_id

    @property
    def item_type_id(self):
        return self._item_type_id

    @property
    def id_(self):
        return self._id

    @staticmethod
    def create(quantity, warehouse_id, supplier_id, item_type_id):
        """
        Adds new item batch to db and returns its *id* or None in case of
        IntegrityError.
        """
        warehouse = db_model.WarehouseSQLA.get_warehouse(warehouse_id)
        supplier = db_model.SupplierSQLA.get_supplier(supplier_id)
        item_type = db_model.ItemTypeSQLA.get_item_type(item_type_id)

        item_batch = db_model.ItemBatchSQLA(quantity=quantity, warehouse=warehouse,
                                            supplier=supplier, item_type=item_type)
        db_model.db.session.add(item_batch)
        try:
            db_model.db.session.commit()
        except IntegrityError:
            db_model.db.session.rollback()
            return None
        return item_batch.id_

    @staticmethod
    def get_item_batch(id_):
        """
        Returns dictionary with serialized object's fields:
        {'id': int, 'deleted': bool, 'quantity': str,
         'warehouse_id': int, 'supplier_id': int, 'item_type_id': int}.
        """
        return db_model.ItemBatchSQLA.get_item_batch(id_)

    @staticmethod
    def get_item_batches(with_deleted=False):
        """ Yields all item_batches."""
        item_batches = db_model.ItemBatchSQLA.get_item_batches()
        for item_batch in item_batches:
            if not item_batch.deleted or with_deleted:
                yield item_batch

    @staticmethod
    def update_item_batch(id_, quantity=None, warehouse=None, supplier=None,
                          item_type=None):
        """
        Updates in db quantity and/or warehouse and/or supplier
        and/or item_type of an item_batch with given *id_*.
        In case of IntegrityError returns False, otherwise returns True.
        """
        # creating dictionary of all arguments, but *id_*
        kwargs = locals()
        kwargs.pop("id_")

        entity = ItemBatchCRUD.get_item_batch(id_)
        for key, value in kwargs.items():
            if value is not None:
                setattr(entity, key, value)

        db_model.db.session.add(entity)
        try:
            db_model.db.session.commit()
        except IntegrityError:
            db_model.db.session.rollback()
            return False
        return True

    @staticmethod
    def delete_item_batch(id_):
        """
        Marks item_batch with given *id* as deleted.
        Returns True if successful, False if it was already deleted.
        """
        item_batch= ItemBatchCRUD.get_item_batch(id_=id_)
        if not item_batch.deleted:
            item_batch.deleted = True
            db_model.db.session.add(item_batch)
            db_model.db.session.commit()
            return True
        else:
            return False

    @staticmethod
    def undelete_item_batch(id_):
        """
        Marks item_batch with given *id* as not deleted.
        Returns True if successful, False if it wasn't deleted.
        """
        item_batch = ItemBatchCRUD.get_item_batch(id_=id_)
        if item_batch.deleted:
            item_batch.deleted = False
            db_model.db.session.add(item_batch)
            db_model.db.session.commit()
            return True
        else:
            return False