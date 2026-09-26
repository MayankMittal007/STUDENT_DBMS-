import json
import os

from student import Student


class DatabaseManager:

    def __init__(self, file_name="students.json"):

        self.file_name = file_name

    # -----------------------------------
    # Load Students
    # -----------------------------------

    def load_students(self):

        if not os.path.exists(self.file_name):
            return []

        try:

            with open(self.file_name, "r") as file:

                data = json.load(file)

                students = []

                for student_data in data:

                    student = Student.from_dict(student_data)

                    students.append(student)

                return students

        except Exception as e:

            print("\nError Loading Database")
            print(e)

            return []

    # -----------------------------------
    # Save Students
    # -----------------------------------

    def save_students(self, students):

        try:

            data = []

            for student in students:

                data.append(student.to_dict())

            with open(self.file_name, "w") as file:

                json.dump(data, file, indent=4)

        except Exception as e:

            print("\nError Saving Database")
            print(e)