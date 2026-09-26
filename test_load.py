from sqlite_database import SQLiteDatabase

db = SQLiteDatabase()

students = db.load_students()

for student in students:

    print(student.roll)
    print(student.name)
    print(student.branch)
    print(student.cgpa)
    print("-" * 30)