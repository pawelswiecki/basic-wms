from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

DB_FILENAME = 'database.db'

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + DB_FILENAME
db = SQLAlchemy(app)

class Warehouse(db.Model):
    __tablename__ = 'warehouse'

    _id = db.Column(db.Integer, primary_key=True, nullable=False)
    _name = db.Column(db.String(80), unique=True, nullable=False)
    _location = db.Column(db.String(120), nullable=False)
    
    def __init__(self, name, location):
        self._name = name
        self._location = location

    def __repr__(self):
        return self.__str__()

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


class ItemType(db.Model):
    __tablename__ = 'item_type'
    
    _id = db.Column(db.Integer, primary_key=True, nullable=False)
    _name = db.Column(db.String(45), nullable=False)
    _model = db.Column(db.String(45), nullable=False)
    _unit_of_measure = db.Column(db.String(45), nullable=False)

    def __init__(self, name, model, unit_of_measure):
        self._name = name
        self._model = model
        self._unit_of_measure = unit_of_measure

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return "<ItemType #{}, name: {}>".format(self._id, self._name)

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, value):
        self._name = value
    
    @property
    def model(self):
        return self._model
    @model.setter
    def model(self, value):
        self._model = value
    
    @property
    def unit_of_measure(self):
        return self._unit_of_measure
    @unit_of_measure.setter
    def unit_of_measure(self, value):
        self._unit_of_measure = value
    

class Supplier(db.Model):
    __tablename__ = 'supplier'
    
    _id = db.Column(db.Integer, primary_key=True, nullable=False)
    # VAT identification number (NIP in Poland)
    _VATIN = db.Column(db.String(45), nullable=False, unique=True)
    _name = db.Column(db.String(45), nullable=False)
    _location = db.Column(db.String(45), nullable=False)

    def __init__(self, VATIN, name, location):
        self._VATIN = VATIN
        self._name = name
        self._location = location

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return "<Supplier #{}, name: {}>".format(self._id, self._name)

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
    

class ItemBatch(db.Model):
    __tablename__ = 'item_batch'

    _id = db.Column(db.Integer, primary_key=True, nullable=False)
    _quantity = db.Column(db.Integer, nullable=False)
   
    _warehouse_id = db.Column(db.Integer, db.ForeignKey("warehouse._id"),
                              nullable=False)
    _warehouse = db.relationship("Warehouse",
                                 backref=db.backref("item_batches",
                                                   lazy="dynamic"))
    
    _supplier_id = db.Column(db.Integer, db.ForeignKey("supplier._id"),
                             nullable=False)
    _supplier = db.relationship("Supplier",
                                backref=db.backref("item_batches",
                                                  lazy="dynamic"))

    _item_type_id = db.Column(db.Integer, db.ForeignKey("item_type._id"),
                              nullable=False)
    _item_type = db.relationship("ItemType",
                                 backref=db.backref("item_batches",
                                                   lazy="dynamic"))

    def __init__(self, quantity, warehouse, supplier, item_type):
        self._quantity = quantity
        self._warehouse = warehouse
        self._supplier = supplier
        self._item_type = item_type

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return "<ItemBatch #{}>".format(self._id)

    @property
    def quantity(self):
        return self._quantity
    @quantity.setter
    def quantity(self, value):
        self._quantity = value

    @property
    def warehouse_id(self):
        return self._warehouse_id
    @warehouse_id.setter
    def warehouse_id(self, value):
        self._warehouse_id = value

    @property
    def supplier_id(self):
        return self._supplier_id
    @supplier_id.setter
    def supplier_id(self, value):
        self._supplier_id = value

    @property
    def item_type_id(self):
        return self._item_type_id
    @item_type_id.setter
    def item_type_id(self, value):
        self._item_type_id = value    
    

if __name__ == "__main__":
    db.create_all()