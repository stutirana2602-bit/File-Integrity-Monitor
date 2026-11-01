
import os
import hashlib
import json

FOLDER = "test_files"
BASELINE = "baseline.json"
REPORT = "security_report.txt"


def calculate_hash(file_path):
    sha256 = hashlib.sha256()

    with open(file_path, "rb") as file:
        for data in iter(lambda: file.read(4096), b""):
            sha256.update(data)

    return sha256.hexdigest()


def scan_files():
    results = {}

    for root, dirs, files in os.walk(FOLDER):
        for filename in files:
            path = os.path.join(root, filename)
            results[path] = calculate_hash(path)

    return results


def main():
    if not os.path.isdir(FOLDER):
        print("Create a test_files folder first.")
        return

    current = scan_files()

    if not os.path.exists(BASELINE):
        with open(BASELINE, "w") as file:
            json.dump(current, file, indent=4)

        print("Baseline created successfully!")
        return

    with open(BASELINE, "r") as file:
        old = json.load(file)

    added = current.keys() - old.keys()
    deleted = old.keys() - current.keys()
    modified = [
        path for path in current.keys() & old.keys()
        if current[path] != old[path]
    ]

    report = []

    for path in added:
        report.append(f"ADDED: {path}")

    for path in deleted:
        report.append(f"DELETED: {path}")

    for path in modified:
        report.append(f"MODIFIED: {path}")

    with open(REPORT, "w") as file:
        if report:
            file.write("\n".join(report))
        else:
            file.write("No file changes detected.")

    print("\n===== FILE INTEGRITY REPORT =====")

    for item in report:
        print(item)

    if not report:
        print("No file changes detected.")

    print("\nReport saved as", REPORT)


if __name__ == "__main__":
    main()
