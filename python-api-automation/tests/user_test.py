import requests
from assertpy.assertpy import assert_that
from json import dumps, loads
from config import BASE_URI


def test_user_get_all():
    users = get_all_users()
    assert_that(users).is_not_empty()


def test_user_get_by_id():
    user_id = 1
    # Step 1: Call "get_user_by_id", return user object
    user = get_user_by_id(user_id)
    # Step 2: Check weather user object is not null or not
    assert_that(user).is_not_empty()
    assert_that(user["id"]).is_equal_to(user_id)


def test_user_get_based_on_firstname():
    users = get_all_users()
    first_names = [user['firstName'] for user in users]  # Python - List Comprehension
    assert_that(first_names).contains('firstName1')


def test_user_can_be_added():
    user_id = 99

    # Step 1: Create user dictionary
    user_dict = user_dict_create(user_id)

    # Step 2: Call "create_new_user" method with post request
    user_new = create_new_user(user_dict)  # First, create user
    assert_that(user_new).is_not_empty()

    # Step 3: Call "get_user_by_id", return user object
    user = get_user_by_id(user_new["id"])
    assert_that(user).is_not_empty()

    # Step 4: Call "


    # # Third, check weather the new user exist in users list
    # new_user = search_users_by_first_name(first_name, users)[0]
    # assert_that(new_user).is_not_empty()
    # # Delete the created user
    # user_id_to_be_deleted = new_user['id']
    # url = f"{BASE_URI}/{user_id_to_be_deleted}"
    # # Step 6: Trigger the delete request
    # response = requests.delete(url)
    # assert_that(response.status_code).is_equal_to(200)


def test_user_can_be_deleted():
    # Arrange - Create user
    user_id = 99
    user_dict = user_dict_create(user_id)   # user dictionary
    user_new = create_new_user(user_dict)   # return created new user
    assert_that(user_new).is_not_empty()  # check weather user is empty/null

    # Act - Delete user
    delete_user_by_id(user_new["id"])

    # Assert - Check user exists or not
    user = get_user_by_id(user_id)  # return user dictionary

        
# List Comprehension returns list
def search_users_by_first_name(first_name, users):
    return [user for user in users if user['firstName'] == first_name]


# Returns user dictionary
def get_user_by_id(user_id):
    url = f"{BASE_URI}/{user_id}"
    response = requests.get(url)
    assert_that(response.status_code).is_equal_to(200)
    assert_that(response.status_code).is_equal_to(requests.codes.ok)
    user = response.json()
    assert_that(user["id"]).is_equal_to(user_id)
    return user


# Returns user dictionary
def delete_user_by_id(user_id):
    url = f"{BASE_URI}/{user_id}"
    response = requests.delete(url)
    assert_that(response.status_code).is_equal_to(200)


# Returns users i.e. List of user dictionaries
def get_all_users():
    response = requests.get(BASE_URI)
    assert_that(response.status_code).is_equal_to(200)
    users = response.json()
    return users


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
