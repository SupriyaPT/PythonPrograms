import pprint


class Library:

    def __init__(self, book_list):
        self.available_books = book_list

    def display_books(self):
        print()
        print("Currently available books are: ")
        print(self.available_books)

    def lend_book(self,requested_book):
        if requested_book in self.available_books:
            print("The book {0} is allocated to you ".format(requested_book))
            self.available_books.remove(requested_book)
        else:
            print("Sorry, the book is currently unavailable")


    def add_book(self, returned_book):
        print("The {0} book returned successfully".format(returned_book))
        self.available_books.append(returned_book)


class Customer:

    def request_book(self):
        requested_book = input("Enter book name you would like to borrow :")
        return requested_book

    def return_book(self):
        requested_book = input("Enter book name you are returning : 2")
        return requested_book


if __name__ == '__main__':

    library = Library(["Vyakti aani Valli", "AsaMi AsaMi", "Batatyachi chal"])
    customer = Customer()

    while True:
        print("Enter 1 to display available books")
        print("Enter 2 to borrow book")
        print("Enter 3 to return book")
        print("Enter 4 to exit")

        try:
            user_input = int(input())
        except ValueError as err:
            print("Please enter valid input between 1 to 4. An error occurred due to invalid input :", err)
            continue

        if user_input is 1:
            library.display_books()
        elif user_input is 2:
            book = customer.request_book()
            library.lend_book(book)
        elif user_input is 3:
            book = customer.return_book()
            library.add_book(book)
        elif user_input is 4:
            quit()
        else:
            print("Invalid Input")