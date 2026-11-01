# File Integrity Monitoring System

## 1. Introduction
This project is a Python-based File Integrity Monitoring System. It detects changes in files using SHA-256 hashing.

## 2. Objective
- Monitor important files.
- Detect modified files.
- Identify newly added files.
- Detect deleted files.

## 3. Technologies Used
- Python
- VS Code
- SHA-256
- Hashlib
- JSON

## 4. Features
- Calculates SHA-256 file hashes.
- Creates an original file baseline.
- Detects added, modified and deleted files.
- Generates a security report.

## 5. How to Run

1. Install Python.
2. Create a folder named `test_files`.
3. Add files inside it.
4. Run:

```bash
python monitor.py
```

5. Modify, add or delete a file and run the program again.

## 6. Output
The program displays detected file changes and saves them in `security_report.txt`.

## 7. Learning Outcomes
- Understanding file integrity.
- Learning SHA-256 hashing.
- Practising Python programming.
- Understanding basic security monitoring.

## 8. Safety and Limitations
This is a beginner learning project. It monitors only the configured test folder and compares files against a locally stored baseline. Protect the baseline file because an attacker who changes it could affect detection.

## 9. Future Improvements
- Add email alerts.
- Add real-time monitoring.
- Create a graphical dashboard.