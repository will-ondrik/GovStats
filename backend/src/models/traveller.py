from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

# create base class
Base = declarative_base()


"""
ORM model for the Traveller table.

This class represents the travellers that make up a travel expense (travel claims) submitted by a Canadian Member of Parliament.
Each instance of this class corresponds with a row in the table, with attributes that represent the columns in the table.
"""

class Traveller(Base):
    __tablename__ = 'Traveller'

    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column('firstName', String(75), nullable=False)
    last_name = Column('lastName', String(75), nullable=False)
    type = Column(String(100), nullable=False)

    travel = relationship('Travel', back_populates='traveller')
    
    def __repr__(self):
        return (
            f'<Traveller(id={self.id}, first_name={self.first_name}, last_name={self.last_name}, type={self.type})>'
        )