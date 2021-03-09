Feature: Cucumber Basket Parameterize
  As a gardener,
  I want to carry cucumbers in a basket,
  So that I don't drop them all.

  Scenario: Add cucumbers to a basket
    Given the basket has "6" cucumbers
    When "4" cucumbers are added to the basket
    Then the basket contains "10" cucumbers

  Scenario: Remove cucumbers from a basket
    Given the basket has "8" cucumbers
    When "3" cucumbers are removed from the basket
    Then the basket contains "5" cucumbers

#  @add
#  Scenario Outline: Add cucumbers to a basket
#    Given the basket has "<initial>" cucumbers
#    When "<some>" cucumbers are added to the basket
#    Then the basket contains "<total>" cucumbers
#    Examples:
#      | initial | some | total |
#      | 0       | 3    | 3     |
#      | 2       | 4    | 6     |
#      | 5       | 5    | 10    |
#
#
#  @remove
#  Scenario Outline: Remove cucumbers from the basket
#    Given the basket has "<initial>" cucumbers
#    When "<some>" cucumbers are removed from the basket
#    Then the basket contains "<total>" cucumbers
#    Examples:
#      | initial | some | total |
#      | 8       | 3    | 5     |
#      | 10      | 4    | 6     |
#      | 7       | 0    | 7     |