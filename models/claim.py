from sqlalchemy import Column, Integer, Float, Date, ForeignKey
from sqlalchemy.orm import relationship
from app import db

class Claim(db.Model):
    __tablename__ = 'claims'
    
    claim_number = db.Column(db.Integer, primary_key=True, autoincrement=True)
    amount = db.Column(db.Float, nullable=False)
    claim_date = db.Column(db.Date, nullable=False)
    policy_number = db.Column(db.String(50), db.ForeignKey('policies.policy_number'), nullable=False)
    status_id = db.Column(db.Integer, db.ForeignKey('statuses.status_id'), nullable=False)

    # Relationships
    policy = relationship('Policy', back_populates='claims')
    status = relationship('Status', back_populates='claims')
