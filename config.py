import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:password@localhost:3306/claims_microservice'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
