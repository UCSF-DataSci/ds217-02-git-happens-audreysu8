
def load_students(filename):
    """
    Read a CSV file and return a list of student dictionaries.
    """
    students = []
    with open(filename, "r") as file:
        lines = file.readlines()

        headers = lines[0].strip().split(",")

        for line in lines[1:]:
            values = line.strip().split(",")
            student = dict(zip(headers, values))

            student["age"] = int(student["age"])
            student["grade"] = int(student["grade"])

            students.append(student)

    return students

def calculate_average_grade(students):
    total_grade = 0
    for student in students[1:]:
        total_grade += int(student["grade"])
    average = total_grade / (len(students) -1 )
    return average

def count_math_students(students):
    count = sum(1 for student in students[1:] if student["subject"] =='Math')
    return count

def generate_report():
    students = load_students('data/students.csv')
    avg_grade = calculate_average_grade(students)
    math_count = count_math_students(students)
    return f"Average grade of students: {avg_grade:.1f} and number of students enrolled in Math: {math_count}"

def save_report(report, filename):
    with open(filename, 'w') as f:
        f.write(report)

def main():
    students = load_students('data/students.csv')
    print("Loaded student data:")
    for student in students:
        print(student)
    save_report(generate_report(), 'output/analysis_report.txt')
    
if __name__ == "__main__":
    main()




