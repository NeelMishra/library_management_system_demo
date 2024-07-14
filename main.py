from models import BookManager, UserManager, CheckoutManager
from storage import Storage

def main_menu():
    print("\nLibrary Management System")
    print("1. Add Book")
    print("2. List Books")
    print("3. Find Book by ISBN")
    print("4. Remove Book by ISBN")
    print("5. Add User")
    print("6. List Users")
    print("7. Find User by User ID")
    print("8. Remove User by User ID")
    print("9. Checkout Book")
    print("10. List Checkouts")
    print("11. Exit")
    choice = input("Enter choice: ")
    return choice

def main():
    storage = Storage("library_data.json")
    book_manager = BookManager(storage)
    user_manager = UserManager(storage)
    checkout_manager = CheckoutManager(storage)

    while True:
        choice = main_menu()
        if choice == '1':
            title = input("Enter title: ")
            author = input("Enter author: ")
            isbn = input("Enter ISBN: ")
            try:
                book_manager.add_book(title, author, isbn)
                print("Book added.")
            except ValueError as e:
                print(e)
        elif choice == '2':
            book_manager.list_books()
        elif choice == '3':
            isbn = input("Enter ISBN: ")
            try:
                book = book_manager.find_book_by_isbn(isbn)
                print(book)
            except LookupError as e:
                print(e)
        elif choice == '4':
            isbn = input("Enter ISBN: ")
            try:
                book_manager.remove_book_by_isbn(isbn)
                storage.remove_entry("books", isbn, "isbn")
                print("Book removed.")
            except LookupError as e:
                print(e)
        elif choice == '5':
            name = input("Enter user name: ")
            user_id = input("Enter user ID: ")
            try:
                user_manager.add_user(name, user_id)
                print("User added.")
            except ValueError as e:
                print(e)
        elif choice == '6':
            user_manager.list_users()
        elif choice == '7':
            user_id = input("Enter user ID: ")
            try:
                user = user_manager.get_user(user_id)
                print(user)
            except KeyError as e:
                print(e)
        elif choice == '8':
            user_id = input("Enter user ID: ")
            try:
                user_manager.remove_user(user_id)
                storage.remove_entry("users", user_id, "user_id")
                print("User removed.")
            except KeyError as e:
                print(e)
        elif choice == '9':
            user_id = input("Enter user ID: ")
            isbn = input("Enter ISBN of the book to checkout: ")
            try:
                checkout_manager.checkout_book(user_id, isbn)
                print("Book checked out.")
            except ValueError as e:
                print(e)
        elif choice == '10':
            checkouts = storage.get_checkouts()
            for checkout in checkouts:
                print(checkout)
        elif choice == '11':
            print("Exiting.")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
