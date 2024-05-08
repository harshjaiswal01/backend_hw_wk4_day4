
class User():

    def __init__(self, name, address, phone, book=None):
        self.name = name
        self.address = address
        self.phone = phone
        self.book = book

    def get_info(self):
        print(f'User: {self.name}')
        print(f'Address: {self.address}')
        print(f'Phone: {self.phone}')

    def borrow(self, books):

        if self.book != None:
            print('You cant borrow two books!')
            return
        else:
            self.book = books
            books.is_available = False
            print(f'{self.name} has rented the {books.get_info()}')
    
    def return_book(self):
        self.book.is_available = True
        print(f'{self.name} returned the {self.book.get_info()}')
        self.book = None
