@service
Feature: QueryEngine Instant Answer API

  Scenario Outline: Basic RestAPI API Query
    Given the Restful API is queried with "<phrase>"
    Then the response status code is "200"
    And the response contains results for "<phrase>"

    Examples: Animals
      | phrase   |
      | panda    |
      | python   |
      | platypus |

    Examples: Fruits
      | phrase     |
      | peach      |
      | pineapple  |
      | papaya     |