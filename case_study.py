# ============================================================
#   STUDENT MANAGEMENT SYSTEM
#   case_study.py
# ============================================================

import os

# ────────────────────────────────────────────────────────────
#  FEATURE 1 — Student Class
# ────────────────────────────────────────────────────────────

class Student:
    """Represents a single student with roll number, name, and subject marks."""

    def __init__(self, roll_no, name, marks):
        """
        Initialize a Student object.
        marks is a dict like {"Math": 85, "Physics": 78}
        """
        self.roll_no = roll_no
        self.name    = name
        self.marks   = marks          # dict: subject -> score

    def average(self):
        """Returns the average of all subject marks."""
        if not self.marks:
            return 0.0
        return sum(self.marks.values()) / len(self.marks)

    def grade(self):
        """Returns letter grade A/B/C/D/F based on average marks."""
        avg = self.average()
        if avg >= 80:
            return "A"
        elif avg >= 70:
            return "B"
        elif avg >= 60:
            return "C"
        elif avg >= 50:
            return "D"
        else:
            return "F"

    def __str__(self):
        """Returns a neat single-line summary of the student."""
        subjects = "  |  ".join(f"{sub}: {score}" for sub, score in self.marks.items())
        return (f"[{self.roll_no}]  {self.name:<20}  "
                f"Avg: {self.average():.1f}  Grade: {self.grade()}  |  {subjects}")


# ────────────────────────────────────────────────────────────
#  FEATURE 2 — File Persistence
# ────────────────────────────────────────────────────────────

FILE_NAME = "records.txt"

def save_all(students):
    """Saves all student records to records.txt in CSV format."""
    try:
        with open(FILE_NAME, "w") as f:
            for s in students:
                subject_part = ",".join(f"{sub}:{score}" for sub, score in s.marks.items())
                line = f"{s.roll_no},{s.name},{subject_part}\n"
                f.write(line)
        print("  [✓] Data saved successfully.")
    except Exception as e:
        print(f"  [!] Error saving data: {e}")


def load_all():
    """Reads records.txt and returns a list of Student objects."""
    students = []
    if not os.path.exists(FILE_NAME):
        return students                      # no file yet — start fresh

    try:
        with open(FILE_NAME, "r") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                parts  = line.split(",")
                roll_no = parts[0]
                name    = parts[1]
                marks   = {}
                for item in parts[2:]:
                    subject, score = item.split(":")
                    marks[subject] = float(score)
                students.append(Student(roll_no, name, marks))
    except Exception as e:
        print(f"  [!] Error loading data: {e}")

    return students


# ────────────────────────────────────────────────────────────
#  FEATURE 3 — Menu Action Functions
# ────────────────────────────────────────────────────────────

def get_subjects_and_marks():
    """
    Prompts the user to enter subjects and marks.
    Returns a dict of {subject: score} or None on invalid input.
    """
    marks = {}
    print("  Enter subjects and marks (type 'done' when finished).")
    while True:
        subject = input("    Subject name (or 'done'): ").strip()
        if subject.lower() == "done":
            break
        if not subject:
            print("    [!] Subject name cannot be empty.")
            continue
        try:
            score = float(input(f"    Marks for {subject} (0-100): "))
            if not (0 <= score <= 100):
                print("    [!] Marks must be between 0 and 100.")
                continue
            marks[subject] = score
        except ValueError:
            print("    [!] Please enter a valid number.")
    return marks if marks else None


def add_student(students):
    """Adds a new student after validating all inputs."""
    print("\n--- Add New Student ---")

    # roll number — must be unique
    while True:
        roll_no = input("  Roll Number: ").strip().upper()
        if not roll_no:
            print("  [!] Roll number cannot be empty.")
            continue
        if any(s.roll_no == roll_no for s in students):
            print("  [!] Roll number already exists. Use a unique one.")
            continue
        break

    # name — cannot be empty
    while True:
        name = input("  Student Name: ").strip()
        if name:
            break
        print("  [!] Name cannot be empty.")

    # marks
    marks = get_subjects_and_marks()
    if not marks:
        print("  [!] No marks entered. Student not added.")
        return

    students.append(Student(roll_no, name, marks))
    print(f"  [✓] Student '{name}' added successfully!")


def view_all(students):
    """Displays all students in a formatted table."""
    print("\n--- All Students ---")
    if not students:
        print("  No students found.")
        return
    print("-" * 80)
    for s in students:
        print(" ", s)
    print("-" * 80)
    print(f"  Total: {len(students)} student(s)")


