n = int(input())
cameras = []

for _ in range(n):
    x, y = [int(num) for num in input().split()]  # Списък от два елемента, който се разопакова и отива към x и y
    cameras.append((x, y))

while True:
    command = input()
    if command == "End":
        break

    parts = command.split()
    action = parts[0]

    if action == "Get":
        index = int(parts[1])

        if 0 <= index < len(cameras):
            x, y = cameras[index]  # Разопаковане
            print(f"X: {x}, Y: {y}")

    elif action == "Move":
        print("Error: cameras are immutable")

    elif action == "Count":
        print(len(cameras))

    elif action == "List":
        print(cameras)
