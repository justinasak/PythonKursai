from sqlalchemy import Column, Integer, String, Float, DateTime, create_engine
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///macros.db')
Base = declarative_base()

class Goal(Base):
    __tablename__ = 'Goal'
    id = Column(Integer, primary_key=True)
    bmr = Column('bmr', Float)

    def __init__(self, bmr):
        self.bmr = bmr

    def __repr__(self):
        return f"{self.id}"

Base.metadata.create_all(engine)