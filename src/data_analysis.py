
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
    for student in students:
        total_grade += int(student["grade"])
    average = total_grade / len(students)
    return average

def calculate_total_studens(students):
    total_students = 0
    for student in students:
        total_students += 1
    return total_students

def count_math_students(students):
    count = sum(1 for student in students if student["subject"] =='Math')
    return count

def count_science_students(students):
    count = sum(1 for student in students if student["subject"] =='Science')
    return count

def count_history_students(students):
    count = sum(1 for student in students if student["subject"] =='History')
    return count

def generate_report():
    students = load_students('data/students.csv')
    total_students = calculate_total_studens(students)
    avg_grade = calculate_average_grade(students)
    math_count = count_math_students(students)
    science_count = count_science_students(students)
    history_count = count_history_students(students)
    return f"Analysis: Average grade of students: {avg_grade:.1f}.\nTotal number of students: {total_students}.\nNumber of students enrolled in Math: {math_count}. Number of students enrolled in Science: {science_count}. Number of students enrolled in History: {history_count}."

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




