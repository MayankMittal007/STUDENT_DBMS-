
"""
sqlite_database.py

Handles SQLite Database
"""

import sqlite3
import os
from student import Student


class SQLiteDatabase:

    def __init__(self):

        self.connection = sqlite3.connect("student.db")
        print("Database:", os.path.abspath("student.db"))

        self.cursor = self.connection.cursor()

        self.create_tables()
        self.create_default_users()

    # =======================================
    # Create Tables
    # =======================================

    def create_tables(self):

        self.cursor.execute("""

        CREATE TABLE IF NOT EXISTS students(

            roll TEXT PRIMARY KEY,

            name TEXT,

            age INTEGER,

            branch TEXT,

            semester INTEGER,

            cgpa REAL,

            phone TEXT,

            email TEXT

        )

        """)
      
      
        self.cursor.execute("""

        CREATE TABLE IF NOT EXISTS users(

            username TEXT PRIMARY KEY,

            password TEXT NOT NULL,

            role TEXT NOT NULL,

            roll TEXT,

            FOREIGN KEY(roll) REFERENCES students(roll)

        )

        """)  

        
        
        self.cursor.execute("""

        CREATE TABLE IF NOT EXISTS attendance(

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            roll TEXT NOT NULL,

            date TEXT NOT NULL,

            status TEXT NOT NULL,

            FOREIGN KEY(roll) REFERENCES students(roll)

        )

        """)    



        self.cursor.execute("""

        CREATE TABLE IF NOT EXISTS marks(

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            roll TEXT NOT NULL,

            subject TEXT NOT NULL,

            marks REAL NOT NULL,

            FOREIGN KEY(roll) REFERENCES students(roll)

        )

        """)




        self.connection.commit()

    # =======================================
    # Insert Student
    # =======================================

    def insert_student(self, student):

        query = """
        INSERT INTO students
        (roll, name, age, branch, semester, cgpa, phone, email)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """

        self.cursor.execute(
            query,
            (
                student.roll,
                student.name,
                student.age,
                student.branch,
                student.semester,
                student.cgpa,
                student.phone,
                student.email
            )
        )

        self.connection.commit()
    # =======================================
    # Update Student
    # =======================================

    def update_student(self, student):

        query = """
        UPDATE students
        SET name = ?,
            age = ?,
            branch = ?,
            semester = ?,
            cgpa = ?,
            phone = ?,
            email = ?
        WHERE roll = ?
        """

        self.cursor.execute(
            query,
            (
                student.name,
                student.age,
                student.branch,
                student.semester,
                student.cgpa,
                student.phone,
                student.email,
                student.roll
            )
        )

        self.connection.commit() 


    # =======================================
    # Check Student
    # =======================================

    def student_exists(self, roll):

        self.cursor.execute(
            "SELECT 1 FROM students WHERE roll = ?",
            (roll,)
        )

        return self.cursor.fetchone() is not None
       

    # =======================================
    # Load Students
    # =======================================

    def load_students(self):

        query = "SELECT * FROM students"

        self.cursor.execute(query)

        rows = self.cursor.fetchall()

        students = []

        for row in rows:

            student = Student(

                row[0],   # roll
                row[1],   # name
                row[2],   # age
                row[3],   # branch
                row[4],   # semester
                row[5],   # cgpa
                row[6],   # phone
                row[7]    # email

            )

            students.append(student)

        return students
    
        


    # =======================================
    # Update Student
    # =======================================

    def update_student(self, student):

        query = """
        UPDATE students
        SET
            name = ?,
            age = ?,
            branch = ?,
            semester = ?,
            cgpa = ?,
            phone = ?,
            email = ?
        WHERE roll = ?
        """

        self.cursor.execute(
            query,
            (
                student.name,
                student.age,
                student.branch,
                student.semester,
                student.cgpa,
                student.phone,
                student.email,
                student.roll
            )
        )

        self.connection.commit()        


    # =======================================
    # Delete Student
    # =======================================

    def delete_student(self, roll):

        query = """
        DELETE FROM students
        WHERE roll = ?
        """

        self.cursor.execute(query, (roll,))

        self.connection.commit()


    # =======================================
    # Add / Update Marks
    # =======================================

    def add_mark(self, roll, subject, marks):

        query = """
        INSERT INTO marks
        (roll, subject, marks)
        VALUES (?, ?, ?)
        """

        self.cursor.execute(
            query,
            (roll, subject, marks)
        )

        self.connection.commit()


    # =======================================
    # Load Marks
    # =======================================

    def load_marks(self, roll):

        query = """
        SELECT subject, marks
        FROM marks
        WHERE roll = ?
        """

        self.cursor.execute(query, (roll,))

        rows = self.cursor.fetchall()

        marks = {}

        for subject, score in rows:

            marks[subject] = score

        return marks





    # =======================================
    # Search Student By Roll
    # =======================================

    def search_by_roll(self, roll):

        query = """
        SELECT * FROM students
        WHERE roll = ?
        """

        self.cursor.execute(query, (roll,))

        row = self.cursor.fetchone()

        if row:

            student = Student(
                row[0],
                row[1],
                row[2],
                row[3],
                row[4],
                row[5],
                row[6],
                row[7]
            )

            return student

        return None

    # =======================================
    # Search Student By Name
    # =======================================

    def search_by_name(self, name):

        query = """
        SELECT * FROM students
        WHERE name LIKE ?
        """

        self.cursor.execute(query, ("%" + name + "%",))

        rows = self.cursor.fetchall()

        students = []

        for row in rows:

            student = Student(
                row[0],   # roll
                row[1],   # name
                row[2],   # age
                row[3],   # branch
                row[4],   # semester
                row[5],   # cgpa
                row[6],   # phone
                row[7]    # email
            )

            students.append(student)

        return students
        


    # =======================================
    # Search Student By Branch
    # =======================================

    def search_by_branch(self, branch):

        query = """
        SELECT * FROM students
        WHERE branch = ?
        """

        self.cursor.execute(query, (branch,))

        rows = self.cursor.fetchall()

        students = []

        for row in rows:

            student = Student(
                row[0],
                row[1],
                row[2],
                row[3],
                row[4],
                row[5],
                row[6],
                row[7]
            )

            students.append(student)

        return students


    # =======================================
    # Search Student By Semester
    # =======================================

    def search_by_semester(self, semester):

        query = """
        SELECT * FROM students
        WHERE semester = ?
        """

        self.cursor.execute(query, (semester,))

        rows = self.cursor.fetchall()

        students = []

        for row in rows:

            student = Student(
                row[0],
                row[1],
                row[2],
                row[3],
                row[4],
                row[5],
                row[6],
                row[7]
            )

            students.append(student)

        return students

    # =======================================
    # Search Student By CGPA
    # =======================================

    def search_by_cgpa(self, minimum, maximum):

        query = """
        SELECT * FROM students
        WHERE cgpa BETWEEN ? AND ?
        """

        self.cursor.execute(query, (minimum, maximum))

        rows = self.cursor.fetchall()

        students = []

        for row in rows:

            student = Student(
                row[0],
                row[1],
                row[2],
                row[3],
                row[4],
                row[5],
                row[6],
                row[7]
            )

            students.append(student)

        return students


    # =======================================
    # Total Students
    # =======================================

    def total_students(self):

        query = """
        SELECT COUNT(*)
        FROM students
        """

        self.cursor.execute(query)

        count = self.cursor.fetchone()[0]

        return count


    # =======================================
    # Average Age
    # =======================================

    def average_age(self):

        query = """
        SELECT AVG(age)
        FROM students
        """

        self.cursor.execute(query)

        average = self.cursor.fetchone()[0]

        if average is None:
            return 0

        return average

    # =======================================
    # Average CGPA
    # =======================================

    def average_cgpa(self):

        query = """
        SELECT AVG(cgpa)
        FROM students
        """

        self.cursor.execute(query)

        average = self.cursor.fetchone()[0]

        if average is None:
            return 0

        return average


    # =======================================
    # Highest CGPA Student
    # =======================================

    def highest_cgpa(self):

        query = """
        SELECT *
        FROM students
        ORDER BY cgpa DESC
        LIMIT 1
        """

        self.cursor.execute(query)

        row = self.cursor.fetchone()

        if row is None:
            return None

        return Student(
            row[0],
            row[1],
            row[2],
            row[3],
            row[4],
            row[5],
            row[6],
            row[7]
        )


    # =======================================
    # Lowest CGPA Student
    # =======================================

    def lowest_cgpa(self):

        query = """
        SELECT *
        FROM students
        ORDER BY cgpa ASC
        LIMIT 1
        """

        self.cursor.execute(query)

        row = self.cursor.fetchone()

        if row is None:
            return None

        return Student(
            row[0],
            row[1],
            row[2],
            row[3],
            row[4],
            row[5],
            row[6],
            row[7]
        )

    # =======================================
    # Students Per Branch
    # =======================================
    def students_per_branch(self):

        query = """
        SELECT branch, COUNT(*)
        FROM students
        GROUP BY branch
        ORDER BY branch
        """

        self.cursor.execute(query)

        return self.cursor.fetchall()

    # =======================================
    # Students Per Semester
    # =======================================

    def students_per_semester(self):

        query = """
        SELECT semester, COUNT(*)
        FROM students
        GROUP BY semester
        ORDER BY semester
        """

        self.cursor.execute(query)

        return self.cursor.fetchall()

    # =======================================
    # Grade Distribution
    # =======================================

    def grade_distribution(self):

        query = """
        SELECT
            CASE
                WHEN cgpa >= 9 THEN 'A'
                WHEN cgpa >= 8 THEN 'B'
                WHEN cgpa >= 7 THEN 'C'
                ELSE 'D'
            END AS grade,
            COUNT(*)
        FROM students
        GROUP BY grade
        ORDER BY grade
        """

        self.cursor.execute(query)

        return self.cursor.fetchall()
    # =======================================
    # Sort By Roll
    # =======================================

    def sort_by_roll(self):

        query = """
        SELECT *
        FROM students
        ORDER BY roll ASC
        """

        self.cursor.execute(query)

        rows = self.cursor.fetchall()

        students = []

        for row in rows:

            students.append(
                Student(
                    row[0],
                    row[1],
                    row[2],
                    row[3],
                    row[4],
                    row[5],
                    row[6],
                    row[7]
                )
            )

        return students


    # =======================================
    # Sort By Name
    # =======================================

    def sort_by_name(self):

        query = """
        SELECT *
        FROM students
        ORDER BY name ASC
        """

        self.cursor.execute(query)

        rows = self.cursor.fetchall()

        students = []

        for row in rows:

            students.append(
                Student(
                    row[0],
                    row[1],
                    row[2],
                    row[3],
                    row[4],
                    row[5],
                    row[6],
                    row[7]
                )
            )

        return students

    # =======================================
    # Sort By CGPA
    # =======================================

    def sort_by_cgpa(self):

        query = """
        SELECT *
        FROM students
        ORDER BY cgpa DESC
        """

        self.cursor.execute(query)

        rows = self.cursor.fetchall()

        students = []

        for row in rows:

            students.append(
                Student(
                    row[0],
                    row[1],
                    row[2],
                    row[3],
                    row[4],
                    row[5],
                    row[6],
                    row[7]
                )
            )

        return students

    # =======================================
    # Add User
    # =======================================

    def add_user(self, username, password, role, roll=None):

        query = """
        INSERT INTO users
        (username, password, role, roll)
        VALUES (?, ?, ?, ?)
        """

        self.cursor.execute(
            query,
            (username, password, role, roll)
        )

        self.connection.commit()


    # =======================================
    # Find User
    # =======================================

    def find_user(self, username):

        query = """
        SELECT username, password, role, roll
        FROM users
        WHERE username = ?
        """

        self.cursor.execute(query, (username,))

        return self.cursor.fetchone()


    # =======================================
    # Create Default Users
    # =======================================

    def create_default_users(self):

        default_users = [
            ("admin", "admin123", "admin", None),
            ("teacher", "teacher123", "teacher", None)
        ]

        for username, password, role, roll in default_users:

            if self.find_user(username) is None:
                self.add_user(username, password, role, roll)

    # =======================================
    # Delete User
    # =======================================

    def delete_user(self, username):

        query = """
        DELETE FROM users
        WHERE username = ?
        """

        self.cursor.execute(query, (username,))
        self.connection.commit()


    # =======================================
    # Save Marks
    # =======================================

    def save_marks(self, roll, marks):

        # Remove old marks
        self.cursor.execute(
            "DELETE FROM marks WHERE roll = ?",
            (roll,)
        )

        # Insert new marks
        for subject, score in marks.items():

            self.cursor.execute(
                """
                INSERT INTO marks
                (roll, subject, marks)
                VALUES (?, ?, ?)
                """,
                (roll, subject, score)
            )

        self.connection.commit()


    # =======================================
    # Load Marks
    # =======================================

    def load_marks(self, roll):

        self.cursor.execute(
            """
            SELECT subject, marks
            FROM marks
            WHERE roll = ?
            """,
            (roll,)
        )

        rows = self.cursor.fetchall()
        

        print(rows)      # <-- Add this

        marks = {}

        for subject, score in rows:
            marks[subject] = score

        return marks

    # =======================================
    # Save Attendance
    # =======================================

    def save_attendance(self, roll, attendance):

        self.cursor.execute(
            "DELETE FROM attendance WHERE roll = ?",
            (roll,)
        )

        for attendance_date, status in attendance.items():

            self.cursor.execute(
                """
                INSERT INTO attendance
                (roll, date, status)
                VALUES (?, ?, ?)
                """,
                (roll, attendance_date, status)
            )

        self.connection.commit()

    # =======================================
    # Load Attendance
    # =======================================

    def load_attendance(self, roll):

        self.cursor.execute(
            """
            SELECT date, status
            FROM attendance
            WHERE roll = ?
            ORDER BY date
            """,
            (roll,)
        )

        rows = self.cursor.fetchall()

        attendance = {}

        for attendance_date, status in rows:

            attendance[attendance_date] = status

        return attendance
