import requests
from assertpy.assertpy import assert_that
from json import dumps
from config import BASE_URI


def test_read_all_has_firstname1():
    users, response = get_all_users()
    assert_that(response.status_code).is_equal_to(requests.codes.ok)
    assert_that(response.status_code).is_equal_to(200)
    first_names = [user['firstName'] for user in users]  # Python - List Comprehension
    assert_that(first_names).contains('firstName1')


def test_user_can_be_added():
    first_name = create_new_unique_user()  # First, create user
    users, _ = get_all_users()  # Second , Get all users
    new_user = search_users_by_first_name(first_name, users)[0]  # Third, check weather the new user exist in users list
    assert_that(new_user).is_not_empty()
    # Delete the created user
    user_id_to_be_deleted = new_user['id']
    url = f"{BASE_URI}/{user_id_to_be_deleted}"
    # Step 6: Trigger the delete request
    response = requests.delete(url)
    assert_that(response.status_code).is_equal_to(200)


def test_user_can_be_deleted():
    # Step 1: Create new user and return firstName
    new_user_first_name = create_new_unique_user()
    # Step 2: Get all users
    users, _ = get_all_users()
    # Step 3: Search weather the new_user exists in all users based on firstName
    # print(type(search_users_by_first_name(new_user_first_name, users)))
    # Step 4: Get the new user object
    new_user = search_users_by_first_name(new_user_first_name, users)[0]
    # print(new_user)
    # print(type(new_user))
    # Step 5: Get id of user object
    user_id_to_be_deleted = new_user['id']
    url = f"{BASE_URI}/{user_id_to_be_deleted}"
    # Step 6: Trigger the delete request
    response = requests.delete(url)
    assert_that(response.status_code).is_equal_to(200)


# List Comprehension returns list
def search_users_by_first_name(first_name, users):
    return [user for user in users if user['firstName'] == first_name]


def get_all_users():
    response = requests.get(BASE_URI)
    users = response.json()
    return users, response


def create_new_unique_user():
    new_user_id = 2
    user_dict = {
        "id": new_user_id,
        "firstName": f"firstName{new_user_id}",
        "lastName": f"lastName{new_user_id}",
        "loc": f"location{new_user_id}",
        "timestamp": ""
    }
    # dumps method converts "python dictionary" to "json". It's Serialization
    payload = dumps(user_dict)
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json"
    }
    response = requests.post(url=BASE_URI, data=payload, headers=headers)
    assert_that(response.status_code).is_equal_to(201)
    return user_dict["firstName"]
