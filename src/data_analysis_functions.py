def load_data(filename):
    """
    Checks if file is .csv or not. If it is, read a CSV file and return a list of student dictionaries.
    """
    if not filename.endswith(".csv"):
        raise ValueError("Unsupported file extension. Please provide a .csv file.")
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

def load_csv(filename):
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

students = load_csv('data/students.csv')
print(students)

def analyze_data(students):
    student_dictionary = {}
    student_dictionary["highest_grade"] = max(student['grade'] for student in students)
    student_dictionary["lowest_grade"] = min(student['grade'] for student in students)
    subject_counts = {}

    for student in students:
        subject = student["subject"]
        if subject in subject_counts.keys():
            subject_counts[subject] += 1 
        else:
            subject_counts[subject] = 1 
    
    student_dictionary["subject_counts"] = subject_counts
    return student_dictionary

print(analyze_data(students))

def analyze_grade_distribution(students):
    def letter_form(grade):
        if grade >= 90:
            return "A"
        elif grade >= 80:
            return "B"
        elif grade >= 70:
            return "C"
        elif grade >= 60:
            return "D"
        else:
            return "F"
    
    def grade_distribution(students):
        distribution = {"A": 0, "B": 0, "C": 0, "D": 0, "F": 0}

        for student in students:
            grade = student["grade"]
            cat = letter_form(grade)
            distribution[cat] += 1

        return distribution

    def percentage_converter(distribution):
        for key in distribution:
            percent = (distribution[key] / len(students)) * 100  
            distribution[key] = f"{percent:.1f}%" 
        return distribution  
    
    return percentage_converter(grade_distribution(students))   

print(analyze_grade_distribution(students))

def save_results(filename):
    def generate_report():
        students = load_csv('data/students.csv')
        analyzed_data = analyze_data(students)
        analyzed_grade_distribtion = analyze_grade_distribution(students)
        return f"\nDictionary with multiple statistics: {analyzed_data} and Dictionary with grade distribution: {analyzed_grade_distribtion}"
    report = generate_report()
    with open(filename, 'a') as f:
        f.write(report)

def main():
    students = load_csv('data/students.csv')
    analyze_data(students)
    analyze_grade_distribution(students)
    save_results('output/analysis_report.txt')


if __name__ == "__main__":
    main()



