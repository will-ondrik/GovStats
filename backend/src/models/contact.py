from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

# create base class
Base = declarative_base()

"""
ORM for the contact table.

This class represents the contact information for the Canadian Parliament's House of Common members and maps to the 'Contact' table in the database.
Each instance of this class corresponds to a row in the table, with attributes that represent the columns in the table.
"""

class Contact(Base):
    __tablename__ = 'Contact'

    id = Column(Integer, primary_key=True, autoincrement=True)
    member_id = Column('memberId', Integer, ForeignKey('MembersOfParliament.id'), nullable=False)
    email = Column(String(128), nullable=False)
    website = Column(String(128), nullable=True)
    hill_office_address = Column('hillOfficeAddress', String(255), nullable=True)
    hill_office_phone = Column('hillOfficePhone', String(15), nullable=True)
    hill_office_fax = Column('hillOfficeFax', String(15), nullable=True)
    constituency_office_address = Column('constituencyOfficeAddress', String(255), nullable=True)
    constituency_office_phone = Column('constituencyOfficeAddress', String(15), nullable=True)
    constituency_office_fax = Column('constituencyOfficeAddress', String(15), nullable=True)
    link_to_site = Column('linkedToSite', String(128), nullable=True)

    
    # defines a relationship to the 'MembersOfParliament' model, allowing access to the related MP object via 'member'
    member = relationship('MembersOfParliament', back_populates='contract')


    def __repr__(self):
        return (
            f'<Contact(id={self.id}, member_id={self.member_id}, email={self.email}, '
            f'website={self.website}, hill_office_address={self.hill_office_address}, hill_office_phone={self.hill_office_phone}, '
            f'hill_office_fax={self.hill_office_fax}, constituency_office_address={self.constituency_office_address}, '
            f'constituency_office_phone={self.constituency_office_phone}, constituency_office_fax={self.constituency_office_fax}, '
            f'link_to_site={self.link_to_site})>'
        )