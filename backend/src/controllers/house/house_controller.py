from src.abstract.abstract_controller import Abstract_Controller
from src.services.house.house_service import House_Service

class House_Controller(Abstract_Controller):

    def __init__(self):
        super().__init__('house')
        self.initialize_routes
        self.member_service = House_Service()


    def initialize_routes(self):
        self.blueprint.add_url_rule('/expenses', 'get_all_house_expenses', methods=['GET'])
        self.blueprint.add_url_rule('/expenses/<int:year>', 'get_house_expenses_by_year', methods=['GET'])
        self.blueprint.add_url_rule('/expenses/<int:year>/<int:quarter>', 'get_house_expenses_by_year_and_quarter', methods=['GET'])
        self.blueprint.add_url_rule('/expenses/<int:year>/<string:month>', 'get_house_expenses_by_year_and_month', methods=['GET'])
        self.blueprint.add_url_rule('/expenses/travel/yearly', 'get_all_house_travel_yearly', methods=['GET'])
        self.blueprint.add_url_rule('/expenses/travel/<int:year>', 'get_all_house_travel_expenses_by_year', methods=['GET'])
        self.blueprint.add_url_rule('/expenses/travel/<int:year>/<int:quarter>','get_house_travel_expenses_by_year_and_quarter', methods=['GET'])
        self.blueprint.add_url_rule('/expenses/travel/<int:year>/<string:month>', 'get_house_expenses_by_year_and_month', methods=['GET'])
        self.blueprint.add_url_rule('/expenses/hospitality/yearly', 'get_all_house_hospitality', methods=['GET'])
        self.blueprint.add_url_rule('/expenses/hospitality/<int:year>', 'get_all_house_travel_expenses_by_year', methods=['GET'])
        self.blueprint.add_url_rule('/expenses/hospitality/<int:year>/<int:quarter>','get_house_travel_expenses_by_year_and_quarter', methods=['GET'])
        self.blueprint.add_url_rule('/expenses/hospitality/<int:year>/<string:month>', 'get_house_expenses_by_year_and_month', methods=['GET'])
        self.blueprint.add_url_rule('/expenses/contract/yearly', 'get_all_house_contract_yearly', methods=['GET'])
        self.blueprint.add_url_rule('/expenses/contract/<int:year>', 'get_all_house_travel_expenses_by_year', methods=['GET'])
        self.blueprint.add_url_rule('/expenses/contract/<int:year>/<int:quarter>','get_house_travel_expenses_by_year_and_quarter', methods=['GET'])
        self.blueprint.add_url_rule('/expenses/contract/<int:year>/<string:month>', 'get_house_expenses_by_year_and_month', methods=['GET'])
        self.blueprint.add_url_rule('/expenses/salary/yearly', 'get_all_house_salaries_yearly', methods=['GET'])
        self.blueprint.add_url_rule('/expenses/salary/<int:year>', 'get_all_house_travel_expenses_by_year', methods=['GET'])
        self.blueprint.add_url_rule('/expenses/salary/<int:year>/<int:quarter>','get_house_travel_expenses_by_year_and_quarter', methods=['GET'])
        self.blueprint.add_url_rule('/expenses/salary/<int:year>/<string:month>', 'get_house_expenses_by_year_and_month', methods=['GET'])


