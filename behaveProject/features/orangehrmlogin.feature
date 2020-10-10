Feature: OrangeHRM Login

  Scenario: Login to OrangeHRM with valid parameters
    Given I launch a Chrome browser
    When I open a OrangeHRM Homepage
    And Enter username as "admin" and password as "admin123"
    And Click on login button
    Then User must successfully login to the Dashboard page

  Scenario Outline: Login to OrangeHRM with Multiple parameters
    Given I launch a Chrome browser
    When I open a OrangeHRM Homepage
    And Enter username as "<username>" and password as "<password>"
    And Click on login button
    Then User must successfully login to the Dashboard page
    Examples:
      | username | password |
      | admin    | admin123 |
      | admin123 | admin    |
      | adminXyz | admin123 |
      | admin    | adminXyz |