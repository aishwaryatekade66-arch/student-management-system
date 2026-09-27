import mysql.connector


# ================= DATABASE CONNECTION =================
def connect_db():

    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="12345@tekade",
        database="student_db"
    )

    print("Database Connected Successfully")

    return conn


# ================= ADD STUDENT =================
def add_student():

    conn = connect_db()
    cursor = conn.cursor()

    try:

        name = input("Enter Student Name: ").strip()
        course = input("Enter Course: ").strip()
        fees = float(input("Enter Fees: "))
        city = input("Enter City: ").strip()

        query = """
        INSERT INTO students
        (name, course, fees, city)
        VALUES (%s, %s, %s, %s)
        """

        values = (name, course, fees, city)

        cursor.execute(query, values)

        conn.commit()

        print("Student Added Successfully")

    except ValueError:

        print("Invalid fees. Please enter a number.")

    except mysql.connector.Error as err:

        print("Database Error:", err)

    finally:

        cursor.close()
        conn.close()


# ================= DISPLAY STUDENTS =================
def display_students():

    conn = connect_db()
    cursor = conn.cursor()

    try:

        query = """
        SELECT id, name, course, fees, city
        FROM students
        ORDER BY id
        """

        cursor.execute(query)

        students = cursor.fetchall()

        if not students:

            print("No students found.")
            return

        print("\n" + "=" * 70)

        print(
            f"{'ID':<5}"
            f"{'Name':<20}"
            f"{'Course':<15}"
            f"{'Fees':<12}"
            f"{'City':<15}"
        )

        print("-" * 70)

        for student in students:

            print(
                f"{student[0]:<5}"
                f"{student[1]:<20}"
                f"{student[2]:<15}"
                f"{student[3]:<12.2f}"
                f"{student[4]:<15}"
            )

        print("=" * 70)

    except mysql.connector.Error as err:

        print("Database Error:", err)

    finally:

        cursor.close()
        conn.close()


# ================= SEARCH STUDENT =================
def search_student():

    conn = connect_db()
    cursor = conn.cursor()

    try:

        student_id = int(
            input("Enter Student ID: ")
        )

        query = """
        SELECT id, name, course, fees, city
        FROM students
        WHERE id = %s
        """

        cursor.execute(query, (student_id,))

        student = cursor.fetchone()

        if student:

            print("\nStudent Found")

            print("ID     :", student[0])
            print("Name   :", student[1])
            print("Course :", student[2])
            print("Fees   :", student[3])
            print("City   :", student[4])

        else:

            print("Student Not Found")

    except ValueError:

        print("Invalid Student ID.")

    except mysql.connector.Error as err:

        print("Database Error:", err)

    finally:

        cursor.close()
        conn.close()


# ================= UPDATE STUDENT =================
def update_student():

    conn = connect_db()
    cursor = conn.cursor()

    try:

        student_id = int(
            input("Enter Student ID: ")
        )

        # First check student exists
        cursor.execute(
            "SELECT id FROM students WHERE id = %s",
            (student_id,)
        )

        student = cursor.fetchone()

        if not student:

            print("Student Not Found")
            return

        name = input("Enter New Name: ").strip()
        course = input("Enter New Course: ").strip()
        fees = float(input("Enter New Fees: "))
        city = input("Enter New City: ").strip()

        query = """
        UPDATE students
        SET name = %s,
            course = %s,
            fees = %s,
            city = %s
        WHERE id = %s
        """

        values = (
            name,
            course,
            fees,
            city,
            student_id
        )

        cursor.execute(query, values)

        conn.commit()

        print("Student Updated Successfully")

    except ValueError:

        print("Invalid input.")

    except mysql.connector.Error as err:

        print("Database Error:", err)

    finally:

        cursor.close()
        conn.close()


# ================= DELETE STUDENT =================
def delete_student():

    conn = connect_db()
    cursor = conn.cursor()

    try:

        student_id = int(
            input("Enter Student ID: ")
        )

        # Check student exists
        cursor.execute(
            "SELECT id FROM students WHERE id = %s",
            (student_id,)
        )

        student = cursor.fetchone()

        if not student:

            print("Student Not Found")
            return

        query = """
        DELETE FROM students
        WHERE id = %s
        """

        cursor.execute(query, (student_id,))

        conn.commit()

        print("Student Deleted Successfully")

    except ValueError:

        print("Invalid Student ID.")

    except mysql.connector.Error as err:

        print("Database Error:", err)

    finally:

        cursor.close()
        conn.close()


# ================= MAIN MENU =================
def main():

    while True:

        print("\n================================")
        print("     STUDENT MANAGEMENT SYSTEM")
        print("================================")
        print("1. Add Student")
        print("2. Display Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":

            add_student()

        elif choice == "2":

            display_students()

        elif choice == "3":

            search_student()

        elif choice == "4":

            update_student()

        elif choice == "5":

            delete_student()

        elif choice == "6":

            print("Thank You!")
            print("Program Closed.")
            break

        else:

            print("Invalid choice. Please select 1-6.")


# ================= START PROGRAM =================
if __name__ == "__main__":

    main()