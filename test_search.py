from sqlite_database import SQLiteDatabase

db = SQLiteDatabase()

roll = input("Enter Roll Number: ")

student = db.search_by_roll(roll)

if student:
    student.display()
else:
    print("Student Not Found")