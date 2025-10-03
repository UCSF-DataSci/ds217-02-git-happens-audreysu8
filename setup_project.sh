#!/bin/bash

echo "Creating needed directories"
mkdir -p src data output

echo "Create .gitignore and requirements.txt..."

cat > .gitignore << 'EOF'
.env/
__pycache__/
*.pyc

EOF
cat > requirements.txt << 'EOF'
# DataSci 217 - Lecture 02 Assignment Requirements
# Git Workflow, CLI Automation, and Python Data Processing

# Core Python packages (built-in, no external dependencies required)
# This assignment focuses on fundamental Python concepts and file I/O

# Testing framework
pytest>=7.0.0

# Optional: For enhanced development experience
# pathlib (built-in since Python 3.4)
# json (built-in)
# csv (built-in)
# subprocess (built-in)
# os (built-in)
# sys (built-in)

# Note: This assignment is designed to use only Python standard library
# to focus on core programming concepts without external dependencies
EOF


cat > data/students.csv << 'EOF'
name,age,grade,subject
Alice,20,85,Math
Bob,19,92,Science
Charlie,21,78,English
Diana,20,88,Math
Eve,22,95,Science
Frank,19,82,History
Grace,21,91,Math
Henry,20,76,Science
EOF

echo "Now, I'll create the Python templates"
cat <<EOL > src/data_analysis.py
def load_students(filename):
    """Load student data from CSV."""
    # TODO: Open file, read lines, skip header
    # TODO: Split each line by comma
    # TODO: Return list of student data
    pass

def calculate_average_grade(students):
    """Calculate average grade."""
    # TODO: Sum all grades
    # TODO: Divide by number of students
    pass

def count_math_students(students):
    """Count students in Math."""
    # TODO: Count students where subject is Math
    pass

def generate_report():
    """Generate report string."""
    # TODO: Create formatted string with results
    # TODO: Use f-strings with .1f for decimals
    pass

def save_report(report, filename):
    """Save report to file."""
    # TODO: Create output directory if needed
    # TODO: Write report to file
    pass

def main():
    # TODO: Load data
    # TODO: Calculate statistics
    # TODO: Generate and save report
    pass

if __name__ == "__main__":
    main()
EOL

cat <<EOL > src/data_analysis_functions.py
def load_data(filename):
    """Load data from CSV file."""
    # TODO: Check file extension
    # TODO: Call appropriate loader
    pass

def load_csv(filename):
    """Load CSV data."""
    # TODO: Same technique as basic script
    pass

def analyze_data(students):
    """Analyze student data."""
    # TODO: Calculate multiple statistics
    # TODO: Return dictionary of results
    pass

def analyze_grade_distribution(grades):
    """Count grades by letter grade."""
    # TODO: Count A (90-100), B (80-89), etc.
    pass

def generate_report():
    """Generate comprehensive report."""
    # TODO: Create formatted string with results.
    pass
    
def save_results(results, filename):
    """Save detailed results."""
    # TODO: Format and write comprehensive report
    pass

def main():
    # TODO: Orchestrate the analysis
    pass

if __name__ == "__main__":
    main()
EOL

# 5️⃣ Make the script itself executable
chmod +x setup_project.sh

echo "And now setup_project.sh is executable. Setup complete!"