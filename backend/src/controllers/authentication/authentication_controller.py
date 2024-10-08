from flask import jsonify
from src.abstract.abstract_controller import AbstractController
from src.services.authentication.authentication_service import AuthenticationService

class AuthenticationController(AbstractController):
    def __init__(self):
        super().__init__('auth')
        self.initialize_routes()
        self.authentication_service = AuthenticationService()

    
    def initialize_routes(self):
        """
        This function initializes all controller endpoints.
        The authentication service file handles all of the interactions with the endpoints.
        """
        self.blueprint.add_url_rule('/delete-account', 'delete', methods=['POST'])
        self.blueprint.add_url_rule('/login', 'login', methods=['POST'])
        self.blueprint.add_url_rule('/logout', 'logout', methods=['POST'])
        self.blueprint.add_url_rule('/register', 'register', methods=['POST'])
        self.blueprint.add_url_rule('reset-password', 'reset_password', methods=['POST'])
        self.blueprint.add_url_rule('/validate', 'validate', methods=['GET'])
        self.blueprint.add_url_rule('/verify-email', 'verify_email', methods=['POST'])