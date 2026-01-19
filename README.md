# Dataset Management and Basic Analysis System

A Python program that reads numerical and categorical data from CSV files, performs statistical analysis, and generates reports.

## Overview

This project demonstrates fundamental Python programming concepts including:

- Variables and File Handling
- Error Handling
- Functions
- Operators and Loops
- Conditional Statements
- Sets
- Object-Oriented Programming (OOP)
- File Output

## Features

### 1. Numerical Data Analysis

- Reads numerical data from a CSV file
- Calculates statistical measures:
  - **Total**: Sum of all values
  - **Average**: Mean of all values
  - **Minimum**: Smallest value
  - **Maximum**: Largest value

### 2. Categorical Data Analysis

- Extracts unique categories from a CSV file using sets
- Displays the total count of unique categories

### 3. Performance Evaluation

- Compares average value against a threshold
- Displays "High Performance" if average exceeds threshold
- Displays "Needs Improvement" if average is below threshold

### 4. Error Handling

- Handles missing files gracefully
- Validates empty files
- Checks for invalid (non-numeric) data

### 5. Report Generation

- Saves all statistics and analysis results to a text file

## Files

- `dataset_analysis.py` - Main Python program
- `student_marks.csv` - Sample numerical data (student marks)
- `courses.csv` - Sample categorical data (course names)
- `analysis_report.txt` - Generated analysis report (created after running)

## Requirements

- Python 3.x (no external dependencies required)

## Usage

### Basic Usage

1. Make sure you have the data files (`student_marks.csv` and `courses.csv`) in the same directory.

2. Run the program:

   ```bash
   python dataset_analysis.py
   ```

3. The program will:
   - Load numerical data from `student_marks.csv`
   - Calculate statistics (total, average, minimum, maximum)
   - Load categorical data from `courses.csv`
   - Extract unique categories
   - Display results on screen
   - Save results to `analysis_report.txt`

### Customizing the Threshold

You can modify the performance threshold by editing the `main()` function in `dataset_analysis.py`:

```python
dataset = DataSet(
    data_file='student_marks.csv',
    categorical_file='courses.csv',
    threshold=85  # Change this value
)
```

### Using Your Own Data Files

1. Create a CSV file with numerical data (one value per line):

   ```sh
   85
   92
   78
   ```

2. Create a CSV file with categorical data (one category per line):

   ```sh
   Category1
   Category2
   Category1
   ```

3. Update the file names in the `main()` function or pass them directly when creating the DataSet object.

## Program Structure

### DataSet Class

The `DataSet` class contains the following methods:

- `__init__(data_file, categorical_file, threshold)` - Initialize the dataset
- `load_data()` - Load numerical data from CSV file
- `calculate_total(dataset)` - Calculate sum of values
- `calculate_average(dataset)` - Calculate mean of values
- `calculate_minimum(dataset)` - Find minimum value
- `calculate_maximum(dataset)` - Find maximum value
- `calculate_statistics()` - Calculate all statistics
- `load_categories()` - Load and extract unique categories
- `display_results()` - Display analysis results
- `save_results(output_file)` - Save results to file

## Example Output

```sh
Successfully loaded 15 data points
Successfully loaded 4 unique categories

==================================================
DATASET ANALYSIS RESULTS
==================================================
Total data points: 15
Total: 1286.0
Average: 85.73
Minimum: 73.0
Maximum: 95.0

Performance: High Performance
(Average 85.73 is above threshold 85)

--------------------------------------------------
CATEGORICAL DATA ANALYSIS
--------------------------------------------------
Total unique categories: 4
Unique categories: ['Biology', 'Chemistry', 'Mathematics', 'Physics']
==================================================
```

## Concepts Demonstrated

### 1. Variables & File Handling

- Reading data from CSV files
- Storing data in lists and sets

### 2. Error Handling

- `try-except` blocks for file operations
- Handling `FileNotFoundError` for missing files
- Handling `ValueError` for invalid data

### 3. Functions

- Separate functions for each calculation
- Functions take dataset as input and return results

### 4. Operators & Loops

- Arithmetic operators: `+`, `-`, `*`, `/`
- Comparison operators: `<`, `>`
- `for` loops to traverse datasets
- Loops used for:
  - Adding values (total calculation)
  - Comparing values (min/max finding)
  - Counting data points (average calculation)

### 5. Conditional Statements

- `if-else` statements for performance evaluation
- Comparison of average against threshold

### 6. Sets

- Using Python `set` to store unique categories
- Automatic handling of duplicates

### 7. Object-Oriented Programming

- `DataSet` class with methods
- Object instantiation and method calls
- Encapsulation of data and methods

### 8. File Output

- Writing results to a text file
- Formatted report generation

## Error Handling Examples

The program handles various error scenarios:

1. **Missing File**: Displays error message and exits gracefully
2. **Empty File**: Detects and reports empty files
3. **Invalid Data**: Identifies non-numeric values and reports them

## Testing

To test the program with different scenarios:

1. **Test with missing file**: Rename `student_marks.csv` temporarily
2. **Test with empty file**: Create an empty CSV file
3. **Test with invalid data**: Add non-numeric values to the CSV file

## License

See LICENSE file for details.
