from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from app import db


class Address(db.Model):
    __tablename__ = 'addresses'

    zipcode = db.Column(db.String(50), primary_key=True)
    street_address = db.Column(db.String(50), nullable=False)
    city = db.Column(db.String(50), nullable=False)
    state = db.Column(db.String(50), nullable=False)

    # Relationships
    customers = relationship('Customer', back_populates='address')
