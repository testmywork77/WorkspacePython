@web
Feature: Web Browsing

  Background:
    Given the home page is displayed

  Scenario: Basic Search
    When the user searches for "panda"
    Then results are shown for "panda"