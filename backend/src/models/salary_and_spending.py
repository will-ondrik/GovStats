from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship

# create base class
Base = declarative_base()

"""
ORM model for the SalaryAndSepending table.

This class represents the yearly salary and expenses of each member of the Canadian Parliament and maps to the 'SalaryAndSpending' table in the database.
Each instance of this class corresponds to a row in the table, with attributes that represent the columns in the table.
"""

class SalaryAndSpending(Base):
    __tablename__ = 'SalaryAndSpending'

    id = Column(Integer, primary_key=True, autoincrement=True)
    member_id = Column('memberId', Integer, ForeignKey('MembersOfParliament.id'), nullable=False)
    member_name = Column('memberName', String(75), nullable=False)
    year = Column(Integer, nullable=False)
    salary = Column(Float, nullable=False)
    travel_expenses = Column('travelExpenses', nullable=True)
    hospitality_expenses = Column('hospitalityExpenses', nullable=True)
    contract_expenses = Column('contractExpenses', nullable=True)

    # defines a relationship to the MembersOfParliament model, allowing access to the related MP object via 'member'
    member = relationship('MembersOfParliament', back_populates='salary_and_spending')

    def __repr__(self):
        return (
            f'<SalaryAndSpending(id={self.id}, member_id={self.member_id}, '
            f'member_name={self.member_id}, member_name={self.member_name}, year={self.year}, '
            f'salary={self.salary}, travel_expenses={self.travel_expenses}, '
            f'hospitality_expenses={self.hospitality_expenses}, contract_expenses={self.contract_expenses})>'
        )