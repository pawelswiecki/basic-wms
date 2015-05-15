print(" # db_model.py")

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

from basic_wms import app 

DB_FILENAME = 'database.db'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///model/' + DB_FILENAME
# app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)


class CommonFieldsSQLA():
    """
    Here *_id* and *_deleted*, fields common to all ORM objects,
    are created.
    """
    _id = db.Column(db.Integer, primary_key=True, nullable=False)
    _deleted = db.Column(db.Boolean, nullable=False)

    def init_common_fields(self):
        self._deleted = False

    @property
    def id_(self):
        return self._id

    @property
    def deleted(self):
        return self._deleted
    @deleted.setter
    def deleted(self, value):
        self._deleted = value


class WarehouseSQLA(db.Model, CommonFieldsSQLA):
    __tablename__ = 'warehouse'

    _name = db.Column(db.String(80), unique=True, nullable=False)
    _location = db.Column(db.String(120), nullable=False)
    
    def __init__(self, name, location):
        self.init_common_fields()
        self._name = name
        self._location = location

    def __repr__(self):
        return self.__str__()

    @staticmethod
    def get_warehouse(id_):
        """
        Returns individual warehouse with given *id*
        or None if there is no such a warehouse.
        """
        query1 = WarehouseSQLA.query.filter_by(_id=id_)
        if query1.count() > 0:
            return query1.one()
        else:
            return None

    @staticmethod
    def get_warehouses():
        """ Yields all warehouses."""
        warehouses = WarehouseSQLA.query.all()
        for warehouse in warehouses:
            yield warehouse

    def __str__(self):
        return "<Warehouse #{}>".format(self._id)

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, value):
        self._name = value

    @property
    def location(self):
        return self._location
    @location.setter
    def location(self, value):
        self._location = value

    @property
    def serialize(self):
        """
        Returns dictionary with serialized object's fields:
        {'id': int, 'deleted': bool, 'name': str, 'location': str}.
        """
        return {
            'id': self.id_,
            'deleted': self.deleted,
            'name': self.name,
            'location': self.location,
        }


class ItemTypeSQLA(db.Model, CommonFieldsSQLA):
    __tablename__ = 'item_type'    
    
    _name = db.Column(db.String(45), nullable=False)
    _item_model = db.Column(db.String(45), nullable=False)
    _manufacturer = db.Column(db.String(45), nullable=False)
    _unit_of_measure = db.Column(db.String(45), nullable=False)

    def __init__(self, name, item_model, manufacturer, unit_of_measure):
        self.init_common_fields()
        self._name = name
        self._item_model = item_model
        self._manufacturer = manufacturer
        self._unit_of_measure = unit_of_measure

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return "<ItemType #{}, name: {}>".format(self._id, self._name)

    @staticmethod
    def get_item_type(id_):
        """
        Returns individual item_type with given *id*
        or None if there is no such an item_type.
        """
        query1 = ItemTypeSQLA.query.filter_by(_id=id_)
        if query1.count() > 0:
            return query1.one()
        else:
            return None

    @staticmethod
    def get_item_types():
        """ Yields all item_types."""
        item_types = ItemTypeSQLA.query.all()
        for item_type in item_types:
            yield item_type

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, value):
        self._name = value
    
    @property
    def item_model(self):
        return self._item_model
    @item_model.setter
    def item_model(self, value):
        self._item_model = value

    @property
    def manufacturer(self):
        return self._manufacturer
    @manufacturer.setter
    def manufacturer(self, value):
        self._manufacturer = value
    
    @property
    def unit_of_measure(self):
        return self._unit_of_measure
    @unit_of_measure.setter
    def unit_of_measure(self, value):
        self._unit_of_measure = value

    @property
    def serialize(self):
        """
        Returns dictionary with serialized object's fields:
        {'id': int, 'deleted': bool, 'name': str, 'item_model': str,
         'manufacturer': str, 'unit_of_measure': str}.
        """
        return {
            'id': self.id_,
            'deleted': self.deleted,
            'name': self.name,
            'item_model': self.item_model,
            'manufacturer': self.manufacturer,
            'unit_of_measure': self.unit_of_measure
        }
    

