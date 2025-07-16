# 📚 Library Management System

This is a simple **Library Management System** built with **Object-Oriented Programming (OOP)** in Python.  
It supports core functionalities such as:

- Managing books, magazines, and DVDs
- Registering users
- Borrowing, reserving, and returning items
- Data persistence using JSON files
- Exception-safe operations and custom error handling

The system uses:

- **Abstract classes** and **interfaces**
- **Composition** between classes
- **Custom exceptions**
- **Structured file operations** with `try-except-finally` blocks

## 🗂️ Project Structure

LibraryManagementSystem/
├── main.py
├── models/
│ ├── library_item.py
│ ├── book.py
│ ├── dvd.py
│ ├── magazine.py
│ ├── user.py
│ └── reservable.py
├── exceptions/
│ ├── item_not_found.py
│ ├── user_not_found.py
│ └── item_not_available.py
├── data/
│ ├── items.json
│ └── users.json
└── README.md
