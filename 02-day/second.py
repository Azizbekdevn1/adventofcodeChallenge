def is_safe(report):
    for i in range(len(report) - 1):
        diff = report[i + 1] - report[i]
        if not (1 <= abs(diff) <= 3):
            return False
    return all(report[i] < report[i + 1] for i in range(len(report) - 1)) or \
        all(report[i] > report[i + 1] for i in range(len(report) - 1))


def process_reports(file_path):
    with open(file_path, 'r') as file:
        reports = file.readlines()

    safe_reports = 0

    for line in reports:
        report = list(map(int, line.split()))
        if is_safe(report):
            print(f"Safe: {report}")
            safe_reports += 1
        else:
            print(f"Unsafe: {report}")

    print(f"\nTotal Safe Reports: {safe_reports}")


# Specify the path to your input.txt
file_path = "input.txt"
process_reports(file_path)
