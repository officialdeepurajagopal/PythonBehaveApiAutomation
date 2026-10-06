Feature:
Managing Books for a Library API

  # Scenario: Get Book Details
  #   Given I have the url setup for "GetBook"
  #   When I sent a request to get the details of the book with ID "bcg970908"
  #   Then I want to validate the name of the book is "DpTest9014"

  Scenario Outline: Add book to the library
    Given I have the url setup for "AddBook"
    And I have the request body created the details of the book to be added "<name>", "<isbn>", "<aisle>", "<author>"
    When I sent a request to add the book to the library
    Then I want to validate the response code is 200
    When I sent a request to get the details of the created book
    Then I want to validate the response code is 200

  Examples:
    | name        | isbn     | aisle | author      |
    | DpTest9022  | bcg9746| 3820 | Deepu       |
    # | DpTest9023  | bcg9738| 7239   | Deepu       |


