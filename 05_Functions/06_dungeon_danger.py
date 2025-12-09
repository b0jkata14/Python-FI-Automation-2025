def create_danger_calculator(mode):
    if mode == "casual":
        monsters_weight = 2
        traps_weight = 3
        depth_weight = 1
    else:
        monsters_weight = 3
        traps_weight = 4
        depth_weight = 2

    def calculate_danger(monsters, traps, depth):
        return monsters * monsters_weight + traps * traps_weight + depth * depth_weight

    return calculate_danger


mode = input()
calculate = create_danger_calculator(mode)

room_name, m, t, d = input().split()
score = calculate(int(m), int(t), int(d))

print(f"{room_name} -> {score}")
