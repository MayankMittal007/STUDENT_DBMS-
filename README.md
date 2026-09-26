# STUDENT_DBMS-
# Student Database Management System

A Python-based Student Management System designed to manage student records efficiently using **SQLite**, with support for data management, authentication, searching, updating, deleting, importing/exporting data, and automated testing.

The project follows a modular structure where database operations, authentication, student management, CSV/JSON handling, and application logic are separated into dedicated Python modules.

---

## 🚀 Features

- Student record management
- Add, update, search, and delete student records
- SQLite-based persistent database
- Authentication system
- CSV data management
- JSON-based student data handling
- Database utility and management modules
- Automated test scripts for major operations
- Separate modules for better maintainability
- Local database support without requiring an external database server

---

## 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| **Python** | Core application development |
| **SQLite** | Database management |
| **CSV** | Student data import/export |
| **JSON** | Structured student data storage |
| **SQL** | Database queries and operations |

---

## 📁 Project Structure

```text
Student-Management-System/
│
├── __pycache__/          # Python generated cache files
│
├── auth.py               # Authentication-related functionality
├── csv_manager.py        # CSV data handling and management
├── database.py           # Database utilities and connection logic
├── main.py               # Main application entry point
├── manager.py            # Student management operations
├── sqlite_database.py    # SQLite database operations
├── student.py            # Student model / student-related functionality
│
├── student.db            # SQLite database containing student records
├── student.sqbpro        # SQLiteStudio project file
├── students.csv          # Student data in CSV format
├── students.json         # Student data in JSON format
│
├── tempCodeRunnerFile.py # Temporary development file
│
├── test_delete.py        # Delete operation tests
├── test_insert.py        # Insert operation tests
├── test_load.py          # Data loading tests
├── test_search.py        # Search operation tests
├── test_sqlite.py        # SQLite functionality tests
├── test_update.py        # Update operation tests
├── test_update2.py       # Additional update tests
│
└── README.md             # Project documentation
