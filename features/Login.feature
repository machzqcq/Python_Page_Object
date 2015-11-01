Feature: Login to portal

  Scenario: Login and logout
    When I open automationpractice website
    And I login with username "abc@xyz.com" and password "Test@123"
    Then I verify that I successfully logged in by logging out
