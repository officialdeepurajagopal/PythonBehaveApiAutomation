Feature: Get Book Information API

  Scenario: Get book details from Library API
    Given I have the API endpoint as "https://rahulshettyacademy.com/Library/GetBook.php"
    And I set the book ID parameter as "bcg97692000"
    When I send a GET request to the API
    Then I should receive a successful response with status code 200
    And the response should contain book information
    And the response should contain fields like title, author, and ISBN

  Scenario: Get book details from Library API
    Given I have the base url setup for the test as "https://rahulshettyacademy.com/Library/GetBook.php"

