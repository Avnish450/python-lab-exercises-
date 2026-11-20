books = []

def add_book():
    title = input("Enter book title: ")
    author = input("Enter author name: ")
    books.append({"title": title, "author": author})
    print("Book added successfully.")

def view_books():
    if not books:
        print("No books available.")
    else:
        print("\nAvailable Books")
        for number, book in enumerate(books, start=1):
            print(f"{number}. {book['title']} by {book['author']}")

def search_book():
    search_title = input("Enter title to search: ").lower()
    found = False
    for book in books:
        if search_title in book["title"].lower():
            print("Book found:", book["title"], "by", book["author"])
            found = True
    if not found:
        print("Book not found.")

while True:
    print("\nLibrary Management System")
    print("1. Add Book")
    print("2. View Books")
    print("3. Search Book")
    print("4. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        add_book()
    elif choice == "2":
        view_books()
    elif choice == "3":
        search_book()
    elif choice == "4":
        print("Exiting library system.")
        break
    else:
        print("Invalid choice.")
