from abc import ABC, abstractmethod
from flask import Blueprint

class Abstract_Controller(ABC):

    def __init__(self, base_path):
        self.base_path = base_path
        self.blueprint = Blueprint(base_path, __name__, url_prefix=f'/{base_path}')


    @abstractmethod
    def initialize_routes(self):
        """
        Abstract method to initialize controller routes.
        Derived classes must implement this method.
        """
        pass