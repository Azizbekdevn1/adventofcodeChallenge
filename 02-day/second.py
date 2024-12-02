# #Part1
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


# Part2
def is_safe(report):
    is_increasing = True
    is_decreasing = True

    for i in range(len(report) - 1):
        diff = report[i + 1] - report[i]

        # Check if the difference is not between 1 and 3
        if abs(diff) < 1 or abs(diff) > 3:
            return False

        # Determine if the sequence is not entirely increasing or decreasing
        if diff < 0:
            is_increasing = False
        elif diff > 0:
            is_decreasing = False

    return is_increasing or is_decreasing


def is_safe_with_dampener(report):
    if is_safe(report):
        return True

    for i in range(len(report)):
        modified_report = report[:i] + report[i + 1:]
        if is_safe(modified_report):
            return True

    return False


def process_reports(file_path):
    with open(file_path, 'r') as file:
        reports = file.readlines()

    safe_reports = 0

    for line in reports:
        report = list(map(int, line.split()))
        if is_safe_with_dampener(report):
            print(f"Safe: {report}")
            safe_reports += 1
        else:
            print(f"Unsafe: {report}")

    print(f"\nTotal Safe Reports (with Dampener): {safe_reports}")


file_path = "input.txt"
process_reports(file_path)
