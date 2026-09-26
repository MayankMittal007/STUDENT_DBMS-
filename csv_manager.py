"""
csv_manager.py

Handles CSV Import and Export
"""

import csv
from student import Student


class CSVManager:

    def __init__(self, file_name="students.csv"):

        self.file_name = file_name

    # =====================================
    # Export Students
    # =====================================

    def export_students(self, students):

        try:

            with open(self.file_name, "w", newline="") as file:

                writer = csv.writer(file)

                writer.writerow([
                    "Roll",
                    "Name",
                    "Age",
                    "Branch",
                    "Semester",
                    "CGPA",
                    "Phone",
                    "Email"
                ])

                for student in students:

                    writer.writerow([
                        student.roll,
                        student.name,
                        student.age,
                        student.branch,
                        student.semester,
                        student.cgpa,
                        student.phone,
                        student.email
                    ])

            print("\nStudents exported successfully!")

        except Exception as e:

            print("\nExport Failed")

            print(e)

    # =====================================
    # Import Students
    # =====================================

    def import_students(self):

        students = []

        try:

            with open(self.file_name, "r") as file:

                reader = csv.DictReader(file)

                for row in reader:

                    student = Student(

                        row["Roll"],
                        row["Name"],
                        int(row["Age"]),
                        row["Branch"],
                        int(row["Semester"]),
                        float(row["CGPA"]),
                        row["Phone"],
                        row["Email"]

                    )

                    students.append(student)

            return students

        except FileNotFoundError:

            print("\nCSV File Not Found")

            return []

        except Exception as e:

            print(e)

            return []