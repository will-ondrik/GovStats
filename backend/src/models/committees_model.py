from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship

# create base class
Base = declarative_base()

"""
ORM model for the Committees table.

This class represents the different committess associated with each of the Members of the Canadian Parliament.
Each instance of this class corresponds to a row in the table, with attributes that represent the columns in the table.
"""

class Committees(Base):
    __tablename__ = 'Committees'

    id = Column(Integer, primary_key=True, autoincrement=True)
    member_id = Column('memberId', ForeignKey('MembersOfParliament.id'), nullable=False)
    name = Column(String(512), nullable=False)
    abbreviation = Column(String(15), nullable=False)

    member = relationship('MembersOfParliament', back_populates='parliamentary_associations_and_interparliamentary_groups')


    def __repr__(self):
        return (
            f'<ParliamentaryAssociationsAndInterparliamentaryGroups(id={self.id}, member_id={self.member_id}, '
            f'name={self.name}, abbreviation={self.abbreviation})>'
        )