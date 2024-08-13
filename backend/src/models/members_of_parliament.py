from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

# create base class
Base = declarative_base()

"""
ORM model for the MembersOfParliament table.

This class represents members of the Canadian Parliament and maps to the 'MembersOfParliament' table in the database.
Each instance of this class corresponds to a row in the table, with attributes that represent the columns in the table.

"""
class MembersOfParliament(Base):

    __tablename__ = 'MembersOfParliament'

    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column('firstName', String(50), nullable=False)
    last_name = Column('lastName', String(50), nullable=False)
    constituency = Column(String(75), nullable=False)
    caucus = Column(String(25), nullable=False)

    def __repr__(self):
        return f'<MembersOfParliament(id={self.id}, first_name={self.first_name}, last_name={self.last_name}, constituency={self.constituency}, caucus={self.caucus})>'
    

    # SQL Queries
    @classmethod
    def get_by_caucus(cls, session, caucus_name):
        """Retrieve all members from a specific caucus."""
        return session.query(cls).filter_by(caucus=caucus_name).all()
    
    @classmethod
    def get_by_constituency(cls, session, constituency_name):
        """Retrieve member(s) from a specific constituency."""
        return session.query(cls).filter_by(constituency=constituency_name).all()
    

    @classmethod
    def get_all_members(cls, session):
        """Retrieves all members of parliament (current and past)."""
        return session.query(cls).all()
    
    @classmethod
    def get_by_last_name(cls, session, mp_last_name):
        """Retrieves member(s) by their last name."""
        return session.query(cls).filter_by(last_name=mp_last_name).all()

    @classmethod
    def get_by_first_name(cls, session, mp_first_name):
        """Retrieves member(s) of parliament by their first name."""
        return session.query(cls).filter_by(first_name=mp_first_name).all()