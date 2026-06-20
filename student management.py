import sqlite3

# Connect to database
conn = sqlite3.connect("students.db")
cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    roll_no INTEGER PRIMARY KEY,
    name TEXT,
    marks INTEGER
)
""")

conn.commit()

def add_student():
    roll = int(input("Enter Roll Number: "))
    name = input("Enter Name: ")
    marks = int(input("Enter Marks: "))

    cursor.execute(
        "INSERT INTO students VALUES (?, ?, ?)",
        (roll, name, marks)
    )
    conn.commit()
    print("Student Added Successfully!")

def view_students():
    cursor.execute("SELECT * FROM students")
    records = cursor.fetchall()

    print("\n--- Student Records ---")
    for row in records:
        print(row)

def update_student():
    roll = int(input("Enter Roll Number to Update: "))
    new_marks = int(input("Enter New Marks: "))

    cursor.execute(
        "UPDATE students SET marks=? WHERE roll_no=?",
        (new_marks, roll)
    )
    conn.commit()
    print("Record Updated Successfully!")

def delete_student():
    roll = int(input("Enter Roll Number to Delete: "))

    cursor.execute(
        "DELETE FROM students WHERE roll_no=?",
        (roll,)
    )
    conn.commit()
    print("Record Deleted Successfully!")

while True:
    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        update_student()
    elif choice == "4":
        delete_student()
    elif choice == "5":
        print("Exiting...")
        break
    else:
        print("Invalid Choice!")

conn.close()