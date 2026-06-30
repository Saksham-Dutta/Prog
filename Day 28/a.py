class Library:
    def __init__(self):
        self.books = {}
        self.users = {}

    def add_book(self, isbn, title, author):
        if isbn in self.books:
            print(" Book with this ISBN already exists.")
        else:
            self.books[isbn] = {"title": title, "author": author, "available": True}
            print(f" Book '{title}' added successfully!")

    def register_user(self, user_id, name):
        if user_id in self.users:
            print(" User ID already registered.")
        else:
            self.users[user_id] = {"name": name, "borrowed": []}
            print(f" User '{name}' registered successfully!")

    def checkout_book(self, user_id, isbn):
        if user_id not in self.users:
            print(" User not found.")
            return
        if isbn not in self.books:
            print(" Book not found.")
            return
        
        if not self.b Sorry, this book is already borrowed.")
        else:
            self.books[isbn]["available"] = False
            self.users[user_id]["borrowed"].append(isbn)
            print(f" '{self.books[isbn]['title']}' successfully checked out to {self.users[user_id]['name']}.")

    def return_book(self, user_id, isbn):
        if user_id not in self.users or isbn not in self.books:
            print(" Invalid User ID or ISBN.")
            return

        if isbn in self.users[user_id]["borrowed"]:
            self.books[isbn]["available"] = True
            self.users[user_id]["borrowed"].remove(isbn)
            print(f" '{self.books[isbn]['title']}' returned successfully.")
        else:
            print(" This user hasn't borrowed this book.")

    def view_books(self):
        if not self.books:
            print("The library is currently empty.")
            return
        print("\n=== CURRENT CATALOG ===")
        for isbn, info in self.books.items():
            status = "Available" if info["available"] else "Borrowed"
            print(f"ISBN: {isbn} | '{info['title']}' by {info['author']} [{status}]")


# --- Interactive Menu ---
def main():
    library = Library()
    
    # Seeding some initial data
    library.add_book("101", "Python Crash Course", "Eric Matthes")
    library.add_book("102", "Automate the Boring Stuff", "Al Sweigart")
    library.register_user("U1", "Alice")

    while True:
        print("\n====== LIBRARY MENU ======")
        print("1. Add a Book")
        print("2. Register a User")
        print("3. Borrow a Book")
        print("4. Return a Book")
        print("5. View All Books")
        print("6. Exit")
        
        choice = input("Enter choice (1-6): ").strip()

        if choice == "1":
            isbn = input("Enter ISBN: ")
            title = input("Enter Title: ")
            author = input("Enter Author: ")
            library.add_book(isbn, title, author)
        elif choice == "2":
            user_id = input("Enter User ID: ")
            name = input("Enter User Name: ")
            library.register_user(user_id, name)
        elif choice == "3":
            user_id = input("Enter User ID: ")
            isbn = input("Enter Book ISBN: ")
            library.checkout_book(user_id, isbn)
        elif choice == "4":
            user_id = input("Enter User ID: ")
            isbn = input("Enter Book ISBN: ")
            library.return_book(user_id, isbn)
        elif choice == "5":
            library.view_books()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()