from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, Date, Float, String, Text, ForeignKey
from sqlalchemy.orm import relationship

# create base class
Base = declarative_base()


"""
ORM model for the ContractClaim table.

This class represents contract expenses (contract claims) for a Canadian Member of Parliament. 
Each instance of this class corresponds with a row in the table, with attributes that represent the columns in the table.
"""

class ContractClaim(Base):
    __tablename__ = 'ContractClaim'

    id = Column(Integer, primary_key=True, autoincrement=True)
    expense_id = Column('expenseId', Integer, ForeignKey('Expense.id'), nullable=False)
    member_id = Column('memberId', Integer, ForeignKey('MembersOfParliament.id'), nullable=False)
    supplier = Column(String(255), nullable=False)
    date = Column(Date, nullable=False)
    purpose = Column(Text, nullable=False)
    total_cost = Column('totalCost', Float, nullable=False)


    # defines a relationship to the Expense model, allowing access to the related Expense object via 'expense'
    expense = relationship('Expense', back_populates='contract_claim')

    # defines a relationship to the MembersOfParliament model, allowing access to the related MP object via 'member'
    member = relationship('MembersOfParliament', back_populates='contract_claim')


    def __repr__(self):
        return (
            f'<ContractClaim(id={self.id}, expense_id={self.expense_id}, member_id={self.member_id}, '
            f'supplier={self.supplier}, date={self.date}, purpose={self.purpose}, total_cost={self.total_cost})>'
        )
    

    @classmethod
    def get_all_contract_expenses(cls, session):
        """Retrieves all entries from the ContractClaim table."""
        return session.query(cls).all()
    
    @classmethod
    def get_all_contract_expenses_by_expense_id(cls, session, expenseId):
        """Retrieves all entries from the ContractClaim table by expense id."""
        return session.query(cls).filter_by(expense_id=expenseId).all()
    
    @classmethod
    def get_all_contract_expenses_by_member_id(cls, session, mpId):
        """Retrieves all entries from the ContractClaim table by member id."""
        return session.query(cls).filter_by(member_id=mpId).all()
    
    @classmethod
    def get_all_contract_expenses_by_supplier(cls, session, supplier_name):
        """Retrieves all entries from the ContractClaim table by supplier."""
        return session.query(cls).filter_by(supplier=supplier_name).all()
    
    @classmethod
    def get_all_contract_expenses_by_date(cls, session, contract_date):
        """Retrieves all contract expenses by date."""
        return session.query(cls).filter_by(date=contract_date).all()
    
    @classmethod
    def get_all_contract_expenses_by_year(cls, session, year):
        """Retrieves all contract expenses by year."""
        return session.query(cls).filter_by(year=year)

    @classmethod
    def get_all_contract_expenses_by_purpose(cls, session, contract_purpose):
        """Retrieves all entries from the ContractClaim table by contract purpose."""
        return session.query(cls).filter_by(purpose=contract_purpose).all()