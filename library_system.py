import json

def save_data(data):
    with open("data.json", "w") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)


def load_data():
    try:
        with open("data.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {"books": [], "users": []}
    

def show_user_books(user, books):
    if not user["borrowed"]:
        print("no borrowed books!")
        return
    
    borrowed_ids = set(user["borrowed"])

    print(f"{user['name']}'s borrowed books:")
    for b in books:
        if b["id"] in borrowed_ids:
            print(f"- {b['title']} by {b['author']}")


def get_status(book):
    return "available" if book["available"] else "borrowed"


def save_all(books, users):
    save_data({"books": books, "users": users})


def add_book(books, next_id):
    title = input("book title: ").strip()
    author = input("author: ").strip()

    if not title or not author:
        print("title and author required!")
        return next_id

    if any(b["title"].lower() == title.lower() and b["author"].lower() == author.lower() for b in books):
        print("this book already exists!")
        return next_id

    book = {
        "id": next_id,
        "title": title,
        "author": author,
        "available": True
    }

    books.append(book)
    print("book added!")
    return next_id + 1


def show_books(books):
    if not books:
        print("no book found!")
        return
    
    for b in books:
        status = get_status(b)
        print(f"{b['id']} | {b['title']} | {b['author']} | {status}")


def sort_books_by_title(books):
    sorted_books = sorted(books, key=lambda b: b["title"].lower())

    for b in sorted_books:
        status = get_status(b)
        print(f"{b['id']} | {b['title']} | {b['author']} | {status}")


def sort_books_by_author(books):
    sorted_books = sorted(books, key=lambda b: b["author"].lower())

    for b in sorted_books:
        status = get_status(b)

        print(f"{b['id']} | {b['title']} | {b['author']} | {status}")


def sort_books_by_status(books):
    sorted_books = sorted(books, key=lambda b: b["available"], reverse=True)

    for b in sorted_books:
        status = get_status(b)

        print(f"{b['id']} | {b['title']} | {b['author']} | {status}")


def search_book(books):
    book_id = input("enter book id to search: ").strip()
    book_title = input("enter book title to search: ").strip().lower()

    if not book_id and not book_title:
        print("enter id or title!")
        return

    if book_id.isdigit():
        book_map = {b["id"]: b for b in books}
        b = book_map.get(int(book_id))
        if b:
            status = get_status(b)
            print(f"id: {b['id']} | title: {b['title']} | author: {b['author']} | status: {status}")
            return
        else:
            print("no book found!")
            return
        
    found = False

    for b in books:
        if book_title and book_title in b["title"].lower():
            
            status = get_status(b)
            print(f"id: {b['id']} | title: {b['title']} | author: {b['author']} | status: {status}")
            found = True
        
    if not found:
        print("no book found!")


def filter_books(books, available=True):
    found = False

    for b in books:
        if b["available"] == available:
            status = get_status(b)
            print(f"{b['id']:>3} | {b['title']:<20} | {b['author']:<15} | {status}")
            found = True

    if not found:
        print("no book found!")


def add_user(users, next_id):
    name = input("user name: ").strip()

    if not name:
        print("name required!")
        return next_id

    if any(u["name"].lower() == name.lower() for u in users):
        print(f"the {name} user already exists!")
        return next_id

    user = {
        "id": next_id,
        "name": name,
        "borrowed": []
    }

    users.append(user)
    print("user added!")
    return next_id + 1


def search_user(users, books):
    user_id = input("enter user id to search: ").strip()
    user_name = input("enter user name to search: ").strip().lower()

    if not user_id and not user_name:
        print("enter id or name!")
        return

    for u in users:
        if (user_id.isdigit() and u["id"] == int(user_id)) or \
        (user_name and user_name in u["name"].lower()):
            print(f"id: {u['id']} | user_name: {u['name']} | borrowed count: {len(u['borrowed'])}")
            show_user_books(u, books)
            return
        
    print("no user found!")


def borrow_book(books, users):
    user_id = input("enter user id: ").strip()
    book_id = input("enter book id: ").strip()

    if not user_id.isdigit() or not book_id.isdigit():
        print("invalid input!")
        return
    
    user_id = int(user_id)
    book_id = int(book_id)

    user = None
    for u in users:
        if u["id"] == user_id:
            user = u
            break

    if not user:
        print("user not fount!")
        return
    
    for b in books:
        if b["id"] == book_id:

            if book_id in user["borrowed"]:
                print("user already has this book!")
                return
            
            if not b["available"]:
                print("book already borrowed!")
                return
            
            if len(user["borrowed"]) >= 3:
                print("user reached borrow limit!")
                return

            b["available"] = False
            user["borrowed"].append(book_id)
            print("book borrowed!")
            return
        
    print("book not found!")


def show_user_borrowed_books(users,books):
    user_id = input("enter user id: ").strip()

    if not user_id.isdigit():
        print("invalid user id!")
        return
    user_id = int(user_id)

    for u in users:
        if u["id"] == user_id:
            print(f"user: {u['name']} | books: {len(u['borrowed'])}")
            show_user_books(u, books)
            return
        
    print("no user found!")


def return_book(books, users):
    user_id = input("enter user id: ").strip()
    book_id = input("enter book id: ").strip()

    if not user_id.isdigit() or not book_id.isdigit():
        print("invalid input!")
        return
    
    user_id = int(user_id)
    book_id = int(book_id)

    for u in users:
        if u["id"] == user_id:

            if book_id not in u["borrowed"]:
                print("this user doesn't have this book!")
                return
            
            u["borrowed"].remove(book_id)

            for b in books:
                if b["id"] == book_id:
                    b["available"] = True
                    print("book returned!")
                    return
                
    print("user not found!")


# main program

data = load_data()

books = data["books"]
users = data["users"]

if books:
    book_id = max(b["id"] for b in books) + 1
else:
    book_id = 1

if users:
    user_id = max(u["id"] for u in users) + 1
else:
    user_id = 1


while True:
    print("\n=== library system ===")
    print("1. add book")
    print("2. show books")
    print("3. sort books by title")
    print("4. sort books by author")
    print("5. sort books by status")
    print("6. search book")
    print("7. show available books")
    print("8. show borrowed books")
    print("9. add user")
    print("10. search user")
    print("11. borrow book")
    print("12. show user borrowed books")
    print("13. return book")
    print("14. exit")

    choice = input("choose: ")

    if choice == "1":
        book_id = add_book(books, book_id)
        save_all(books, users)

    elif choice == "2":
        show_books(books)

    elif choice == "3":
        sort_books_by_title(books)

    elif choice == "4":
        sort_books_by_author(books)

    elif choice == "5":
        sort_books_by_status(books)

    elif choice == "6":
        search_book(books)

    elif choice == "7":
        filter_books(books, True)

    elif choice == "8":
        filter_books(books, False)

    elif choice == "9":
        user_id = add_user(users, user_id)
        save_all(books, users)

    elif choice == "10":
        search_user(users, books)

    elif choice == "11":
        borrow_book(books, users)
        save_all(books, users)

    elif choice == "12":
        show_user_borrowed_books(users, books)

    elif choice == "13":
        return_book(books, users)
        save_all(books, users)

    elif choice == "14":
        print("exited!")
        break

    else:
        print("invalid choice!")