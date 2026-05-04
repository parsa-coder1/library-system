# 📚 Library Management System (CLI - Python)

A simple and practical command-line Library Management System built with Python.  
This project is designed for learning purposes and demonstrates core programming concepts such as functions, data structures, file handling, and basic validation.

---

## 🚀 Features

### 📖 Book Management
- Add new books
- Prevent duplicate books (same title & author)
- View all books
- Sort books by:
  - Title
  - Author
  - Availability status
- Search books by:
  - ID
  - Title (supports partial search)

### 👤 User Management
- Add new users
- Prevent duplicate users (same name)
- Search users by:
  - ID
  - Name (supports partial search)

### 🔄 Borrowing System
- Borrow books
- Return books
- Prevent borrowing unavailable books
- Prevent duplicate borrowing
- Limit each user to maximum 3 books

### 📊 Filtering & Display
- Show available books
- Show borrowed books
- Show books borrowed by a specific user
- Display number of borrowed books per user

### 💾 Data Persistence
- All data is stored in a JSON file (`data.json`)
- Data is automatically saved after every change

---

## 🧱 Project Structure

### 📘 Books
Each book contains:
- `id`
- `title`
- `author`
- `available` (True / False)

### 👥 Users
Each user contains:
- `id`
- `name`
- `borrowed` (list of book IDs)

---

## ▶️ How to Run

1. Make sure Python is installed
2. Run the program:

```bash
python library_system.py
 
📁 Data File
The system uses:
data.json
If the file does not exist, it will be created automatically.
 
⚠️ Input Validation
• 
Prevents empty inputs
• 
Ensures numeric IDs
• 
Avoids invalid operations
• 
Handles missing data safely
 
🎯 Learning Goals
This project helps you practice:
• 
Functions and modular design
• 
Lists and dictionaries
• 
File handling (JSON)
• 
Input validation
• 
Searching and sorting
• 
Writing clean and readable code
 
🔮 Future Improvements
• 
Convert project to Object-Oriented Programming (OOP)
• 
Add database support (SQLite)
• 
Build a graphical user interface (GUI)
• 
Add authentication system
• 
Improve search performance with indexing
 
💡 Author    
Developed as a learning project to improve Python programming skills.            
