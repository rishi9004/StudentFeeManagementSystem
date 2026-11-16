import csv
import os

# Student Fee Management System - PS No. 43
COURSE_FEES = {
    "BCA": 45000,
    "BTECH": 60000,
    "MBA": 80000
}
DATA_FILE = "fees.txt"
students = {}


def load_records():
    """Load student records from fees.txt."""
    students.clear()
    if not os.path.exists(DATA_FILE):
        return
    try:
        with open(DATA_FILE, "r", newline="", encoding="utf-8") as file:
            for row in csv.reader(file):
                if len(row) != 4:
                    continue
                roll, name, course, paid_text = row
                course = course.strip().upper()
                if course not in COURSE_FEES:
                    continue
                try:
                    paid = int(paid_text)
                except ValueError:
                    continue
                total = COURSE_FEES[course]
                if 0 <= paid <= total:
                    students[roll] = {
                        "Name": name,
                        "Course": course,
                        "Paid": paid
                    }
    except OSError:
        print("Error: Could not read fees.txt.")


def save_records():
    """Save all student records to fees.txt."""
    try:
        with open(DATA_FILE, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            for roll, details in students.items():
                writer.writerow([
                    roll, details["Name"], details["Course"], details["Paid"]
                ])
    except OSError:
        print("Error: Could not save fees.txt.")


def get_status(paid, total):
    if paid == 0:
        return "Unpaid"
    if paid < total:
        return "Partial"
    return "Paid"


def add_student():
    print("\\n--- Add Student ---")
    roll = input("Roll: ").strip()
    if not roll:
        print("Invalid roll number.")
        return
    if roll in students:
        print("Student already exists.")
        return

    name = input("Name: ").strip()
    if not name:
        print("Invalid student name.")
        return

    course = input("Course: ").strip().upper()
    if course not in COURSE_FEES:
        print("Invalid course. Choose BCA, BTECH or MBA.")
        return

    students[roll] = {"Name": name, "Course": course, "Paid": 0}
    save_records()
    total = COURSE_FEES[course]
    print(
        f"Student added: {roll} |{name} |{course} |"
        f"Total Fee: {total}|Paid:0|Due:{total}|Status:Unpaid"
    )


def pay_fees():
    print("\\n--- Pay Fees ---")
    roll = input("Roll: ").strip()
    if roll not in students:
        print("Student not found.")
        return

    try:
        amount = int(input("Amount: ").strip())
    except ValueError:
        print("Invalid amount. Payment rejected.")
        return

    if amount <= 0:
        print("Invalid amount. Payment rejected.")
        return

    student = students[roll]
    total = COURSE_FEES[student["Course"]]
    due = total - student["Paid"]

    if amount > due:
        print(f"Amount exceeds due ({due}). Payment rejected.")
        return

    student["Paid"] += amount
    due = total - student["Paid"]
    status = get_status(student["Paid"], total)
    save_records()
    print(
        f"Payment received. Paid:{student['Paid']}|"
        f"Due:{due}|Status: {status}"
    )


def search_student():
    print("\\n--- Search Student ---")
    roll = input("Roll: ").strip()
    if roll not in students:
        print("Student not found.")
        return

    student = students[roll]
    total = COURSE_FEES[student["Course"]]
    due = total - student["Paid"]
    print(
        f"{roll} |{student['Name']} |{student['Course']} |"
        f"Total Fee:{total}|Paid:{student['Paid']}|Due:{due}|"
        f"Status:{get_status(student['Paid'], total)}"
    )


def pending_dues():
    print("\\n--- Pending Dues ---")
    found = False
    for roll, student in students.items():
        total = COURSE_FEES[student["Course"]]
        due = total - student["Paid"]
        if due > 0:
            print(f"{roll}|{student['Name']}|Due:{due}")
            found = True
    if not found:
        print("No pending dues.")


def main():
    load_records()
    while True:
        print("\\n===== STUDENT FEE MANAGEMENT SYSTEM =====")
        print("1. Add Student")
        print("2. Pay Fees")
        print("3. Search Student")
        print("4. Pending Dues")
        print("5. Exit")
        choice = input("Menu option: ").strip()

        if choice == "1":
            add_student()
        elif choice == "2":
            pay_fees()
        elif choice == "3":
            search_student()
        elif choice == "4":
            pending_dues()
        elif choice == "5":
            save_records()
            print("Program closed.")
            break
        else:
            print("Invalid menu option. Enter 1 to 5.")


if __name__ == "__main__":
    main()
