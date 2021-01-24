import requests
from assertpy import assert_that

from clients.employee.employee_client import EmployeeClient


client = EmployeeClient()


def test_get_all_employees():
    response = client.get_all_employees()
    assert_that(response.status_code).is_equal_to(requests.codes.ok)

