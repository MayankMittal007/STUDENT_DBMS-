from sqlite_database import SQLiteDatabase

db = SQLiteDatabase()

students = db.load_students()

student = students[0]

print("Before Update:")
print(student.name)
print(student.cgpa)

student.name = "Mayank Mittal"
student.cgpa = 9.45

db.update_student(student)

print("\nStudent Updated Successfully!")