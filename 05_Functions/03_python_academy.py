def calculate_average(*scores):
    return sum(scores) / len(scores)


def classify_student(average, min_pass=60):
    if average >= 90:
        return "Excellent"
    elif 80 <= average <= 89:
        return "Very Good"
    elif average >= min_pass:
        return "Pass"
    else:
        return "Fail"


n = int(input())

setting = input().strip()

if setting.startswith("New"):
    min_pass = int(setting.split()[1])
else:
    min_pass = 60

students = []

for _ in range(n):
    parts = input().split()
    name = parts[0]
    scores = list(map(int, parts[1:]))

    avg = calculate_average(*scores)
    status = classify_student(avg, min_pass)

    students.append((name, avg, status))
    print(f"Student {name}: {avg:.2f} -> {status}")

overall_average = sum(s[1] for s in students) / n

best_student = max(students, key=lambda x: x[1])
best_name, best_avg, _ = best_student

failed_count = sum(1 for s in students if s[2] == "Fail")

print(f"Overall average: {overall_average:.2f}")
print(f"Best student: {best_name} with {best_avg:.2f}")
print(f"Failed students: {failed_count}")
