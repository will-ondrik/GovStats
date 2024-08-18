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

    # defines relationships to other models, allowing access to the related objects via variable name
    member = relationship('MembersOfParliament', back_populates='expense')
    travel_claim = relationship('TravelClaim', back_populates='expense')
    contract_claim = relationship('ContractClaim', back_populates='expense')
    hospitality_claim = relationship('HospitalityClaim', back_populates='expense')

    def __repr__(self):
        return (
            f'<Expense(id={self.id}, member_id={self.member_id}, claim_type={self.claim_type}, '
            f'reporting_period_start={self.reporting_period_start}, reporting_period_end={self.reporting_period_end}, '
            f'year={self.year}, fiscal_quarter={self.fiscal_quarter})>'
        )

    @classmethod
    def get_all_expenses(cls, session):
        """Retrieves all entries from the Expense table."""
        return session.query(cls).all()

    @classmethod
    def get_all_expenses_by_year(cls, session, selected_year):
        """Retrieves all entries from the Expense table by year."""
        return session.query(cls).filter_by(year = selected_year).all()
    
    @classmethod
    def get_all_expenses_by_fiscal_quarter(cls, session, quarter):
        """Retrieves all entries from the Expense table by a specified fiscal quarter."""
        return session.query(cls).filter_by(fiscal_quarter=quarter).all()

    @classmethod
    def get_all_expenses_by_year_and_quarter(cls, session, selected_year, quarter):
        """Retrieves all entries from the Expense table by year and fiscal quarter."""
        return session.query(cls).filter_by(year = selected_year).filter_by(fiscal_quarter=quarter).all()

    @classmethod
    def get_all_expenses_by_type(cls, session, type):
        """Retrieves all entries from the Expense table by claim type."""
        return session.query(cls).filter_by(claim_type=type).all()

    @classmethod
    def get_all_expenses_by_memberId(cls, session, mp_id):
        """Retrieves all entries from the Expense table by member id."""
        return session.query(cls).filter_by(member_id=mp_id).all()

    