from clients.employee.base_client import BaseClient
from config import BASE_URI
from utils.request import APIRequest


class EmployeeClient(BaseClient):
    def __init__(self):
        super().__init__()

        self.base_url = BASE_URI
        self.request = APIRequest

    def get_all_employees(self):
        return self.request.get(self, self.base_url)