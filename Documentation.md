---
title: "Documentation for Assignment 2"
output: github_document
---

# DataSci Week 02 Integration Project

## Project Overview
The purpose of this project is to combine three skills — using Git for version control, using the command line to automate setup, and writing Python code to process data into one assignment.

## Project Structure
datasci-week02-integration/ ├── .github │ ├──test │ │ └── requirements.txt │ └── test_assignment.py ├── workflows │ └── classroom.yml ├── data/ │ ├── students.csv └── output/ └── analysis_report.txt ├── src/ │ ├── data_analysis.py │ └── data_analysis_functions.py├── .gitignore 

## Features
- **Project Scaffold**: Here, I do automatic project initialization using `setup_project.sh`
- **Data Processing**: Python programs for analyzing student grades
- **Git Workflow**: Developing features on separate branches and merging them into `main`

## Usage
1. Run `./setup_project.sh` to initialize the project layout
2. Execute `python src/data_analysis.py` for initial analysis
3. Run `python src/data_analysis_functions.py` for more comprehensive analysis

## Git Workflow
| Branch | Purpose | Status |
|--------|---------|--------|
| main | Production code | Active |
| feature/project-scaffold | CLI automation | Merged |
| feature/data-processing | Python analysis | Merged |