# Student Fee Management System (PS No. 43)

## Project overview
A menu-driven Python console application for maintaining student fee records. It supports student registration, full or partial fee payments, fee-status checking, searching by roll number, and listing pending dues.

## Objectives
- Maintain student fee records using dictionaries.
- Calculate total fees and outstanding dues.
- Accept valid full and partial payments.
- Reject zero, negative, and above-due payments.
- Save and reload records using a text file.

## Features
1. Add a student with roll number, name, and course.
2. Pay fees in full or in part.
3. Search a student by roll number.
4. Display students with pending dues.
5. Persist records in `fees.txt`.

## Course fee table

| Course | Total fee |
|---|---:|
| BCA | 45000 |
| BTECH | 60000 |
| MBA | 80000 |

Fee status rules:
- `Unpaid`: paid amount is 0.
- `Partial`: paid amount is greater than 0 and less than total fee.
- `Paid`: due amount is 0.

## Requirements
- Python 3.8 or newer.
- No third-party Python packages are required to run `one.py`.

## Files
- `one.py`: complete single-file application.
- `README.md`: project documentation.
- `fees.txt`: persistent data file (CSV-formatted text; created/updated automatically).
- `screenshots/`: test-case input/output evidence.
- `Test_Case_Results.pdf`: combined test screenshots/report.

## Execution instructions
1. Keep `one.py` and `fees.txt` in the same folder.
2. Open a terminal in that folder.
3. Run:

   ```bash
   python one.py
   ```

4. Choose a menu option from 1 to 5.
5. Use option 5 to exit. Records are saved after each successful add/payment and again on exit.

## Input format
- Option 1 (Add): enter roll number, student name, then course (`BCA`, `BTECH`, or `MBA`).
- Option 2 (Pay): enter roll number and payment amount as a whole number.
- Option 3 (Search): enter roll number.
- Option 4 (Pending dues): no additional input.
- Option 5 (Exit): no additional input.

## Test cases and expected results

### Test Case 1 - Normal input
Input:
```text
Menu option: 1
Roll: 101
Name: Riya
Course: BCA
```
Expected key output:
```text
Student added: 101 |Riya |BCA |Total Fee: 45000|Paid:0|Due:45000|Status:Unpaid
```

### Test Case 2 - Boundary/minimum payment (full payment)
Starting record: roll 101, Riya, BCA, paid 0.
Input:
```text
Menu option: 2
Roll: 101
Amount: 45000
```
Expected key output:
```text
Payment received. Paid:45000|Due:0|Status: Paid
```

### Test Case 3 - Invalid payment above due
Starting record: roll 101, Riya, BCA, paid 0.
Input:
```text
Menu option: 2
Roll: 101
Amount: 50000
```
Expected key output:
```text
Amount exceeds due (45000). Payment rejected.
```

### Test Case 4 - Partial payment and pending dues
Starting record: roll 102, Aman, BTECH, paid 0.
Input:
```text
Menu option: 2
Roll: 102
Amount: 20000
Menu option: 4
```
Expected key output:
```text
Payment received. Paid:20000|Due:40000|Status: Partial
102|Aman|Due:40000
```

## Testing notes
The four scenarios are run independently with the exact initial records described above. Test Cases 2 and 3 both require roll 101 to begin with paid amount 0, so they must not be run sequentially against the same modified data file. The screenshot evidence and PDF show the actual program execution for each scenario.

## Data file format
Each line in `fees.txt` contains four CSV fields:
`Roll,Name,Course,Paid`

Example:
```text
101,Riya,BCA,20000
```

Do not manually change a student's paid amount beyond the course fee. Back up `fees.txt` before manually editing records.
Project Mentor




Mentored by: Mr. Satyaprakash Sethy

GitHub: "@SATYAPRAKASHSETHY" (https://github.com/SATYAPRAKASHSETHY)

Role: Python Mentor / Technical Guide

Special thanks to Mr. Satyaprakash Sethy for his valuable mentorship and technical guidance throughout this project.
