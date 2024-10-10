from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app import db


class CarType(db.Model):
    __tablename__ = 'car_types'
    
    car_type_id = db.Column(db.Integer, primary_key=True, autoincrement=True)  # No size argument
    car_make = db.Column(db.String(50), nullable=False)
    car_model = db.Column(db.String(50), nullable=False)

    # Relationships
    vehicles = relationship('Vehicle', back_populates='car_type')
