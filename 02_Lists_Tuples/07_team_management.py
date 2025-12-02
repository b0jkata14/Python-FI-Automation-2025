employees = input().split(", ")

while True:
    command = input()
    if command == "End":
        break

    parts = command.split()
    action = parts[0]

    if action == "AddTeam":
        employees.extend(parts[1:])  # Взимаме от втория ел., защото първият е командата

    elif action == "FireLast":
        count = int(parts[1])

        if count >= len(employees):
            employees.clear()
        else:
            employees = employees[:-count]

    elif action == "SortAZ":
        employees.sort()

    elif action == "SortZA":
        employees.sort(reverse=True)

    elif action == "Reverse":
        employees.reverse()

    elif action == "Clear":
        employees.clear()

for e in employees:
    print(e)
