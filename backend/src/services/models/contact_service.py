class ContactService:

    def __init__(self, session):
        self.session = session

    """
    The following functions return contract expenses for Members of Parliament.
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
