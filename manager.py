#=============================PART 1=============================
from student import Student
from sqlite_database import SQLiteDatabase
from datetime import date
from csv_manager import CSVManager


class StudentManager:

    def __init__(self):

        self.database = SQLiteDatabase()
        self.csv = CSVManager()

        self.students = self.database.load_students()

    # ======================================
    # Utility
    # ======================================

    def pause(self):

        input("\nPress Enter To Continue...")

    # ======================================
    # Display Student Table
    # ======================================

    def print_student_table(self, student_list):

        if len(student_list) == 0:

            print("\nNo Students Found")

            return

        print("\n" + "=" * 115)

        print(
            f"{'No':<5}"
            f"{'Roll':<10}"
            f"{'Name':<20}"
                f"{'Age':<8}"
            f"{'Branch':<12}"
            f"{'Sem':<8}"
            f"{'CGPA':<8}"
            f"{'Phone':<15}"
        )

        print("=" * 115)

        for index, student in enumerate(student_list, start=1):

            print(
                f"{index:<5}"
                f"{student.roll:<10}"
                f"{student.name:<20}"
                f"{student.age:<8}"
                f"{student.branch:<12}"
                f"{student.semester:<8}"
                f"{student.cgpa:<8}"
                f"{student.phone:<15}"
            )

        print("=" * 115)

        print(f"\nTotal Students : {len(student_list)}")

    # ======================================
    # Add Student
    # ======================================

    def add_student(
        self,
        roll,
        name,
        age,
        branch,
        semester,
        cgpa,
        phone,
        email
    ):

        for student in self.students:

            if student.roll == roll:

                print("\nRoll Number Already Exists")

                return False

        student = Student(
            roll,
            name,
            age,
            branch,
            semester,
            cgpa,
            phone,
            email
        )

        self.students.append(student)

        self.database.insert_student(student)

        username = f"student{roll}"
        password = "student123"

        self.database.add_user(
            username,
            password,
            "student",
            roll
)

        print("\nStudent Added Successfully")

        return True
    
    # ======================================
    # View Students
    # ======================================

    def view_students(self):

        self.print_student_table(self.students)

        self.pause()


    # ======================================
    # Find Student By Roll
    # ======================================

    def find_student(self, roll):

        for student in self.students:

            if student.roll == roll:

                return student

        return None
    
    
    # ======================================
    # Delete Student
    # ======================================

    def delete_student(self, roll):

        student = self.find_student(roll)

        if student is None:

            print("\nStudent Not Found")

            return

        self.students.remove(student)

        self.database.delete_student(student.roll)

        username = f"student{roll}"
        self.database.delete_user(username)

        print("\nStudent Deleted Successfully")

    
    
    # ======================================
    # Update Student
    # ======================================

    def update_student(

        self,

        roll,

        name=None,

        age=None,

        branch=None,

        semester=None,

        cgpa=None,

        phone=None,

        email=None

    ):

        student = self.find_student(roll)

        if student is None:

            print("\nStudent Not Found")

            return

        student.update(

            name,

            age,

            branch,

            semester,

            cgpa,

            phone,

            email

        )

        self.database.update_student(student)

        print("\nStudent Updated Successfully")

    
    
    # ======================================
    # Total Students
    # ======================================

    def total_students(self):

        return self.database.total_students()



    # ======================================
    # Search By Roll
    # ======================================

    #def search_by_roll(self, roll):
     #   return self.find_student(roll)
    def search_by_roll(self, roll):

        return self.database.search_by_roll(roll) 

    # ======================================
    # Search By Name
    # ======================================

    # def search_by_name(self, name):

    #     result = []

    #     name = name.lower()

    #     for student in self.students:

    #         if name in student.name.lower():

    #             result.append(student)

    #     return result
    def search_by_name(self, name):

        return self.database.search_by_name(name)

    
    # ======================================
    # Search By Branch
    # ======================================

    # def search_by_branch(self, branch):

    #     result = []

    #     branch = branch.upper()

    #     for student in self.students:

    #         if student.branch == branch:

    #             result.append(student)

    #     return result

    def search_by_branch(self, branch):

        return self.database.search_by_branch(branch)

    # ======================================
    # Search By Semester
    # ======================================

    # def search_by_semester(self, semester):

    #     result = []

    #     for student in self.students:

    #         if student.semester == semester:

    #             result.append(student)

    #     return result
    
    def search_by_semester(self, semester):

        return self.database.search_by_semester(semester)

    # ======================================
    # Search By CGPA
    # ======================================

    # def search_by_cgpa(self, minimum, maximum):

    #     result = []

    #     for student in self.students:

    #         if minimum <= student.cgpa <= maximum:

    #             result.append(student)

    #     return result
    def search_by_cgpa(self, minimum, maximum):

        return self.database.search_by_cgpa(minimum, maximum)

    # ======================================
    # Sort By Roll
    # ======================================

    def sort_by_roll(self):
          return self.database.sort_by_roll()



    # ======================================
    # Sort By Name
    # ======================================

    def sort_by_name(self):

        return self.database.sort_by_name()


    # ======================================
    # Sort By CGPA
    # ======================================

    def sort_by_cgpa(self):

        return self.database.sort_by_cgpa()

    # ======================================
    # Highest CGPA
    # ======================================

    def highest_cgpa(self):
        return self.database.highest_cgpa()

    # ======================================
    # Lowest CGPA
    # ======================================

    def lowest_cgpa(self):

        return self.database.lowest_cgpa()

    # ======================================
    # Top Three Students
    # ======================================

    def top_three_students(self):

        return sorted(

            self.students,

            key=lambda student: student.cgpa,

            reverse=True

        )[:3]

    # ======================================
    # Average CGPA
    # ======================================

    # def average_cgpa(self):

    #     if not self.students:

    #         return 0

    #     total = 0

    #     for student in self.students:

    #         total += student.cgpa

    #     return total / len(self.students)

    def average_cgpa(self):

        return self.database.average_cgpa()

    # ======================================
    # Average Age
    # ======================================

    # def average_age(self):

    #     if not self.students:

    #         return 0

    #     total = 0

    #     for student in self.students:

    #         total += student.age

    #     return total / len(self.students)
    def average_age(self):

        return self.database.average_age()

    # ======================================
    # Students Per Branch
    # ======================================

    def students_per_branch(self):
        return self.database.students_per_branch()        
        # branches = {}

        # for student in self.students:

        #     branch = student.branch

        #     branches[branch] = branches.get(branch, 0) + 1

        # return branches

    # ======================================
    # Students Per Semester
    # ======================================

    def students_per_semester(self):
        return self.database.students_per_semester()

        # semesters = {}

        # for student in self.students:

        #     semester = student.semester

        #     semesters[semester] = semesters.get(semester, 0) + 1

        # return semesters

    # ======================================
    # Grade Distribution
    # ======================================

    def grade_distribution(self):
        return self.database.grade_distribution()



    # ======================================
    # Enter Marks
    # ======================================

    def enter_marks(self, roll):

        student = self.find_student(roll)

        if student is None:

            print("\nStudent Not Found")

            return

        student.enter_marks()

        self.database.save_marks(
            student.roll,
            student.marks
        )

        print("\nMarks Updated Successfully")


    # ======================================
    # Report Card
    # ======================================

    def report_card(self, roll):

        student = self.find_student(roll)

        if student is None:

            print("\nStudent Not Found")

            return

        student.marks = self.database.load_marks(student.roll)
          
        student.report_card()



    # ======================================
    # Mark Attendance
    # ======================================

    def mark_attendance(self, roll):

        student = self.find_student(roll)

        if student is None:

            print("\nStudent Not Found")

            return

        today = str(date.today())

        print("\n1. Present")
        print("2. Absent")

        choice = input("Choice : ")

        if choice == "1":

            student.mark_attendance(today, "Present")

        elif choice == "2":

            student.mark_attendance(today, "Absent")

        else:

            print("Invalid Choice")

            return

        self.database.save_attendance(student.roll,
            student.attendance)

        print("\nAttendance Saved")

    # ======================================
    # View Attendance
    # ======================================

    def view_attendance(self, roll):

        student = self.find_student(roll)

        if student is None:

            print("\nStudent Not Found")

            return

        student.attendance = self.database.load_attendance(student.roll)

        student.display_attendance()

    # ======================================
    # Export CSV
    # ======================================

    def export_csv(self):

        self.csv.export_students(self.students)

    # ======================================
# Import CSV
# ======================================

    def import_csv(self):

        imported = self.csv.import_students()

        if imported:

            self.students = imported

            for student in self.students:

                if self.database.student_exists(student.roll):

                    self.database.update_student(student)

                else:

                    self.database.insert_student(student)
                
            print("\nStudents Imported Successfully")    