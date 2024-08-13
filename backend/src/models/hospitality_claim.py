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
    expense = relationship('Expense', back_populates='hospitality_claim')

    # defines a relationship to the MembersOfParliament model, allowing access to the related MP object via 'member'
    member = relationship('MembersOfParliament', back_populates='hospitality_claim')

    event = relationship('Event', back_populates='hospitality_claim')


    def __repr__(self):
        return (
            f'<HospitalityClaim(id={self.id}, expense_id={self.expense_id}, member_id={self.member_id}, '
            f'date={self.date}, location={self.location}, attendance={self.attendance}, purpose={self.purpose}, '
            f'total_cost={self.total_cost})>'
        )
    
    @classmethod
    def get_all_hospitality_expenses(cls, session):
        """Retrieves all entries from the HospitalityClaim table."""
        return session.query(cls).all()
    
    @classmethod
    def get_all_hospitality_expenses_by_expense_id(cls, session, expenseId):
        """Retrieves all entries from the HospitalityClaim table by expense id."""
        return session.query(cls).filter_by(expense_id=expenseId).all()
    

    @classmethod
    def get_all_hospitality_expenses_by_member_id(cls, session, memberId):
        """Retrieves all entries from the HospitalityClaim table by member id."""
        return session.query(cls).filter_by(member_id=memberId).all()
    
    @classmethod
    def get_all_hospitality_expenses_by_date(cls, session, selected_date):
        """Retrieves all entries from the HospitalityClaim table on a specified date."""
        return session.query(cls).filter_by(date=selected_date).all()
    
    @classmethod
    def get_all_hospitality_expeneses_by_purpose(cls, session, hospitality_purpose):
        """Retrieves all entries from the HospitalityClaim table by purpose."""
        return session.query(cls).filter_by(purpose=hospitality_purpose).all()