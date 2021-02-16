from my_app import db
from datetime import datetime


class Producto(db.Model):
    __tablename__ = 'Productos'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    price = db.Column(db.Float)
    fecha = db.Column(db.DateTime, default =datetime.now)

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __repr__(self):
        return '<Producto %r %s $RD>' % (self.name, self.price)