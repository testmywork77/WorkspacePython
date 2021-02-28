# Created by Venkata at 28/02/2021
Feature: Verify the Users added and deleted using Library API
  # Enter feature description here

  Scenario: Verify AddUser API functionality
    Given the user details which needs to be added to UsersDB
    When we execute the AddUser API method
    Then user is successfully added

  Scenario Outline: Verify AddUser API functionality
    Given the user details with <name> and <job>
    When we execute the AddUser API method
    Then ensure AddUser API's response code as <statuscode>
    And ensure response's name as <name> and job as <job>
    Examples:
      | name  | job  | statuscode |
      | name1 | job1 | 201        |
      | name2 | job2 | 201        |
