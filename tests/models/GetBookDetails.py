from dataclasses import dataclass

@dataclass
class GetBookDetails:
    book_name: str
    isbn: str
    aisle: str
    author: str