def search_student(students):
    """Searches for a student by roll number."""
    print("\n--- Search Student ---")
    roll_no = input("  Enter Roll Number: ").strip().upper()
    for s in students:
        if s.roll_no == roll_no:
            print("\n  Student Found:")
            print(f"    Roll No : {s.roll_no}")
            print(f"    Name    : {s.name}")
            print(f"    Marks   : {s.marks}")
            print(f"    Average : {s.average():.1f}")
            print(f"    Grade   : {s.grade()}")
            return
    print("  [!] Student not found.")


def delete_student(students):
    """Deletes a student record by roll number."""
    print("\n--- Delete Student ---")
    roll_no = input("  Enter Roll Number to delete: ").strip().upper()
    for i, s in enumerate(students):
        if s.roll_no == roll_no:
            confirm = input(f"  Delete '{s.name}'? (yes/no): ").strip().lower()
            if confirm == "yes":
                students.pop(i)
                print("  [✓] Student deleted.")
            else:
                print("  Deletion cancelled.")
            return
    print("  [!] Student not found.")


def top_performer(students):
    """Displays the student with the highest average marks."""
    print("\n--- Top Performer ---")
    if not students:
        print("  No students found.")
        return
    top = max(students, key=lambda s: s.average())
    print(f"  🏆  {top.name}  |  Roll: {top.roll_no}  |  Average: {top.average():.1f}  |  Grade: {top.grade()}")


# ────────────────────────────────────────────────────────────
#  FEATURE 4 — Analytics / Class Statistics
# ────────────────────────────────────────────────────────────

def show_statistics(students):
    """Displays full class analytics including averages, grades, and best subject."""
    print("\n--- Class Statistics ---")
    if not students:
        print("  No students to analyse.")
        return

    # total students
    total = len(students)

    # class average
    class_avg = sum(s.average() for s in students) / total

    # highest and lowest
    highest = max(students, key=lambda s: s.average())
    lowest  = min(students, key=lambda s: s.average())

    # grade distribution
    grade_count = {"A": 0, "B": 0, "C": 0, "D": 0, "F": 0}
    for s in students:
        grade_count[s.grade()] += 1

    # best subject (subject with highest class average)
    subject_totals = {}
    subject_counts = {}
    for s in students:
        for subject, score in s.marks.items():
            subject_totals[subject] = subject_totals.get(subject, 0) + score
            subject_counts[subject] = subject_counts.get(subject, 0) + 1

    best_subject = None
    best_avg     = -1
    for subject in subject_totals:
        avg = subject_totals[subject] / subject_counts[subject]
        if avg > best_avg:
            best_avg     = avg
            best_subject = subject

    # display
    print("-" * 50)
    print(f"  Total Students      : {total}")
    print(f"  Class Average       : {class_avg:.1f}")
    print(f"  Highest Scorer      : {highest.name} ({highest.average():.1f})")
    print(f"  Lowest Scorer       : {lowest.name} ({lowest.average():.1f})")
    print(f"\n  Grade Distribution  :")
    for grade, count in grade_count.items():
        bar = "█" * count
        print(f"    {grade} : {bar} ({count})")
    print(f"\n  Best Subject        : {best_subject} (Avg: {best_avg:.1f})")
    print("-" * 50)


# ────────────────────────────────────────────────────────────
#  MAIN MENU
# ────────────────────────────────────────────────────────────

def print_menu():
    """Prints the main menu options."""
    print("\n" + "=" * 40)
    print("   STUDENT MANAGEMENT SYSTEM")
    print("=" * 40)
    print("  1. Add new student")
    print("  2. View all students")
    print("  3. Search by roll number")
    print("  4. Delete a student")
    print("  5. Show top performer")
    print("  6. Show class statistics")
    print("  0. Exit")
    print("=" * 40)


def main():
    """Main function — loads data, runs menu loop, saves on exit."""
    students = load_all()
    print(f"\n  [✓] Loaded {len(students)} student(s) from file.")

    while True:
        print_menu()
        choice = input("  Enter your choice: ").strip()

        if   choice == "1":
            add_student(students)
            save_all(students)
        elif choice == "2":
            view_all(students)
        elif choice == "3":
            search_student(students)
        elif choice == "4":
            delete_student(students)
            save_all(students)
        elif choice == "5":
            top_performer(students)
        elif choice == "6":
            show_statistics(students)
        elif choice == "0":
            save_all(students)
            print("\n  Goodbye! Data saved. ✓\n")
            break
        else:
            print("  [!] Invalid choice. Please enter 0-6.")


# ───────────────────────────────────────────────────────────
if __name__ == "__main__":
    main()