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
    

    @classmethod
    def get_all_travel(cls, session):
        """Retrieves all entries from the Travel table."""
        return session.query(cls).all()
    
    @classmethod
    def get_all_travel_by_traveller_id(cls, session, travellerId):
        """Retrieves all entries from the Travel table by traveller id."""
        return session.query(cls).filter_by(traveller_id=travellerId).all()
    
    @classmethod
    def get_all_travel_by_travel_claim_id(cls, session, claimId):
        """Retrieves all entries from the Travel table by TravelClaim id."""
        return session.query(cls).filter_by(claim_id=claimId).all()
    
    @classmethod
    def get_all_travel_by_departure(cls, session, departure_location):
        """Retrieves all entries from the Travel table by departure location."""
        return session.query(cls).filter_by(departure=departure_location).all()
    

    @classmethod
    def get_all_travel_by_destination(cls, session, destination_location):
        """Retrieves all entries from the Travel table by destination location."""
        return session.query(cls).filter_by(destination=destination_location).all()
    

    @classmethod
    def get_all_travel_by_purpose(cls, session, travel_purpose):
        """Retrieves all entries from the Travel table by travel purpose."""
        return session.query(cls).filter_by(purpose=travel_purpose).all()