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

    def __init__(self, name, model, unit_of_measure):
        self.name = name
        self.model = model
        self.unit_of_measure = unit_of_measure

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return "<ItemType #{}, name: {}>".format(self.id_, self.name)


class Supplier(db.Model):
    __tablename__ = 'supplier'
    
    id_ = db.Column(db.Integer, primary_key=True, nullable=False)
    # VAT identification number (NIP in Poland)
    VATIN = db.Column(db.String(45), nullable=False, unique=True)
    name = db.Column(db.String(45), nullable=False)
    location = db.Column(db.String(45), nullable=False)

    def __init__(self, VATIN, name, location):
        self.VATIN = VATIN
        self.name = name
        self.location = location

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
    item_type = db.relationship("ItemType",
                                backref=db.backref("item_batches",
                                                   lazy="dynamic"))

    def __init__(self, quantity, warehouse, supplier, item_type):
        self.quantity = quantity
        self.warehouse = warehouse
        self.supplier = supplier
        self.item_type = item_type

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return "<ItemBatch #{}>".format(self.id_)

if __name__ == "__main__":
    db.create_all()    

    s1 = Supplier(VATIN="12345643", name="company1", location="address...")
    db.session.add(s1)

    s2 = Supplier(VATIN="87654", name="company2", location="address...")
    db.session.add(s2)

    s3 = Supplier(VATIN="653547634", name="company3", location="address...")
    db.session.add(s3)

    i1 = ItemType(name="keyboard", model="x15", unit_of_measure="each")
    db.session.add(i1)

    w1 = Warehouse(name="warehouse1", location="some address ...")
    db.session.add(w1)

    ib1 = ItemBatch(quantity=100, warehouse=w1, supplier=s3, item_type=i1)
    db.session.add(ib1)

    db.session.commit()