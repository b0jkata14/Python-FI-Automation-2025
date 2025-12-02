readings = input().split()  # Връща списък
sensor_type = input()

filtered = [r for r in readings if r.startswith(sensor_type + ":")]  # Методът .startswith() проверява дали започва

print(filtered)
