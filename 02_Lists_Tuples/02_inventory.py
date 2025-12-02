items = input().split(", ")  # методът .split() връща списък, по подразбиране сплитва по 1 или няколко интервала

while True:
    command = input()
    if command == "End":
        break

    parts = command.split()
    action = parts[0]

    if action == "Add":
        item = parts[1]

        if item not in items:
            items.append(item)

    elif action == "Insert":
        item = parts[1]
        index = int(parts[2])

        if item not in items and 0 <= index < len(items):
            items.insert(index, item)

    elif action == "Remove":
        item = parts[1]

        if item in items:
            items.remove(item)

    elif action == "Swap":
        item1 = parts[1]
        item2 = parts[2]

        if item1 in items and item2 in items:
            i1 = items.index(item1)
            i2 = items.index(item2)

            items[i1], items[i2] = items[i2], items[i1]

print(items)
