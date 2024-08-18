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
    
    event = relationship('HospitalityClaim', back_populates='event')

    @classmethod
    def get_all_event_expenses(cls, session):
        """Retrieves all entries from the Event table."""
        return session.query(cls).all()
    
    @classmethod
    def get_all_event_expenses_by_claim_id(cls, session, hospitality_claim_id):
        """Retrieves all entries from the Event table associated with a HospitalityClaim id."""
        return session.query(cls).filter_by(claim_id=hospitality_claim_id).all()
    
    @classmethod
    def get_all_event_expenses_by_claim_number(cls, session, claim_num):
        """Retrieves all entries from the Event table by claim number."""
        return session.query(cls).filter_by(claim_number=claim_num).all()

    @classmethod
    def get_all_event_expenses_by_type(cls, session, event_type):
        """Retrieves all entries from the Event table by Event type."""
        return session.query(cls).filter_by(type=event_type).all()
    
    @classmethod
    def get_all_event_expenses_by_supplier(cls, session, event_supplier):
        """Retrieves all entries from the Event table by supplier."""
        return session.query(cls).filter_by(supplier=event_supplier).all()