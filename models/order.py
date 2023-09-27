from sqlalchemy import Column, String, Integer, Float, Boolean, ForeignKey, DataTime
from sqlalchemy.orm import relationship, backref
from sqlalchemy.orm import declarative_base

from models.product import Products

Base = declarative_base()

class Order(Base):

    __tablaname__ = 'orders'

    id = Column(Integer, primary_key=True)
    quantity = Column(Integer)
    data = Column(DataTime)
    product_id = Column(Integer, ForeignKey(product.id))
    user_id = Column(Integer)
    products = relationship(
        Products,
        backref = backref(
            'orders',
            uselist=True,
            cascade='delete,all'
        )
    )
    def __str__(self):
        return f"{self.quantity} {self.data}"