from src.abstract.abstract_controller import AbstractController
from src.services.members.members_service import MembersService

class MembersController(AbstractController):
    def __init__(self):
        super().__init__('members')
        self.initialize_routes()
        self.members_service = MembersService()


    def initialize_routes(self):
        self.blueprint.add_url_rule('/<int:mpId>/expenses', 'get_all_members_expenses', methods=['GET'])
        self.blueprint.add_url_rule('/<int:mpId>/expenses/<int:year>', 'get_members_expenses_by_year', methods=['GET'])
        self.blueprint.add_url_rule('/<int:mpId>/expenses/<int:year>/<int:quarter>', 'get_members_expenses_by_year_and_quarter', methods=['GET'])
        self.blueprint.add_url_rule('/<int:mpId>/expenses/travel', 'get_all_members_travel_expenses_yearly')
        self.blueprint.add_url_rule('/<int:mpId>/expenses/travel/<int:year>', 'get_all_members_travel_expenses_by_year', methods=['GET'])
        self.blueprint.add_url_rule('/<int:mpId>/expenses/travel/<int:year>/<int:quarter>','get_members_travel_expenses_by_year_and_quarter', methods=['GET'])
        self.blueprint.add_url_rule('/<int:mpId>/expenses/hospitality/yearly', 'get_all_members_hospitality_expenses_yearly', methods=['GET'])
        self.blueprint.add_url_rule('/<int:mpId>/expenses/hospitality/<int:year>', 'get_all_members_travel_expenses_by_year', methods=['GET'])
        self.blueprint.add_url_rule('/<int:mpId>/expenses/hospitality/<int:year>/<int:quarter>','get_members_travel_expenses_by_year_and_quarter', methods=['GET'])
        self.blueprint.add_url_rule('/<int:mpId>/expenses/contract/yearly', 'get_all_members_contract_expenses_yearly', methods=['GET'])
        self.blueprint.add_url_rule('/<int:mpId>/expenses/contract/<int:year>', 'get_all_members_travel_expenses_by_year', methods=['GET'])
        self.blueprint.add_url_rule('/<int:mpId>/expenses/contract/<int:year>/<int:quarter>','get_members_travel_expenses_by_year_and_quarter', methods=['GET'])
        self.blueprint.add_url_rule('/<int:mpId>/expenses/salary/yearly', 'get_all_members_salaries', methods=['GET'])
        self.blueprint.add_url_rule('/<int:mpId>/expenses/salary/<int:year>', 'get_all_members_travel_expenses_by_year', methods=['GET'])
        self.blueprint.add_url_rule('/<int:mpId>/expenses/salary/<int:year>/<int:quarter>','get_members_travel_expenses_by_year_and_quarter', methods=['GET'])
