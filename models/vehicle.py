from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from app import db


class Vehicle(db.Model):
    __tablename__ = 'vehicles'
    
    VIN = db.Column(db.String(50), primary_key=True)  # Assuming VIN is the primary key
    model_year = db.Column(db.Integer, nullable=False)  # No size argument
    car_type_id = db.Column(db.Integer, db.ForeignKey('car_types.car_type_id'), nullable=False)

    # Relationships
    car_type = relationship('CarType', back_populates='vehicles')
    policies = relationship('Policy', back_populates='vehicle')
