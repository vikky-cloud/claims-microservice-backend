from sqlalchemy import Column, Integer, Float, Date, ForeignKey, String
from sqlalchemy.orm import relationship
from app import db

class Policy(db.Model):
    __tablename__ = 'policies'

    policy_number = db.Column(db.String(50), primary_key=True)
    policy_limit = db.Column(db.Integer, nullable=False)
    deductible = db.Column(db.Float, nullable=False)
    expiration_date = db.Column(db.Date, nullable=False)
    customer_number = db.Column(db.String(50), db.ForeignKey('customers.customer_number'), nullable=False)
    VIN = db.Column(db.String(50), db.ForeignKey('vehicles.VIN'), nullable=False)

    # Relationships
    customer = relationship('Customer', back_populates='policies')
    vehicle = relationship('Vehicle', back_populates='policies')
    claims = relationship('Claim', back_populates='policy')
