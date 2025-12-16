# Ако сте се затруднили, използвайте https://www.diffchecker.com/text-compare/
# да сравните текущия си код с примерното решение :)

raw_students = [
    {"name": "Daria", "points": "95"},
    {"name": "Ivan", "points": 82},
    {"name": "", "points": 70},
    {"name": "Maria", "points": "not available"},
    {"points": 50},
    {"name": "Gosho", "points": -10},
    None,
    {"name": "Stamat", "points": 120},
    {"name": "Ani", "points": "55"},
    "just a string",
]

SCHOLARSHIP_THRESHOLD = 80

normalized = []
invalid_count = 0

for i in range(len(raw_students)):
    record = raw_students[i]

    if not isinstance(record, dict):
        invalid_count = invalid_count + 1
        continue

    name = record.get("name", "")

    points = str(record.get("points", ""))

    if not name or not points.lstrip("-").isnumeric():
        invalid_count = invalid_count + 1
        continue

    points = int(points)

    if points > 100:
        points = 100

    if points < 0:
        points = 0

    normalized.append({
        "name": name,
        "points": points
    })

print("Normalized data:")

for s in normalized:
    print(s["name"], "->", s["points"])

print("Invalid records:", invalid_count)

print("\n--- Averages ---")

total_points = 0
passed_points = 0
passed_students = 0

for student in normalized:
    total_points += student["points"]
    if student["points"] >= SCHOLARSHIP_THRESHOLD:
        passed_points += student["points"]
        passed_students = passed_students + 1

overall_average = total_points / len(normalized)
passed_average = passed_points / passed_students

print(f"Overall average: {overall_average:.2f}")
print(f"Passed average: {passed_average:.2f}")

print("\n--- Scholarships ---")

for s in normalized:
    if s["points"] >= SCHOLARSHIP_THRESHOLD:
        print(s["name"], "gets scholarship")
    else:
        print(s["name"], "no scholarship")

print("\n--- Top student ---")

best_name = None
best_points = 0

for s in normalized:
    if s["points"] > best_points:
        best_name = s["name"]
        best_points = s["points"]

print("Best student:", best_name, "with", best_points, "points")

print("\n--- Final stats ---")
print("Total students:", len(raw_students))
print("Valid students:", len(normalized))
print("Invalid students:", len(raw_students) - len(normalized))
print("Scholarship threshold was:", SCHOLARSHIP_THRESHOLD)