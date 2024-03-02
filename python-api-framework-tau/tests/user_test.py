from json import dumps
import requests
from assertpy.assertpy import assert_that
from utils.print_helpers import pretty_print

from config import BASE_URI

def test_get_all_users():
    response = requests.get(BASE_URI)
    assert_that(response.status_code).is_equal_to(requests.codes.ok)
    response_text = response.json()
    pretty_print(response_text)