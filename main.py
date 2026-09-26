from manager import StudentManager
from auth import AuthManager        


# =====================================
# LOGIN
# =====================================

def login_screen(auth):

    print("\n" + "=" * 50)
    print("              LOGIN")
    print("=" * 50)

    username = input("Username : ")
    password = input("Password : ")

    user = auth.login(username, password)

    if user is None:
        print("\nInvalid Username Or Password")
        return None

    print("\nLogin Successful!")
    print("Logged In As :", user["role"].upper())

    return user

# =====================================
# MAIN MENU
# =====================================

def admin_menu(manager):

    

    while True:

        print("\n" + "=" * 50)
        print("      STUDENT MANAGEMENT SYSTEM")
        print("=" * 50)

        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Sort Students")
        print("7. Analytics")
        print("8. Marks")
        print("9. Attendance")
        print("10. CSV")
        print("11. Exit")

        choice = input("\nEnter Choice : ")

        # --------------------------------
        # ADD STUDENT
        # --------------------------------

        if choice == "1":

            roll = input("Roll Number : ")
            name = input("Name : ")
            age = int(input("Age : "))
            branch = input("Branch : ").upper()
            semester = int(input("Semester : "))
            cgpa = float(input("CGPA : "))
            phone = input("Phone : ")
            email = input("Email : ")

            manager.add_student(
                roll,
                name,
                age,
                branch,
                semester,
                cgpa,
                phone,
                email
            )

            manager.pause()

        # --------------------------------
        # VIEW
        # --------------------------------

        elif choice == "2":

            manager.view_students()

        # --------------------------------
        # SEARCH
        # --------------------------------

        elif choice == "3":

            print("\n1. Roll")
            print("2. Name")
            print("3. Branch")
            print("4. Semester")
            print("5. CGPA Range")

            ch = input("\nChoice : ")

            if ch == "1":

                roll = input("Roll : ")

                student = manager.search_by_roll(roll)

                if student:
                    manager.print_student_table([student])
                else:
                    print("Student Not Found")

            elif ch == "2":

                name = input("Name : ")

                manager.print_student_table(
                    manager.search_by_name(name)
                )

            elif ch == "3":

                branch = input("Branch : ")

                manager.print_student_table(
                    manager.search_by_branch(branch)
                )

            elif ch == "4":

                semester = int(input("Semester : "))

                manager.print_student_table(
                    manager.search_by_semester(semester)
                )

            elif ch == "5":

                minimum = float(input("Minimum CGPA : "))
                maximum = float(input("Maximum CGPA : "))

                manager.print_student_table(
                    manager.search_by_cgpa(
                        minimum,
                        maximum
                    )
                )

            manager.pause()

        # --------------------------------
        # UPDATE
        # --------------------------------

        elif choice == "4":

            roll = input("Roll Number : ")

            student = manager.find_student(roll)

            if student is None:

                print("Student Not Found")

            else:

                name = input("New Name : ")
                age = input("New Age : ")
                branch = input("New Branch : ")
                semester = input("New Semester : ")
                cgpa = input("New CGPA : ")
                phone = input("New Phone : ")
                email = input("New Email : ")

                manager.update_student(

                    roll,

                    name if name else None,

                    int(age) if age else None,

                    branch if branch else None,

                    int(semester) if semester else None,

                    float(cgpa) if cgpa else None,

                    phone if phone else None,

                    email if email else None

                )

            manager.pause()

        # --------------------------------
        # DELETE
        # --------------------------------

        elif choice == "5":

            roll = input("Roll Number : ")

            manager.delete_student(roll)

            manager.pause()

        # --------------------------------
        # SORT
        # --------------------------------

        elif choice == "6":

            print("\n1. Roll")
            print("2. Name")
            print("3. CGPA")

            ch = input("Choice : ")

            if ch == "1":

                manager.print_student_table(
                    manager.sort_by_roll()
                )

            elif ch == "2":

                manager.print_student_table(
                    manager.sort_by_name()
                )

            elif ch == "3":

                manager.print_student_table(
                    manager.sort_by_cgpa()
                )

            manager.pause()

        # --------------------------------
        # ANALYTICS
        # --------------------------------

        elif choice == "7":

            while True:

                print("\n" + "=" * 50)
                print("              ANALYTICS")
                print("=" * 50)

                print("1. Total Students")
                print("2. Average Age")
                print("3. Average CGPA")
                print("4. Highest CGPA Student")
                print("5. Lowest CGPA Student")
                print("6. Students Per Branch")
                print("7. Students Per Semester")
                print("8. Grade Distribution")
                print("9. Back")

                ch = input("\nChoice : ")

                if ch == "1":

                    print("\nTotal Students :", manager.total_students())
                    manager.pause()

                elif ch == "2":

                    print("\nAverage Age :", round(manager.average_age(), 2))
                    manager.pause()

                elif ch == "3":

                    print("\nAverage CGPA :", round(manager.average_cgpa(), 2))
                    manager.pause()

                elif ch == "4":

                    student = manager.highest_cgpa()

                    if student:
                        manager.print_student_table([student])

                    manager.pause()

                elif ch == "5":

                    student = manager.lowest_cgpa()

                    if student:
                        manager.print_student_table([student])

                    manager.pause()

                elif ch == "6":

                    print("\nStudents Per Branch")
                    print("-" * 30)

                    for branch, count in manager.students_per_branch():
                        print(f"{branch:<15}{count}")

                    manager.pause()

                elif ch == "7":

                    print("\nStudents Per Semester")
                    print("-" * 30)

                    for semester, count in manager.students_per_semester():
                        print(f"Semester {semester:<3}: {count}")
                    

                    manager.pause()

                elif ch == "8":

                    print("\nGrade Distribution")
                    print("-" * 30)

                    for grade, count in manager.grade_distribution():
                        print(f"Grade {grade}: {count}")

                    manager.pause()

                elif ch == "9":

                    break

                else:

                    print("\nInvalid Choice")
        # --------------------------------
        # MARKS
        # --------------------------------

        elif choice == "8":

            print("\n1. Enter Marks")
            print("2. Report Card")

            ch = input("Choice : ")

            roll = input("Roll Number : ")

            if ch == "1":

                manager.enter_marks(roll)

            else:

                manager.report_card(roll)

            manager.pause()


        elif choice == "9":

            print("\n1. Mark Attendance")
            print("2. View Attendance")

            ch = input("Choice : ")

            roll = input("Roll Number : ")

            if ch == "1":

                manager.mark_attendance(roll)

            elif ch == "2":

                manager.view_attendance(roll)

            manager.pause()

        # --------------------------------
        # CSV
        # --------------------------------
        elif choice == "10":

            print("\n========== CSV ==========")

            print("1. Export Students")

            print("2. Import Students")

            print("3. Back")

            ch = input("\nChoice : ")

            if ch == "1":

                manager.export_csv()

            elif ch == "2":

                manager.import_csv()

            manager.pause()    
        # --------------------------------
        # EXIT
        # --------------------------------

        elif choice == "11":

            print("\nLogging Out...")

            break

        else:

            print("Invalid Choice")

            manager.pause()

