import requests
from behave import given, when, then


class Context:
    def __init__(self):
        self.api_endpoint = None
        self.book_id = None
        self.response = None
        self.status_code = None


@given('^I have the API endpoint as (.*)$')
def step_set_api_endpoint(context, endpoint):
    """Set the API endpoint"""
    context.api_endpoint = endpoint


@given('^I set the book ID parameter as {book_id}$')
def step_set_book_id(context, book_id):
    """Set the book ID parameter"""
    context.book_id = book_id


@when('I send a GET request to the API')
def step_send_get_request(context):
    """Send a GET request to the API with the book ID parameter"""
    url = f"{context.api_endpoint}?ID={context.book_id}"
    try:
        context.response = requests.get(url, timeout=10)
        context.status_code = context.response.status_code
        assert context.response.ok, f"Request failed with status code {context.status_code}"
    except Exception as e:
        context.error = str(e)
        raise


@then('I should receive a successful response with status code {status_code:d}')
def step_check_status_code(context, status_code):
    """Verify the response status code"""
    assert context.status_code == status_code, \
        f"Expected status code {status_code}, but got {context.status_code}"


@then('the response should contain book information')
def step_check_response_contains_data(context):
    """Verify the response contains data"""
    assert context.response is not None, "Response is None"
    assert context.response.text, "Response body is empty"
    response_data = context.response.json() if context.response.headers.get('content-type') == 'application/json' else context.response.text
    assert response_data, "Response data is empty"


@then('the response should contain fields like title, author, and ISBN')
def step_check_required_fields(context):
    """Verify the response contains required fields"""
    try:
        response_data = context.response.json()
    except ValueError:
        raise AssertionError("Response is not valid JSON")
    
    # Check if response is a list or a dict
    if isinstance(response_data, list):
        assert len(response_data) > 0, "Response list is empty"
        book_data = response_data[0]
    else:
        book_data = response_data
    
    # Verify at least some book information fields exist
    book_info_fields = ['title', 'author', 'isbn', 'book_name', 'author_name']
    has_required_fields = any(field in book_data for field in book_info_fields)
    assert has_required_fields, \
        f"Response does not contain expected book information fields. Got: {list(book_data.keys())}"