from sqlite_database import SQLiteDatabase

db = SQLiteDatabase()

print("Before Delete")

students = db.load_students()

for student in students:
    print(student.roll, student.name)

roll = input("\nEnter Roll Number to Delete: ")

db.delete_student(roll)

print("\nStudent Deleted Successfully!")

print("\nAfter Delete")

students = db.load_students()

for student in students:
    print(student.roll, student.name)