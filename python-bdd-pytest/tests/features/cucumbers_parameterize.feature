@cucumber-basket
Feature: Cucumber Basket Parameterize

  @add
  Scenario: Add cucumbers to a basket
    Given the basket has "6" cucumbers
    When "4" cucumbers are added to the basket
    Then the basket contains "10" cucumbers

  @remove
  Scenario: Remove cucumbers from a basket
    Given the basket has "8" cucumbers
    When "3" cucumbers are removed from the basket
    Then the basket contains "5" cucumbers