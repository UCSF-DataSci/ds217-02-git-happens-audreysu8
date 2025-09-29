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
# TODO: Need to add data analysis here
def sample_function():
    pass
def sample_function_2():
    pass

# TODO: Then add a main function to orchestrate analysis
def main():
    pass

if __name__ == "__main__":
    main()
EOL

cat <<EOL > src/data_analysis_functions.py
# TODO: Need to add extra data analysis functions here
def sample_function():
    pass
def sample_function_2():
    pass

# TODO: Then add a main function to orchestrate analysis
def main():
    pass

if __name__ == "__main__":
    main()
EOL

# 5️⃣ Make the script itself executable
chmod +x setup_project.sh

echo "And now setup_project.sh is executable. Setup complete!"