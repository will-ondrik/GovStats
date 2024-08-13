from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, Date, String, Text, ForeignKey
from sqlalchemy.orm import relationship

# create base class
Base = declarative_base()


"""
ORM model for the Travel table.

This class represents travel entries (associated with travel claims and travellers) for a Canadian Member of Parliament. 
Each instance of this class corresponds with a row in the table, with attributes that represent the columns in the table.
"""

class Travel(Base):
    __tablename__ = 'Travel'

    id = Column(Integer, primary_key=True, autoincrement=True)
    traveller_id = Column('travellerId', Integer, ForeignKey('Traveller.id'), nullable=False)
    claim_id = Column('claimId', Integer, ForeignKey('TravelClaim.id'), nullable=False)
    date = Column(Date, nullable=True)
    departure = Column(String(255), nullable=True)
    destination = Column(String(255), nullable=True)
    purpose = Column(Text, nullable=False)

    # defines a relationship to the Traveller model, allowing access to the related Traveller object via 'traveller'
    traveller = relationship('Traveller', back_populates='travel')

    # defines a relationship to the TravelClaim model, allowing access to the related TravelClaim object via 'claim'
    claim = relationship('TravelClaim', back_populates='travel')


    def __repr__(self):
        return (
            f'<Travel(id={self.id}, traveller_id={self.traveller_id}, claim_id={self.claim_id}, date={self.date}, '
            f'departure={self.departure}, destination={self.destination}, purpose={self.purpose})>'
        )