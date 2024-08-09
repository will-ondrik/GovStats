from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

# create base class
Base = declarative_base()

"""
ORM model for the MembersOfParliament table.

This class represents members of the Canadian Parliament and maps to the 'MembersOfParliament' table in the database.
Each instance of this class corresponds to a row in the table, with attributes that represent the columns in the table.

"""
class MemberOfParliament(Base):

    __tablename__ = 'MembersOfParliament'

    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column('firstName', String(50), nullable=False)
    last_name = Column('lastName', String(50), nullable=False)
    constituency = Column(String(75), nullable=False)
    caucus = Column(String(25), nullable=False)

    def __repr__(self):
        return f'<MembersOfParliament(id={self.id}, first_name={self.first_name}, last_name={self.last_name}, constiuency={self.constituency}, caucas={self.caucus}>'