# =====================================
# TEACHER MENU
# =====================================

def teacher_menu(manager):

    while True:

        print("\n" + "=" * 50)
        print("              TEACHER MENU")
        print("=" * 50)

        print("1. View Students")
        print("2. Search Student")
        print("3. Enter Marks")
        print("4. View Report Card")
        print("5. Mark Attendance")
        print("6. View Attendance")
        print("7. Logout")

        choice = input("\nEnter Choice : ")

        if choice == "1":

            manager.view_students()

        elif choice == "2":

            roll = input("Enter Roll Number : ")

            student = manager.search_by_roll(roll)

            if student:
                manager.print_student_table([student])

            else:
                print("\nStudent Not Found")

            manager.pause()

        elif choice == "3":

            roll = input("Enter Roll Number : ")

            manager.enter_marks(roll)

            manager.pause()

        elif choice == "4":

            roll = input("Enter Roll Number : ")

            manager.report_card(roll)

            manager.pause()

        elif choice == "5":

            roll = input("Enter Roll Number : ")

            manager.mark_attendance(roll)

            manager.pause()

        elif choice == "6":

            roll = input("Enter Roll Number : ")

            manager.view_attendance(roll)

            manager.pause()

        elif choice == "7":

            print("\nLogging Out...")

            break

        else:

            print("\nInvalid Choice")

# =====================================
# STUDENT MENU
# =====================================

def student_menu(manager, user):

    roll = user["roll"]

    student = manager.find_student(roll)

    if student is None:

        print("\nStudent Record Not Found")
        print("Please Contact Administrator.")

        return

    while True:

        print("\n" + "=" * 50)
        print("              STUDENT MENU")
        print("=" * 50)

        print("Welcome,", student.name)

        print("\n1. View My Profile")
        print("2. View My Report Card")
        print("3. View My Attendance")
        print("4. Logout")

        choice = input("\nEnter Choice : ")

        # -----------------------------
        # PROFILE
        # -----------------------------

        if choice == "1":

            manager.print_student_table([student])

            manager.pause()

        # -----------------------------
        # REPORT CARD
        # -----------------------------

        elif choice == "2":

            manager.report_card(roll)

            manager.pause()

        # -----------------------------
        # ATTENDANCE
        # -----------------------------

        elif choice == "3":

            manager.view_attendance(roll)

            manager.pause()

        # -----------------------------
        # LOGOUT
        # -----------------------------

        elif choice == "4":

            print("\nLogging Out...")

            break

        else:

            print("\nInvalid Choice")            
# =====================================
# MAIN PROGRAM
# =====================================

def main():

    manager = StudentManager()

    auth = AuthManager(manager.database)

    while True:

        user = login_screen(auth)

        if user is None:

            continue

        role = user["role"]

        if role == "admin":

            admin_menu(manager)

        elif role == "teacher":

            teacher_menu(manager)

        elif role == "student":

            student_menu(manager, user)

        else:

            print("\nUnknown User Role")


if __name__ == "__main__":
    main()



