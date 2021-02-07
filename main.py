from typing import List

from typing import List

class BooksStack:
    def __init__(self, collection_name: str, collection_type: str):
        self.collection_name=collection_name
        self.collection_type=collection_type
        self.stack=[]

    def add_new_book(self, book_name: str):
        self.stack.append(book_name)

    def get_book(self):
        last_element= len(self.stack)-1
        top_book=self.stack.pop()
        print(top_book)
        return top_book

    def all_books(self) -> List[str]:
        print(self.stack)


    def __add__(self, second_stack):
        new_collection=BooksStack(self.collection_name, self.collection_type)
        new_collection.stack=self.stack+second_stack.stack
        return new_collection

    def __gt__(self, second_stack):
        return len(self.stack)>len(second_stack.stack)


    def __le__(self, second_stack):
        return len(self.stack) <= len(second_stack.stack)
my_books = BooksStack("My Stack of Books", "Natural")

my_books.add_new_book("Cheetahs")
my_books.add_new_book("Elephants")
my_books.add_new_book("Cats")

print(my_books.all_books())
print(my_books.get_book())
print(my_books.all_books())

her_books = BooksStack("Her Stack of Books", "Natural")
her_books.add_new_book("Horses")

my_books = my_books + her_books
print(my_books.all_books())

print(my_books > her_books)
print(my_books <= her_books)

print(my_books)
print(repr(my_books))

print(len(my_books))