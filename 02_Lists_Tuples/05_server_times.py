times = tuple([int(time) for time in input().split()])

while True:
    command = input()
    if command == "End":
        break

    parts = command.split()
    action = parts[0]

    if action == "Count":
        value = int(parts[1])

        print(times.count(value))

    elif action == "Index":
        value = int(parts[1])

        if value in times:
            print(times.index(value))
        else:
            print("Not found")

    elif action == "Contains":
        value = int(parts[1])

        print("Yes" if value in times else "No")  # Синтаксис за if-else на един ред

    elif action == "Stats":
        minimum = min(times)
        maximum = max(times)
        average = sum(times) / len(times)

        print(f"Min: {minimum}, Max: {maximum}, Average: {average:.2f}")

    elif action == "Print":
        print(times)
