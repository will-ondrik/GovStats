from flask import jsonify
from src.abstract.abstract_controller import Abstract_Controller
from src.services.authentication.authentication_service import Authentication_Service

class Authentication_Controller(Abstract_Controller):
    def __init__(self):
        super.__init__('auth')
        self.initialize_routes
        self.authentication_service = Authentication_Service()

    
    def initialize_routes(self):
        self.blueprint.add_url_rule('/delete-account', 'delete', methods=['POST'])
        self.blueprint.add_url_rule('/login', 'login', methods=['POST'])
        self.blueprint.add_url_rule('/logout', 'logout', methods=['POST'])
        self.blueprint.add_url_rule('/register', 'register', methods=['POST'])
        self.blueprint.add_url_rule('reset-password', 'reset_password', methods=['POST'])
        self.blueprint.add_url_rule('/validate', 'validate', methods=['GET'])
        self.blueprint.add_url_rule('/verify-email', 'verify_email', methods=['POST'])