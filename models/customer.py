from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app import db

class Customer(db.Model):
    __tablename__ = 'customers'

    customer_number = db.Column(db.String(50), primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    zipcode = db.Column(db.String(50), db.ForeignKey('addresses.zipcode'), nullable=False)

    # Relationships
    address = relationship('Address', back_populates='customers')
    policies = relationship('Policy', back_populates='customer')
