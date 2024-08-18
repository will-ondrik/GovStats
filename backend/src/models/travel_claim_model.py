from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, Date, Float, ForeignKey
from sqlalchemy.orm import relationship

# create base class
Base = declarative_base()


"""
ORM model for the TravelClaim table.

This class represents travel expenses (travel claims) for a Canadian Member of Parliament. 
Each instance of this class corresponds with a row in the table, with attributes that represent the columns in the table.
"""

class TravelClaim(Base):
    __tablename__ = 'TravelClaim'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    expense_id = Column('expenseId', Integer, ForeignKey('Expense.id'), nullable=False)
    member_id = Column('memberId', Integer, ForeignKey('MembersOfParliament.id'), nullable=False)
    start_date = Column('startDate', Date, nullable=True)
    end_date = Column('endDate', Date, nullable=True)
    tranportation_costs = Column('transportationCosts', Float, nullable=False)
    accomodation_costs = Column('accomodationCosts', Float, nullable=False)
    meals_and_incidentals_costs = Column('mealsAndIncidentalsCosts', Float, nullable=False)
    regular_points = Column('regularPoints', Float, nullable=False)
    usa_points = Column('usaPoints', Float, nullable=False)
    total_cost = Column('totalCosts', Float, nullable=False)

    # defines a relationship to the Expense model, allowing access to the related Expense object via 'expense'
    expense = relationship('Expense', back_populates='travel_claim')

    # defines a relationship to the MembersOfParliament model, allowing access to the related MP object via 'member'
    member = relationship('MembersOfParliament', back_populates='travel_claim')


    def __repr__(self):
        return (
            f'<TravelClaim(id={self.id}, expense_id={self.expense_id}, member_id={self.member_id}, '
            f'start_date={self.start_date}, end_date={self.end_date}, transportation_costs={self.tranportation_costs}, '
            f'accomodation_costs={self.accomodation_costs}, meals_and_incidentals_costs={self.meals_and_incidentals_costs}, '
            f'regular_points={self.regular_points}, usa_points={self.usa_points}, total_cost={self.total_cost})>'
        )
    

    @classmethod
    def get_all_travel_expenses(cls, session):
        """Retrieves all entries from the TravelClaim table."""
        return session.query(cls).all()

    @classmethod
    def get_all_travel_expenses_by_departure(cls, session, departure_location):
        """Retrieves all entries from the TravelClaim table by location of departure."""
        return session.query(cls).filter_by(departure=departure_location).all()

    @classmethod
    def get_all_travel_expenses_by_destination(cls, session, destination_location):
        """Retrieves entries from the TravelClaim table by location of destination."""
        return session.query(cls).filter_by(destination=destination_location).all()

    @classmethod
    def get_all_travel_expenses_by_expense_id(cls, session, expenseId):
        """Retrieves entries from the TravelClaim table by expense id."""
        return session.query(cls).filter_by(expense_id=expenseId).all()

    @classmethod
    def get_all_travel_expenses_by_member_id(cls, session, mpId):
        """Retrieves entries from the TravelClaim table by member id."""
        return session.query(cls).filter_by(member_id=mpId).all()