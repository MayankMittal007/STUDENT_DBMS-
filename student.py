class Student:

    def __init__(
        self,
        roll,
        name,
        age,
        branch,
        semester,
        cgpa,
        phone,
        email,
        attendance=None,
        marks=None
    ):

        self.roll = roll
        self.name = name
        self.age = age
        self.branch = branch
        self.semester = semester
        self.cgpa = cgpa
        self.phone = phone
        self.email = email
        if attendance is None:
            self.attendance = {}
        else:
            self.attendance = attendance

        if marks is None:

            self.marks = {
                "Python": 0,
                "Java": 0,
                "DBMS": 0,
                "Operating System": 0,
                "Computer Network": 0
            }

        else:

            self.marks = marks

    # -----------------------------------
    # Convert Object -> Dictionary
    # -----------------------------------

    def to_dict(self):

        return {

            "roll": self.roll,
            "name": self.name,
            "age": self.age,
            "branch": self.branch,
            "semester": self.semester,
            "cgpa": self.cgpa,
            "phone": self.phone,
            "email": self.email,
            "attendance": self.attendance,
            "marks": self.marks

        }

    # -----------------------------------
    # Dictionary -> Object
    # -----------------------------------

    @classmethod
    def from_dict(cls, data):

        return cls(

            data["roll"],
            data["name"],
            data["age"],
            data["branch"],
            data["semester"],
            data["cgpa"],
            data["phone"],
            data["email"],
            data.get("attendance", {}),
            data.get("marks", None)

        )

    # -----------------------------------
    # Display Student
    # -----------------------------------

    def display(self):

        print("\n" + "=" * 40)
        print("STUDENT DETAILS")
        print("=" * 40)

        print(f"Roll Number : {self.roll}")
        print(f"Name        : {self.name}")
        print(f"Age         : {self.age}")
        print(f"Branch      : {self.branch}")
        print(f"Semester    : {self.semester}")
        print(f"CGPA        : {self.cgpa}")
        print(f"Phone       : {self.phone}")
        print(f"Email       : {self.email}")
        print(f"Attendance  : {self.attendance_percentage()}%")

        print("=" * 40)

    def update(
        self,
        name=None,
        age=None,
        branch=None,
        semester=None,
        cgpa=None,
        phone=None,
        email=None
    ):

        if name:
            self.name = name

        if age:
            self.age = age

        if branch:
            self.branch = branch

        if semester:
            self.semester = semester

        if cgpa:
            self.cgpa = cgpa

        if phone:
            self.phone = phone

        if email:
            self.email = email




# ======================================
# Enter Marks
# ======================================

    def enter_marks(self):

        print("\nEnter Marks (0-100)\n")

        for subject in self.marks:

            while True:

                try:

                    marks = int(input(f"{subject} : "))

                    if 0 <= marks <= 100:

                        self.marks[subject] = marks

                        break

                    else:

                        print("Marks must be between 0 and 100.")

                except ValueError:

                    print("Invalid Input.")


        # ======================================
    # Total Marks
    # ======================================

    def total_marks(self):

        return sum(self.marks.values())

    # ======================================
    # Percentage
    # ======================================

    def percentage(self):

        return self.total_marks() / len(self.marks)
    # ======================================
    # Grade
    # ======================================

    def grade(self):

        percentage = self.percentage()

        if percentage >= 90:

            return "A+"

        elif percentage >= 80:

            return "A"

        elif percentage >= 70:

            return "B"

        elif percentage >= 60:

            return "C"

        else:

            return "D"
        
        # ======================================
    # Display Marks
    # ======================================

    def display_marks(self):

        print("\nSubjects\n")

        for subject, marks in self.marks.items():

            print(f"{subject:<25}{marks}")


        # ======================================
    # Report Card
    # ======================================

    def report_card(self):

        print("\n")
        print("=" * 55)
        print("REPORT CARD")
        print("=" * 55)

        print(f"Name       : {self.name}")
        print(f"Roll       : {self.roll}")
        print(f"Branch     : {self.branch}")
        print(f"Semester   : {self.semester}")
        print(f"Attendance : {self.attendance}%")

        self.display_marks()

        print("\n---------------------------------------")

        print(f"Total      : {self.total_marks()}")

        print(f"Percentage : {self.percentage():.2f}")

        print(f"Grade      : {self.grade()}")

        print("=" * 55) 


    # ======================================
    # Mark Attendance
    # ======================================

    def mark_attendance(self, date, status):

        self.attendance[date] = status



    # ======================================
    # Attendance Percentage
    # ======================================

    def attendance_percentage(self):

        if len(self.attendance) == 0:
            return 0

        present = 0

        for status in self.attendance.values():

            if status == "Present":
                present += 1

        return round((present / len(self.attendance)) * 100, 2)

    # ======================================
    # Attendance History
    # ======================================

    def display_attendance(self):

        if len(self.attendance) == 0:

            print("\nNo Attendance Records")

            return

        print("\nAttendance History\n")

        for date, status in self.attendance.items():

            print(f"{date:<15}{status}")

        print("\nAttendance Percentage :", self.attendance_percentage(), "%")

        
            