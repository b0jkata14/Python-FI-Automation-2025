passwords = input().split()

result = ["valid" if len(p) > 6 else "invalid" for p in passwords]

print(result)
