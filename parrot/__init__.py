NUM_COURSES = 20
students = []

def calculate_mean(grades):
    return sum(grades) / len(grades)

def calculate_median(grades):
    sorted_grades = sorted(grades)
    mid = len(sorted_grades) // 2
    return (sorted_grades[mid] + sorted_grades[~mid]) / 2  # ~mid handles both odd and even cases

def calculate_mode(grades):
    frequency = {grade: grades.count(grade) for grade in set(grades)}
    max_freq = max(frequency.values())
    modes = [grade for grade, freq in frequency.items() if freq == max_freq]
    return modes[0] if len(modes) == 1 else "No unique mode"

def add_student():
    name = input("Enter the student's name: ")
    grades = [float(input(f"Course {i + 1}: ")) for i in range(NUM_COURSES)]
    students.append({'name': name, 'grades': grades, 'average': calculate_mean(grades)})
    print("Student grades added successfully.")

def display_records():
    for student in students:
        print(f"\nStudent Name: {student['name']}\nGrades: {', '.join(f'{g:.2f}' for g in student['grades'])}\nAverage: {student['average']:.2f}")

def display_summary():
    all_grades = [g for s in students for g in s['grades']]
    print("\n--- Summary ---")
    print(f"Mean: {calculate_mean(all_grades):.2f}")
    print(f"Median: {calculate_median(all_grades):.2f}")
    print(f"Mode: {calculate_mode(all_grades)}")

def main():
    while True:
        add_student()
        if input("\nAdd more? (1 - Yes, 0 - No): ").strip() == '0':
            if len(students) < 5:
                print("Insufficient records. Minimum required is 5 students.")
            else:
                display_records()
                display_summary()
            break

if __name__ == "__main__":
    main()
