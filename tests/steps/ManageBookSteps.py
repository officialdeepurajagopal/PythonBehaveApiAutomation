import requests
import Contants as Constants
from behave import given, when, then
from models.GetBookDetails import GetBookDetails
from models.AddBookRequest import AddBookRequest
from models.AddBookResponse import AddBookResponse


class ManageBooks:

    def __init__(self):
        self.baseUrl = none
        self.bookId = none
        self.response = none
        self.newBookId = none


@given('I have the url setup for "{operation}"')
def setup_url(ManageBooks, operation):
    """Setup the base url for the test"""
    if operation == 'AddBook':
        ManageBooks.baseUrl = f'{Constants.BASE_URL}{Constants.Add_Book}'
    if operation == 'GetBook':
        ManageBooks.baseUrl = f'{Constants.BASE_URL}{Constants.Get_Book}'

@when('I sent a request to get the details of the book with ID "{bookId}"')
def get_book_details(ManageBooks, bookId):
    """Sending GET request to get the book details using book id"""
    urlToSend = f"{ManageBooks.baseUrl}?ID={bookId}"
    ManageBooks.response = requests.get(urlToSend)

    assert ManageBooks.response.status_code == 200, f"Expected status code 200, but got {ManageBooks.response.status_code}"

@then('I want to validate the name of the book is "{bookName}"')
def validate_book_name(ManageBooks, bookName):
    """Validating the name of the book in the response"""
    details_of_book = ManageBooks.response.json()[0]
    book = GetBookDetails(**details_of_book)
    assert book.book_name == bookName, f"Expected book name '{bookName}', but got '{book.book_name}'"

@given('I have the request body created the details of the book to be added "{name}", "{isbn}", "{aisle}", "{author}"')
def create_request_to_add_book(ManageBooks, name, isbn, aisle, author):
    """Creating the request body to add a book"""
    ManageBooks.AddBookRequest = AddBookRequest(
        name=name,
        isbn=isbn,
        aisle=aisle,
        author=author,
    )

@when('I sent a request to add the book to the library')
def send_add_book_request(ManageBooks):
    """Sending POST request to add a book"""
    headers = {'Content-Type': 'application/json'}
    ManageBooks.response = requests.post(ManageBooks.baseUrl, json=ManageBooks.AddBookRequest.__dict__, headers=headers)

    responseOfAddBook = AddBookResponse(**ManageBooks.response.json())
    ManageBooks.newBookId = responseOfAddBook.ID

    assert ManageBooks.response.status_code == 200, f"Expected status code 200, but got {ManageBooks.response.status_code}"
    

@then('I want to validate the response code is {code}')
def validate_response_code(ManageBooks, code):
    """Validating the response code of the add book request"""
    assert ManageBooks.response.status_code == int(code), f"Expected status code {code}, but got {ManageBooks.response.status_code}"

@when('I sent a request to get the details of the created book')
def get_details_of_created_book(ManageBooks):
    """Sending GET request to get the details of the created book"""
    bookId = ManageBooks.newBookId
    reqUrl = f"{ManageBooks.baseUrl}?ID={bookId}"
    ManageBooks.response = requests.get(reqUrl)

    assert ManageBooks.response.status_code == 200, f"Expected status code 200, but got {ManageBooks.response.status_code}"