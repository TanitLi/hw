import pickle

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print("Book added to the library.")
        print("======================================================")
        print("")

    def remove_book(self, book):
        if book in self.books:
            self.books.remove(book)
            print("Book removed from the library.")
            print("======================================================")
            print("")
        else:
            print("Book not found in the library.")
            print("======================================================")
            print("")

    def show_books(self):
        if self.books:
            print("Books on the shelf:")
            print("======================================================")
            for book in self.books:
                print(book)
        else:
            print("No books on the shelf.")
            print("======================================================")
            print("")

    def save_library(self, filename):
        with open(filename, 'wb') as file:
            pickle.dump(self.books, file)
        print(f"Book list saved to the file {filename}.")

    def load_library(self, filename):
        try:
            with open(filename, 'rb') as file:
                self.books = pickle.load(file)
            print(f"Book list loaded from the file {filename}.")
            print("======================================================")
        except FileNotFoundError:
            print("File not found. Unable to load.")
            print("======================================================")
            print("")

def show_menu():
    
        print("=== From TanitLi ===")
        print("=== + ===")
        print("=== Main Menu ===")
        print("Available commands:")
        
        print("")
        print("add    - add a book")
        print("remove - remove a book")
        print("show   - show the list of books")
        print("save   - save the list of books to a file")
        print("load   - load the list of books from a file")
        print("exit   - stop the program")
        print(" ")
        
def easy_show_menu():
    
        print("=== Main Menu ===")
        print("Available commands:")
        print("")
        print("add    - add a book")
        print("remove - remove a book")
        print("show   - show the list of books")
        print("save   - save the list of books to a file")
        print("load   - load the list of books from a file")
        print("exit   - stop the program")
        print(" ")
        
library = Library()

counter = 0
while True:
    
    if counter == 0:
        show_menu()
    else:
        easy_show_menu()
        
    command = input("Enter a command: ")
    counter += 1

    if command == "add":
        book = input("Enter the book title: ")
        library.add_book(book)

    elif command == "remove":
        book = input("Enter the book title: ")
        library.remove_book(book)

    elif command == "show":
        library.show_books()
        print("======================================================")
        print("")

    elif command == "save":
        filename = input("Enter the filename to save to: ")
        library.save_library(filename)

    elif command == "load":
        filename = input("Enter the filename to load from: ")
        library.load_library(filename)

    elif command == "exit":
        break

    else:
        print("Invalid command. Please try again.")
        print("======================================================")
        print("")

print("Program terminated.")