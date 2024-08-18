"""
This class provides methods for retrieving contract expenses related to the House of Commons,
Caucuses, Constituencies, and Members of Parliament.

Each method allows for filtering contract expenses based on various criteria such as 
the Member of Parliament's ID, caucus, constituency, year, quarter, supplier, and contract purpose. 
These methods encapsulate the business logic for querying the ContractClaim table and 
its relationships with other tables, ensuring that only the relevant data is returned.
"""
class ContractClaimService:

    def __init__(self, session):
        self.session = session

    """
    1) House of Commons

    The following functions return contract expenses for the House of Commons, allowing for
    filtering by various criteria such as year, quarter, supplier, and purpose.
    """
    @classmethod
    def get_all_contract_expenses_by_house(cls, session):
        """Retrieves all contract expenses for the House of Commons."""
        return session.query(cls).all()
    
    @classmethod
    def get_contract_expenses_by_house_in_year(cls, session, year):
        """Retrieves all contract expenses for the House of Commons for a specified year."""
        return session.query(cls)\
                      .join(cls.year == year)\
                      .all()
    
    @classmethod
    def get_contract_expenses_by_house_in_year_by_quarter(cls, session, year, quarter):
        """Retrieves all contract expenses for the House of Commons by year and fiscal quarter."""
        return session.query(cls)\
                      .join(cls.member)\
                      .filter(cls.year == year)\
                      .filter(cls.quarter == quarter)\
                      .all()
    
    @classmethod
    def get_contract_expenses_by_house_and_supplier(cls, session, supplier):
        """Retrieves contract expenses by supplier for a specified Member of Parliament."""
        return session.query(cls)\
                      .join(cls.member)\
                      .filter(cls.expense.has(supplier=supplier))\
                      .all()
    
    @classmethod
    def get_contract_expenses_by_house_in_year_with_supplier(cls, session, supplier, year):
        """Retrieves contract expenses by year and supplier for a specified Member of Parliament."""
        return session.query(cls)\
                      .join(cls.member)\
                      .filter(supplier=supplier)\
                      .filter(year=year)\
                      .all()
    
    @classmethod
    def get_contract_expenses_by_house_in_year_and_quarter_with_supplier(cls, session, supplier, year, quarter):
        """Retrives contract expenses by year and quarter with supplier for a specified Member of Parliament."""
        return session.query(cls)\
                      .join(cls.member)\
                      .filter(supplier=supplier)\
                      .filter(year=year)\
                      .filter(quarter=quarter)\
                      .all()
                      
    @classmethod
    def get_contract_expenses_by_house_by_purpose(cls, session, purpose):
        """Retrieves contract expenses by contract purpose for a specified Member of Parliament."""
        return session.query(cls)\
                      .join(cls.member)\
                      .filter(purpose=purpose)\
                      .all()
    
    @classmethod
    def get_contract_expenses_by_house_in_year_with_purpose(cls, session, purpose, year):
        """Retrives contract expenses by year with purpose."""
        return session.query(cls)\
                      .join(cls.member)\
                      .filter(year=year)\
                      .filter(purpose=purpose)\
                      .all()

    @classmethod
    def get_contract_expenses_by_house_in_year_and_quarter_with_purpose(cls, session, purpose, year, quarter):
        """Retrives contract expenses by year and quarter with purpose."""
        return session.query(cls)\
                      .join(cls.member)\
                      .filter(year=year)\
                      .filter(quarter=quarter)\
                      .filter(purpose=purpose)\
                      .all()

    """
    2) Caucuses
    
    The following functions return contract expenses for caucuses, allowing for filtering by 
    various criteria such as year, quarter, supplier, and purpose.
    """
    @classmethod
    def get_all_contract_expenses_by_caucus(cls, session, caucus):
        """Retrieves contract expenses for a specific Member of Parliament from the ContractClaim table."""
        return session.query(cls)\
                      .join(cls.member)\
                      .filter(cls.caucus == caucus)\
                      .all()
    
    @classmethod 
    def get_contract_expenses_by_caucus_in_year(cls, session, caucus, year):
        """Retrieves a specified year of contract expenses for a Member of Parliament."""
        return session.query(cls)\
                      .join(cls.member)\
                      .filter(cls.caucus == caucus)\
                      .filter(cls.expense.has(year=year))\
                      .all()

    @classmethod
    def get_contract_expenses_by_caucus_in_year_by_quarter(cls, session, caucus, year, quarter):
        """Retrieves contract expenses for a specified year's quarter for a Member of Parliament."""
        return session.query(cls)\
                      .join(cls.member)\
                      .filter(cls.caucus == caucus)\
                      .filter(cls.expense.has(year=year))\
                      .filter(cls.expense.has(quarter=quarter))\
                      .all()
    
    @classmethod
    def get_contract_expenses_by_caucus_and_supplier(cls, session, supplier, caucus):
        """Retrieves contract expenses by supplier for a specified Member of Parliament."""
        return session.query(cls)\
                      .join(cls.member)\
                      .filter(cls.caucus == caucus)\
                      .filter(cls.expense.has(supplier=supplier))\
                      .all()
    
    @classmethod
    def get_contract_expenses_by_caucus_in_year_with_supplier(cls, session, supplier, caucus, year):
        """Retrieves contract expenses by year and supplier for a specified Member of Parliament."""
        return session.query(cls)\
                      .join(cls.member)\
                      .filter(cls.caucus == caucus)\
                      .filter(supplier=supplier)\
                      .filter(year=year)\
                      .all()
    
    @classmethod
    def get_contract_expenses_by_caucus_in_year_and_quarter_with_supplier(cls, session, caucus, supplier, year, quarter):
        """Retrives contract expenses by year and quarter with supplier for a specified Member of Parliament."""
        return session.query(cls)\
                      .join(cls.member)\
                      .filter(cls.caucus == caucus)\
                      .filter(supplier=supplier)\
                      .filter(year=year)\
                      .filter(quarter=quarter)\
                      .all()
                      
    @classmethod
    def get_contract_expenses_by_caucus_by_purpose(cls, session, purpose, caucus):
        """Retrieves contract expenses by contract purpose for a specified Member of Parliament."""
        return session.query(cls)\
                      .join(cls.member)\
                      .filter(cls.caucus == caucus)\
                      .filter(purpose=purpose)\
                      .all()
    
    @classmethod
    def get_contract_expenses_by_caucus_in_year_with_purpose(cls, session, purpose, year, caucus):
        """Retrives contract expenses by year with purpose."""
        return session.query(cls)\
                      .join(cls.member)\
                      .filter(cls.caucus == caucus)\
                      .filter(year=year)\
                      .filter(purpose=purpose)\
                      .all()

    @classmethod
    def get_contract_expenses_by_caucus_in_year_and_quarter_with_purpose(cls, session, purpose, year, quarter, caucus):
        """Retrives contract expenses by year and quarter with purpose."""
        return session.query(cls)\
                      .join(cls.member)\
                      .filter(cls.caucus == caucus)\
                      .filter(year=year)\
                      .filter(quarter=quarter)\
                      .filter(purpose=purpose)\
                      .all()


    """
    3) Constituencies
    
    The following functions return contract expenses for constituencies, filtered by 
    various criteria such as year, quarter, supplier, and purpose.
    """
    @classmethod
    def get_all_contract_expenses_by_mp(cls, session, constituency):
        """Retrieves contract expenses for a specific Member of Parliament from the ContractClaim table."""
        return session.query(cls)\
                      .join(cls.member)\
                      .filter(cls.constituency == constituency)\
                      .all()
    
    @classmethod 
    def get_contract_expenses_by_constituency_in_year(cls, session, constituency, year):
        """Retrieves a specified year of contract expenses for a Member of Parliament."""
        return session.query(cls)\
                      .join(cls.member)\
                      .filter(cls.constituency == constituency)\
                      .filter(cls.expense.has(year=year))\
                      .all()

    @classmethod
    def get_contract_expenses_by_constituency_in_year_by_quarter(cls, session, constituency, year, quarter):
        """Retrieves contract expenses for a specified year's quarter for a Member of Parliament."""
        return session.query(cls)\
                      .join(cls.member)\
                      .filter(cls.constituency == constituency)\
                      .filter(cls.expense.has(year=year))\
                      .filter(cls.expense.has(quarter=quarter))\
                      .all()
    
    @classmethod
    def get_contract_expenses_by_constituecy_and_supplier(cls, session, supplier, constituency):
        """Retrieves contract expenses by supplier for a specified Member of Parliament."""
        return session.query(cls)\
                      .join(cls.member)\
                      .filter(cls.constituency == constituency)\
                      .filter(cls.expense.has(supplier=supplier))\
                      .all()
    
    @classmethod
    def get_contract_expenses_by_constituency_in_year_with_supplier(cls, session, supplier, constituency, year):
        """Retrieves contract expenses by year and supplier for a specified Member of Parliament."""
        return session.query(cls)\
                      .join(cls.member)\
                      .filter(cls.constituency == constituency)\
                      .filter(supplier=supplier)\
                      .filter(year=year)\
                      .all()
    
    @classmethod
    def get_contract_expenses_by_constituency_in_year_and_quarter_with_supplier(cls, session, constituency, supplier, year, quarter):
        """Retrives contract expenses by year and quarter with supplier for a specified Member of Parliament."""
        return session.query(cls)\
                      .join(cls.member)\
                      .filter(cls.constituency == constituency)\
                      .filter(supplier=supplier)\
                      .filter(year=year)\
                      .filter(quarter=quarter)\
                      .all()
                      
    @classmethod
    def get_contract_expenses_by_constituency_by_purpose(cls, session, purpose, constituency):
        """Retrieves contract expenses by contract purpose for a specified Member of Parliament."""
        return session.query(cls)\
                      .join(cls.member)\
                      .filter(cls.constituency == constituency)\
                      .filter(purpose=purpose)\
                      .all()
    
    @classmethod
    def get_contract_expenses_by_constituency_in_year_with_purpose(cls, session, purpose, year, constituency):
        """Retrives contract expenses by year with purpose."""
        return session.query(cls)\
                      .join(cls.member)\
                      .filter(cls.constituency == constituency)\
                      .filter(year=year)\
                      .filter(purpose=purpose)\
                      .all()

    @classmethod
    def get_contract_expenses_by_constituency_in_year_and_quarter_with_purpose(cls, session, purpose, year, quarter, constituency):
        """Retrives contract expenses by year and quarter with purpose."""
        return session.query(cls)\
                      .join(cls.member)\
                      .filter(cls.constituency == constituency)\
                      .filter(year=year)\
                      .filter(quarter=quarter)\
                      .filter(purpose=purpose)\
                      .all()
    
    """
    4) Members of Parliament

    The following functions return contract expenses for Members of Parliament, filtered by 
    various criteria such as year, quarter, supplier, and purpose.
    """
    @classmethod
    def get_all_contract_expenses_by_mp(cls, session, mp_id):
        """Retrieves contract expenses for a specific Member of Parliament from the ContractClaim table."""
        return session.query(cls)\
                      .join(cls.member)\
                      .filter(cls.member_id == mp_id)\
                      .all()
    
    @classmethod 
    def get_contract_expenses_by_mp_in_year(cls, session, mp_id, year):
        """Retrieves a specified year of contract expenses for a Member of Parliament."""
        return session.query(cls)\
                      .join(cls.member)\
                      .filter(cls.member_id == mp_id)\
                      .filter(cls.expense.has(year=year))\
                      .all()

    @classmethod
    def get_contract_expenses_by_mp_in_year_by_quarter(cls, session, mp_id, year, quarter):
        """Retrieves contract expenses for a specified year's quarter for a Member of Parliament."""
        return session.query(cls)\
                      .join(cls.member)\
                      .filter(cls.member_id == mp_id)\
                      .filter(cls.expense.has(year=year))\
                      .filter(cls.expense.has(quarter=quarter))\
                      .all()
    
    @classmethod
    def get_contract_expenses_by_mp_and_supplier(cls, session, supplier, mp_id):
        """Retrieves contract expenses by supplier for a specified Member of Parliament."""
        return session.query(cls)\
                      .join(cls.member)\
                      .filter(cls.member_id == mp_id)\
                      .filter(cls.expense.has(supplier=supplier))\
                      .all()
    
    @classmethod
    def get_contract_expenses_by_mp_in_year_with_supplier(cls, session, supplier, mp_id, year):
        """Retrieves contract expenses by year and supplier for a specified Member of Parliament."""
        return session.query(cls)\
                      .join(cls.member)\
                      .filter(cls.member_id == mp_id)\
                      .filter(supplier=supplier)\
                      .filter(year=year)\
                      .all()
    
    @classmethod
    def get_contract_expenses_by_mp_in_year_and_quarter_with_supplier(cls, session, mp_id, supplier, year, quarter):
        """Retrives contract expenses by year and quarter with supplier for a specified Member of Parliament."""
        return session.query(cls)\
                      .join(cls.member)\
                      .filter(cls.member_id == mp_id)\
                      .filter(supplier=supplier)\
                      .filter(year=year)\
                      .filter(quarter=quarter)\
                      .all()
                      
    @classmethod
    def get_contract_expenses_by_mp_by_purpose(cls, session, purpose, mp_id):
        """Retrieves contract expenses by contract purpose for a specified Member of Parliament."""
        return session.query(cls)\
                      .join(cls.member)\
                      .filter(cls.member_id == mp_id)\
                      .filter(purpose=purpose)\
                      .all()
    
    @classmethod
    def get_contract_expenses_by_mp_in_year_with_purpose(cls, session, purpose, year, mp_id):
        """Retrives contract expenses by year with purpose."""
        return session.query(cls)\
                      .join(cls.member)\
                      .filter(cls.member_id == mp_id)\
                      .filter(year=year)\
                      .filter(purpose=purpose)\
                      .all()

    @classmethod
    def get_contract_expenses_by_mp_in_year_and_quarter_with_purpose(cls, session, purpose, year, quarter, mp_id):
        """Retrives contract expenses by year and quarter with purpose."""
        return session.query(cls)\
                      .join(cls.member)\
                      .filter(cls.member_id == mp_id)\
                      .filter(year=year)\
                      .filter(quarter=quarter)\
                      .filter(purpose=purpose)\
                      .all()
