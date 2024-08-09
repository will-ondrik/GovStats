from src.abstract.abstract_controller import Abstract_Controller
from src.services.party.party_service import Party_Service

class Party_Controller(Abstract_Controller):
    def __init__(self):
        super().__init__('party')
        self.initialize_routes
        self.party_service = Party_Service()

    def initialize_routes(self):
        self.blueprint.add_url_rule('/<string:party>', 'get_all_members_party', methods=['GET'])
        self.blueprint.add_url_rule('/<string:party>/<int:year>/<int:quarter>', 'get_members_party_by_year_and_quarter', methods=['GET'])
        self.blueprint.add_url_rule('/<string:party>/<int:year>/<string:month>', 'get_members_party_by_year_and_month', methods=['GET'])
        self.blueprint.add_url_rule('/<string:party>/travel/<int:year>', 'get_all_members_travel_party_by_year', methods=['GET'])
        self.blueprint.add_url_rule('/<string:party>/travel/<int:year>/<int:quarter>','get_members_travel_party_by_year_and_quarter', methods=['GET'])
        self.blueprint.add_url_rule('/<string:party>/travel/<int:year>/<string:month>', 'get_members_party_by_year_and_month', methods=['GET'])
        self.blueprint.add_url_rule('/<string:party>/hospitality/<int:year>', 'get_all_members_travel_party_by_year', methods=['GET'])
        self.blueprint.add_url_rule('/<string:party>/hospitality/<int:year>/<int:quarter>','get_members_travel_party_by_year_and_quarter', methods=['GET'])
        self.blueprint.add_url_rule('/<string:party>/hospitality/<int:year>/<string:month>', 'get_members_party_by_year_and_month', methods=['GET'])
        self.blueprint.add_url_rule('/<string:party>/contract/<int:year>', 'get_all_members_travel_party_by_year', methods=['GET'])
        self.blueprint.add_url_rule('/<string:party>/contract/<int:year>/<int:quarter>','get_members_travel_party_by_year_and_quarter', methods=['GET'])
        self.blueprint.add_url_rule('/<string:party>/contract/<int:year>/<string:month>', 'get_members_party_by_year_and_month', methods=['GET'])
        self.blueprint.add_url_rule('/expenses/salary/<int:year>', 'get_all_party_travel_expenses_by_year', methods=['GET'])
        self.blueprint.add_url_rule('/expenses/salary/<int:year>/<int:quarter>','get_party_travel_expenses_by_year_and_quarter', methods=['GET'])
        self.blueprint.add_url_rule('/expenses/salary/<int:year>/<string:month>', 'get_party_expenses_by_year_and_month', methods=['GET'])
