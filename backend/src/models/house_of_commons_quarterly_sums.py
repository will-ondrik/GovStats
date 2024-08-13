from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, Float

# create base class
Base = declarative_base()

"""
ORM for the HouseOfCommonsQuarterlySums table.

This class represents the Canadian Parliament's House of Commons quarterly sums and maps the to 'HouseOfCommonsQuarterlySums' table in the database.
Each instance of this class corresponds to a row in the table, with attributes that represents the columns in the table.
"""

class HouseOfCommonsQuarterlySums(Base):
    __tablename__ = 'HouseOfCommonsQuarterlySums'

    id = Column(Integer, primary_key=True, autoincrement=True)
    year = Column(Integer, nullable=False)
    quarter = Column(Integer, nullable=False)
    salary_total = Column('salaryTotal', Float, nullable=False)
    travel_total = Column('travelTotal', Float, nullable=False)
    hospitality_total = Column('hospitalityTotal', Float, nullable=False)
    contract_total = Column('contractTotal', Float, nullable=False)


    def __repr__(self):
        return (
            f'<HouseOfCommonsQuarterlySums(id={self.id}, year={self.year}, quarter={self.quarter}, '
            f'salary_total={self.salary_total}, travel_total={self.travel_total}, hospitality_total={self.hospitality_total}, '
            f'contract_total={self.contract_total})>'
        )
