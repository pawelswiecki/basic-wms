from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

class Warehouse(db.Model):
    __tablename__ = 'warehouse'

    id_ = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(80), unique=True, nullable=False)
    location = db.Column(db.String(120), nullable=False)
    
    def __init__(self, name, location):
        self.name = name
        self.location = location

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return "<Warehouse #{}>".format(self.id_)


class ItemType(db.Model):
    __tablename__ = 'item_type'
    
    id_ = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(45), nullable=False)
    model = db.Column(db.String(45), nullable=False)
    unit_of_measure = db.Column(db.String(45), nullable=False)

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return "<ItemType #{}>".format(self.id_)


class Supplier(db.Model):
    __tablename__ = 'supplier'
    
    id_ = db.Column(db.Integer, primary_key=True, nullable=False)
    VATIN = db.Column(db.String(45), nullable=False)
    name = db.Column(db.String(45), nullable=False)
    location = db.Column(db.String(45), nullable=False)

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return "<Supplier #{}>".format(self.id_)


class ItemBatch(db.Model):
    __tablename__ = 'item_batch'

    id_ = db.Column(db.Integer, primary_key=True, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
   
    warehouse_id = db.Column(db.Integer, db.ForeignKey("warehouse.id_"),
                              nullable=False)
    warehouse = db.relationship("Warehouse",
                                backref=db.backref("item_batches",
                                                   lazy="dynamic"))
    
    supplier_id = db.Column(db.Integer, db.ForeignKey("supplier.id_"),
                             nullable=False)
    supplier = db.relationship("Supplier",
                               backref=db.backref("item_batches",
                                                  lazy="dynamic"))

    item_type_id = db.Column(db.Integer, db.ForeignKey("item_type.id_"),
                             nullable=False)
    itemtype = db.relationship("ItemType",
                               backref=db.backref("item_batches",
                                                  lazy="dynamic"))


    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return "<ItemBatch #{}>".format(self.id_)

if __name__ == "__main__":
    db.create_all()    