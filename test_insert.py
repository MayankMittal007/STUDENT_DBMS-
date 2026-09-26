from sqlite_database import SQLiteDatabase
from student import Student

db = SQLiteDatabase()

student = Student(
    "101",
    "Mayank",
    20,
    "AIML",
    5,
    8.75,
    "9876543210",
    "mayank@gmail.com"
)

db.insert_student(student)

print("Student Inserted Successfully!")