from sqlalchemy import Column, Integer, String, Float, DateTime, create_engine
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///macros.db')
Base = declarative_base()


class Food(Base):
    __tablename__ = 'Food'
    id = Column(Integer, primary_key=True)
    description = Column("Description", String)
    category = Column('Category', Integer)
    kcal = Column('kcal', Float)
    fat = Column('fat', Float)
    carbs = Column('carbs', Float)
    protein = Column('protein', Float)

    def __init__(self, description, category, kcal, fat, carbs, protein, portion):
        self.description = description
        self.category = category
        self.portion = portion/100
        self.kcal = kcal*self.portion
        self.fat = fat*self.portion
        self.carbs = carbs*self.portion
        self.protein = protein*self.portion

    def __repr__(self):
        return f"{self.id}"

Base.metadata.create_all(engine)