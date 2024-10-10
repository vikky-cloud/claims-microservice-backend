from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app import db

class Status(db.Model):
    __tablename__ = 'statuses'

    status_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    status = db.Column(db.String(30), nullable=False)

    # Relationships
    claims = relationship('Claim', back_populates='status')
