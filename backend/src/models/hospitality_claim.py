from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, Date, Text, String, Float, ForeignKey
from sqlalchemy.orm import relationship

# create base class
Base = declarative_base()

"""
ORM model for the HospitalityClaim table.

This class represents hospitality expenses (hospitality claims) for a Canadian Member of Parliament. 
Each instance of this class corresponds with a row in the table, with attributes that represent the columns in the table.
"""

class HospitalityClaim(Base):
    __tablename__ = 'HospitalityClaim'

    id = Column(Integer, primary_key=True, autoincrement=True)
    expense_id = Column('expenseId', Integer, ForeignKey('Expense.id'), nullable=False)
    member_id = Column('memberId', Integer, ForeignKey('MembersOfParliament.id'), nullable=False)
    date = Column(Date, nullable=False)
    location = Column(String, nullable=False)
    attendance = Column(Integer, nullable=False)
    purpose = Column(Text, nullable=False)
    total_cost = Column('totalCost', Float, nullable=False)

    # defines a relationship to the Expense model, allowing access to the related Expense object via 'expense'
    expense = relationship('Expense', back_populates='travel_claim')

    # defines a relationship to the MembersOfParliament model, allowing access to the related MP object via 'member'
    member = relationship('MembersOfParliament', back_populates='travel_claim')


    def __repr__(self):
        return (
            f'<HospitalityClaim(id={self.id}, expense_id={self.expense_id}, member_id={self.member_id}, '
            f'date={self.date}, location={self.location}, attendance={self.attendance}, purpose={self.purpose}, '
            f'total_cost={self.total_cost})>'
        )