from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Text, Float, ForeignKey
from sqlalchemy.orm import relationship

# create base class
Base = declarative_base()


"""
ORM model for the Event table.

This class represents hospitality expenses (hospitality claims) for a Canadian Member of Parliament. 
Each instance of this class corresponds with a row in the table, with attributes that represent the columns in the table.
"""

class Event(Base):
    __tablename__ = 'Event'

    id = Column(Integer, primary_key=True, autoincrement=True)
    claim_id = Column(Integer, ForeignKey('HospitalityClaim.id'), nullable=False)
    claim_number = Column('claimNumber', String(25), nullable=False)
    type = Column(Text, nullable=False)
    supplier = Column(String(125), nullable=True)
    total_cost = Column('totalCost', Float, nullable=False)

    # defines a relationship to the TravelClaim model, allowing access to the related TravelClaim object via 'claim'
    claim = relationship('HospitalityClaim', back_populates='event')


    def __repr__(self):
        return (
            f'<Event(id={self.id}, claim_id={self.claim_id}, claim_number={self.claim_number}, '
            f'type={self.type}, supplier={self.supplier}, total_cost={self.total_cost})>'
        )