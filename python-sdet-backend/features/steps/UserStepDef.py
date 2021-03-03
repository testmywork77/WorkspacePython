import requests
from behave import *
from utilities.resources import *
from payloads.payload import *


# context object is global and share across all the steps
@given("the user details which needs to be added to UsersDB")
def step_impl(context):
    # Arrange
    context.url = getUserBaseURI() + ApiResources.postUser
    context.payLoad = userPayload()


# Common for Sc1 & Sc2
@when("we execute the AddUser API method")
def step_impl(context):
    # Act
    context.response = requests.post(url=context.url, json=context.payLoad)


@then("user is successfully added")
def step_impl(context):
    # Assert
    assert context.response.status_code == 201
    context.statuscode = context.response.status_code
    response_validation(context, context.payLoad['name'], context.payLoad['job'])


@then("status code of response should be {statuscode:d}")
def step_impl(context, statuscode):
    print(context.response.status_code)
    assert context.response.status_code == statuscode


@given('the user details with {name} and {job}')
def step_impl(context, name, job):
    # Arrange
    context.url = getUserBaseURI() + ApiResources.postUser
    context.payLoad = userPayloadFromFeature(name, job)


@then("ensure AddUser API's response code as {statuscode}")
def step_impl(context, statuscode):
    """
    :type context: behave.runner.Context
    :type statuscode: str
    """
    assert context.response.status_code == int(statuscode)
    context.statuscode = context.response.status_code


@then("ensure response's name as {name} and job as {job}")
def step_impl(context, name, job):
    """
    :type context: behave.runner.Context
    :type name: str
    :type job: str
    """
    response_validation(context, name, job)


def response_validation(context, name, job):
    print("*** response_validation started ***")
    print(context.response.json())
    response_json = context.response.json()
    context.userId = response_json['id']
    assert response_json['name'] == name
    assert response_json['job'] == job
