measurements = list(map(int, input().split()))

while True:
    command = input()

    if command == "end":
        break

    if command.startswith("op "):
        operation = command.split()[1]

        if operation == "double":
            measurements = [x * 2 for x in measurements]

        elif operation == "shift_up":
            measurements = [x + 3 for x in measurements]

        elif operation == "to_positive":
            measurements = [abs(x) for x in measurements]

        else:
            print("Unknown operation")

    elif command == "summary":
        summary_dict = {
            "negative": sum(1 for x in measurements if x < 0),
            "zero":     sum(1 for x in measurements if x == 0),
            "positive": sum(1 for x in measurements if x > 0)
        }

        sorted_summary = sorted(
            summary_dict.items(),
            key=lambda item: (-item[1], item[0])
        )

        for category, count in sorted_summary:
            print(f"{category}: {count}")

    elif command == "print":
        print(*measurements)
