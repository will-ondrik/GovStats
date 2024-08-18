from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship

# create base class
Base = declarative_base()

"""
ORM model for the ParliamentaryAssociationsAndInterparliamentaryGroups table.

This class represents the different Parliamentary and Interparliamentary groups and associations of Members of the Canadian Parliament.
Each instance of this class corresponds to a row in the table, with attributes that represent the columns in the table.
"""

class ParliamentaryAssociationsAndInterparliamentaryGroups(Base):
    __tablename__ = 'ParliamentaryAssociationsAndInterparliamentaryGroups'

    id = Column(Integer, primary_key=True, autoincrement=True)
    member_id = Column('memberId', ForeignKey('MembersOfParliament.id'), nullable=False)
    name = Column(String(512), nullable=False)
    abbreviation = Column(String(15), nullable=False)
    executive_committee = Column('executiveCommittee', Boolean, nullable=False)

    member = relationship('MembersOfParliament', back_populates='parliamentary_associations_and_interparliamentary_groups')


    def __repr__(self):
        return (
            f'<ParliamentaryAssociationsAndInterparliamentaryGroups(id={self.id}, member_id={self.member_id}, name={self.name} ,'
            f'abbreviation={self.abbreviation}, executive_committee={self.executive_committee})>'
        )