class SupplierSQLA(db.Model, CommonFieldsSQLA):
    __tablename__ = 'supplier'
    
    # VAT identification number (NIP in Poland)
    _VATIN = db.Column(db.String(45), nullable=False, unique=True)
    _name = db.Column(db.String(45), nullable=False)
    _location = db.Column(db.String(45), nullable=False)

    def __init__(self, VATIN, name, location):
        self.init_common_fields()
        self._VATIN = VATIN
        self._name = name
        self._location = location

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return "<Supplier #{}, name: {}>".format(self._id, self._name)

    @staticmethod
    def get_supplier(id_):
        """
        Returns individual supplier with given *id*
        or None if there is no such a supplier.
        """
        query1 = SupplierSQLA.query.filter_by(_id=id_)
        if query1.count() > 0:
            return query1.one()
        else:
            return None

    @staticmethod
    def get_suppliers():
        """ Yields all suppliers."""
        suppliers = SupplierSQLA.query.all()
        for supplier in suppliers:
            yield supplier

    @property
    def VATIN(self):
        return self._VATIN
    @VATIN.setter
    def VATIN(self, value):
        self._VATIN = value
    
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, value):
        self._name = value    

    @property
    def location(self):
        return self._location
    @location.setter
    def location(self, value):
        self._location = value

    @property
    def serialize(self):
        """
        Returns dictionary with serialized object's fields:
        {'id': int, 'deleted': bool, 'VATIN': str, 'name': str,
         'location': str}.
        """
        return {
            'id': self.id_,
            'deleted': self.deleted,
            'VATIN': self.VATIN,
            'name': self.name,
            'location': self.location
        }
    

class ItemBatchSQLA(db.Model, CommonFieldsSQLA):
    __tablename__ = 'item_batch'
    
    _quantity = db.Column(db.Integer, nullable=False)
   
    _warehouse_id = db.Column(db.Integer, db.ForeignKey("warehouse._id"),
                              nullable=False)
    _warehouse = db.relationship("WarehouseSQLA",
                                 backref=db.backref("item_batches",
                                                    lazy="dynamic"))
    
    _supplier_id = db.Column(db.Integer, db.ForeignKey("supplier._id"),
                             nullable=False)
    _supplier = db.relationship("SupplierSQLA",
                                backref=db.backref("item_batches",
                                                   lazy="dynamic"))

    _item_type_id = db.Column(db.Integer, db.ForeignKey("item_type._id"),
                              nullable=False)
    _item_type = db.relationship("ItemTypeSQLA",
                                 backref=db.backref("item_batches",
                                                    lazy="dynamic"))

    def __init__(self, quantity, warehouse, supplier, item_type):
        self.init_common_fields()
        self._quantity = quantity
        self._warehouse = warehouse
        self._supplier = supplier
        self._item_type = item_type

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return "<ItemBatch #{}>".format(self._id)

    @staticmethod
    def get_item_batch(id_):
        """
        Returns individual item_batch with given *id*
        or None if there is no such an item_type.
        """
        query1 = ItemBatchSQLA.query.filter_by(_id=id_)
        if query1.count() > 0:
            return query1.one()
        else:
            return None

    @staticmethod
    def get_item_batches():
        """ Yields all item_batches."""
        item_batches = ItemBatchSQLA.query.all()
        for item_batch in item_batches:
            yield item_batch

    @property
    def quantity(self):
        return self._quantity
    @quantity.setter
    def quantity(self, value):
        self._quantity = value

    @property
    def warehouse(self):
        return self._warehouse
    @warehouse.setter
    def warehouse(self, value):
        self._warehouse = value

    @property
    def supplier(self):
        return self._supplier
    @supplier.setter
    def supplier(self, value):
        self._supplier = value

    @property
    def item_type(self):
        return self._item_type
    @item_type.setter
    def item_type(self, value):
        self._item_type = value

    @property
    def serialize(self):
        """
        Returns dictionary with serialized object's fields:
        {'id': int, 'deleted': bool, 'quantity': str,
         'warehouse_id': int, 'supplier_id': int, 'item_type_id': int}.
        """
        return {
            'id': self.id_,
            'quantity': self.quantity,
            'warehouse_id': self.warehouse.id_,
            'supplier_id': self.supplier.id_,
            'item_type_id': self.item_type.id_
        }
    

if __name__ == "__main__":
    db.create_all()