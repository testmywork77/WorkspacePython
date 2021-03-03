# Created by Venkata at 28/02/2021
Feature: Verify the Users added and deleted using Library API
  # Enter feature description here

  @smoke
  Scenario: Verify AddUser API functionality
    Given the user details which needs to be added to UsersDB
    When we execute the AddUser API method
    Then user is successfully added
    And status code of response should be 201

  @regression
  Scenario Outline: Verify AddUser API functionality
    Given the user details with <name> and <job>
    When we execute the AddUser API method
    Then status code of response should be 201
    And ensure response's name as <name> and job as <job>
    Examples:
      | name  | job  |
      | name1 | job1 |
      | name2 | job2 |
