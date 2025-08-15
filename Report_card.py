import json
from datetime import datetime
import matplotlib.pyplot as plt

DATA_FILE = "students_data.json"
SUBJECTS = ["Math", "Science", "English", "History", "Art"]
students_database = []

def clear_screen():
    os.system('clear' if os.name == 'posix' else 'cls')

def display_header():
    print("=" * 60)
    print("STUDENT REPORT CARD GENERATOR")
    print("welcome! Let's get started.")
    print("=" * 60)
    print()

def get_student_info():
    print("📝 Enter Student Information")
    print("-" * 30)
    while True:
        name = input("Student Name: ").strip()
        if len(name) >= 2:
            break
        print("Name must be at least 2 characters.")
    while True:
        try:
            student_id = int(input("Student ID: "))
            if student_id > 0:
                break
            print("Must be positive.")
        except ValueError:
            print("Invalid number.")
    while True:
        try:
            grade = int(input("Grade Level (1-12): "))
            if 1 <= grade <= 12:
                break
            print("Must be between 1 and 12.")
        except ValueError:
            print("Invalid grade level.")
    return {
        "name": name,
        "id": student_id,
        "grade": grade,
        "subjects": {},
        "date_created": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

def get_subject_grades(student_name):
    print(f"\n📊 Enter Grades for {student_name}")
    print("-" * 40)
    grades = {}
    for subject in SUBJECTS:
        while True:
            try:
                grade = float(input(f"{subject} grade (0-100): "))
                if 0 <= grade <= 100:
                    grades[subject] = grade
                    break
                print(" Must be between 0 and 100.")
            except ValueError:
                print(" Invalid number.")
    return grades

def calculate_gpa(grades):
    scale = [
        (97, 4.0), (93, 3.7), (90, 3.3), (87, 3.0), (83, 2.7),
        (80, 2.3), (77, 2.0), (73, 1.7), (70, 1.3), (67, 1.0), (65, 0.7), (0, 0.0)
    ]
    points = [next(p for cutoff, p in scale if grade >= cutoff) for grade in grades.values()]
    return round(statistics.mean(points), 2) if points else 0.0

def get_letter_grade(score):
    thresholds = [(97, "A+"), (93, "A"), (90, "A-"), (87, "B+"), (83, "B"),
                  (80, "B-"), (77, "C+"), (73, "C"), (70, "C-"),
                  (67, "D+"), (65, "D"), (0, "F")]
    return next(letter for cutoff, letter in thresholds if score >= cutoff)

def generate_performance_comment(avg):
    if avg >= 95: return "🌟 Outstanding work!"
    if avg >= 90: return "⭐ Excellent performance."
    if avg >= 85: return "👍 Very good, keep improving."
    if avg >= 80: return "📈 Good work, focus on weak spots."
    if avg >= 70: return "💪 Satisfactory, more effort needed."
    return "📚 Needs significant improvement."

def add_student():
    clear_screen()
    display_header()
    student = get_student_info()
    if any(s['id'] == student['id'] for s in students_database):
        print(" Student ID already exists!")
        input("Press Enter...")
        return
    student['subjects'] = get_subject_grades(student['name'])
    students_database.append(student)
    print(f"\n✅ {student['name']} added!")
    input("Press Enter...")

def view_all_students():
    clear_screen()
    display_header()
    if not students_database:
        print(" No students yet.")
        input("Press Enter...")
        return
    print(f"{'ID':<5} {'Name':<20} {'Grade':<6} {'Avg':<8} {'GPA':<6}")
    for s in students_database:
        avg = round(statistics.mean(s['subjects'].values()), 1)
        gpa = calculate_gpa(s['subjects'])
        print(f"{s['id']:<5} {s['name']:<20} {s['grade']:<6} {avg:<8} {gpa:<6}")
    input("\nPress Enter...")

def view_student_report():
    clear_screen()
    display_header()
    if not students_database:
        print("No students.")
        input("Press Enter...")
        return
    for s in students_database:
        print(f"ID: {s['id']} - {s['name']}")
    try:
        sid = int(input("\nEnter Student ID: "))
        student = next((s for s in students_database if s['id'] == sid), None)
        if not student:
            print("Not found.")
            input("Press Enter...")
            return
        display_report_card(student)
    except ValueError:
        print("Invalid ID.")
    input("Press Enter...")

def display_report_card(student):
    clear_screen()
    display_header()
    avg = round(statistics.mean(student['subjects'].values()), 2)
    gpa = calculate_gpa(student['subjects'])
    print(f"REPORT CARD: {student['name'].upper()}")
    print(f"ID: {student['id']} | Grade: {student['grade']} | Date: {student['date_created']}")
    print("=" * 60)
    for sub, score in student['subjects'].items():
        print(f"{sub:<12}: {score:>5.1f} ({get_letter_grade(score)})")
    print("=" * 60)
    print(f"Average: {avg} | GPA: {gpa} | Overall: {get_letter_grade(avg)}")
    print(f"Comment: {generate_performance_comment(avg)}")

def save_data():
    try:
        with open(DATA_FILE, "w") as f:
            json.dump(students_database, f, indent=2)
        print("Data saved.")
    except Exception as e:
        print(f"Save error: {e}")
    input("Press Enter...")

def load_data(silent=False):
    global students_database
    if not os.path.exists(DATA_FILE):
        if not silent:
            print("No saved data.")
        return
    try:
        with open(DATA_FILE, "r") as f:
            students_database = json.load(f)
        if not silent:
            print(f"Loaded {len(students_database)} students.")
    except Exception as e:
        print(f"Load error: {e}")
    if not silent:
        input("Press Enter...")

def main_menu():
    while True:
        clear_screen()
        display_header()
        print("1. Add New Student")
        print("2. View All Students")
        print("3. View Student Report Card")
        print("4. Save Data")
        print("5. Load Data")
        print("6. Exit")
        choice = input("Choose (1-6): ").strip()
        if choice == '1': add_student()
        elif choice == '2': view_all_students()
        elif choice == '3': view_student_report()
        elif choice == '4': save_data()
        elif choice == '5': load_data()
        elif choice == '6': break
        else:
            print("Invalid choice.")
            input("Press Enter...")

if __name__ == "__main__":
    load_data(silent=True)
    main_menu()
    print("👋 Goodbye!")


