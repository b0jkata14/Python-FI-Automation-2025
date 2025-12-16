responses = ["10", "7", "abc", None, "-1", "  8  ", {}, "12", "5"]

valid = []
invalid_count = 0

for r in responses:
    try:
        value = int(r)
    except (TypeError, ValueError):
        invalid_count += 1
        continue

    if value < 0 or value > 10:
        invalid_count += 1
    else:
        valid.append(value)

average = sum(valid) / len(valid)

print("Valid:", valid)
print("Invalid:", invalid_count)
print("Average satisfaction:", round(average, 2))