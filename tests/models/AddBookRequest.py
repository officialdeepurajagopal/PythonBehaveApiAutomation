from dataclasses import dataclass

@dataclass
class AddBookRequest:
    name: str
    isbn: str
    aisle: str
    author: str