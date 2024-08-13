from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey
from sqlalchemy.orm import relationship

# create base class
Base = declarative_base()

class Expense(Base):
    id = Column(Integer, primary_key=True, autoincrement=True)
    member_id = Column('memberId', Integer, ForeignKey('MembersOfParliament.id'), nullable=False)
    claim_type = Column('claimType', String(25), nullable=False)
    cost = Column(Float, nullable=False)
    reporting_period_start = Column('reportingPeriodStart', Date, nullable=False)
    reporting_period_end = Column('reportingPeriodEnd', Date, nullable=False)
    year = Column(Integer, nullable=False)
    fiscal_quarter = Column('fiscalQuarter', Integer, nullable=False)

    # defines a relationship to the MembersOfParliament model, allowing access to the related MP object via 'member'
    member = relationship('MembersOfParliament', back_populates='expense')


    def __repr__(self):
        return (
            f'<Expense(id={self.id}, member_id={self.member_id}, claim_type={self.claim_type}, '
            f'reporting_period_start={self.reporting_period_start}, reporting_period_end={self.reporting_period_end}, '
            f'year={self.year}, fiscal_quarter={self.fiscal_quarter})>'
        )