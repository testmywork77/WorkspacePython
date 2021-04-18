import requests
from assertpy.assertpy import assert_that
from json import dumps, loads
from config import BASE_URI


# Get All -> Assert
def test_user_get_all():
    # Act
    users = get_all_users()
    # Assert
    assert_that(users).is_not_empty()


# Get -> Assert
def test_user_get_by_id():
    # Arrange - Create user
    user_id = 99
    user_dict = user_dict_create(user_id)  # user dictionary
    user_new = create_new_user(user_dict)  # return created new user

    # Act - Get user based on id
    response = get_user_by_id(user_new["id"])

    # Assert
    assert_that(response.status_code).is_equal_to(200)
    assert_that(response.status_code).is_equal_to(requests.codes.ok)
    user = response.json()
    assert_that(user).is_not_empty()
    assert_that(user["id"]).is_equal_to(user_id)

    # Teardown
    delete_user_by_id(user_new["id"])  # delete user_new


# User: Get -> Assert
def test_user_get_based_on_firstname():
    # Arrange
    users = get_all_users()

    # Assert
    first_names = [user['firstName'] for user in users]  # Python - List Comprehension
    assert_that(first_names).contains('firstName1')


# User: Create -> Get -> Assert -> Delete
def test_user_can_be_created():
    # Arrange - Create user
    user_id = 99
    user_dict = user_dict_create(user_id)

    # Act - Create user
    user_new = create_new_user(user_dict)   # return created new user

    # Assert - Check user exists or not
    assert_that(user_new).is_not_empty()  # check weather user is empty/null
    response = get_user_by_id(user_new["id"])
    assert_that(response.status_code).is_equal_to(200)
    assert_that(response.status_code).is_equal_to(requests.codes.ok)
    user = response.json()
    assert_that(user).is_not_empty()
    assert_that(user["id"]).is_equal_to(user_id)

    # Teardown
    delete_user_by_id(user_new["id"])  # delete user_new


# User: Create -> Delete -> Get -> Assert
def test_user_can_be_deleted():
    # Arrange - Create user
    user_id = 99
    user_dict = user_dict_create(user_id)   # user dictionary
    user_new = create_new_user(user_dict)   # return created new user
    assert_that(user_new).is_not_empty()  # check weather user is empty/null

    # Act - Delete user
    delete_user_by_id(user_new["id"])

    # Assert - Check user exists or not
    response = get_user_by_id(user_new["id"])
    assert_that(response.status_code).is_equal_to(404)
    user = response.json()
    assert_that(user).is_empty()


# List Comprehension returns list
def search_users_by_first_name(first_name, users):
    return [user for user in users if user['firstName'] == first_name]


# Return user dictionary
def get_user_by_id(user_id):
    url = f"{BASE_URI}/{user_id}"
    response = requests.get(url)
    return response


# Delete user
def delete_user_by_id(user_id):
    url = f"{BASE_URI}/{user_id}"
    response = requests.delete(url)
    assert_that(response.status_code).is_equal_to(200)


# Return users list i.e. List of user dictionaries
def get_all_users():
    response = requests.get(BASE_URI)
    assert_that(response.status_code).is_equal_to(200)
    users = response.json()
    return users


# Create new user dictionary
def create_new_user(user_dict):
    # dumps method converts "python dictionary" to "json". It's Serialization
    payload = dumps(user_dict)
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json"
    }
    response = requests.post(url=BASE_URI, data=payload, headers=headers)
    assert_that(response.status_code).is_equal_to(201)
    user_created = loads(response.text)
    return user_created


# Create and return user dictionary
def user_dict_create(user_id):
    new_user_id = user_id
    user_dict = {
        "id": new_user_id,
        "firstName": f"firstName{new_user_id}",
        "lastName": f"lastName{new_user_id}",
        "loc": f"location{new_user_id}",
        "timestamp": ""
    }
    return user_dict
