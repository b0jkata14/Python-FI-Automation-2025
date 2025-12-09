def is_clean(message, banned_words):
    for word in banned_words:
        if word in message:
            return False
    return True


banned_words = input().split(", ")
n = int(input())

blocked_count = 0

for i in range(1, n + 1):
    message = input()

    if is_clean(message, banned_words):
        print(f"Message {i}: OK")
    else:
        blocked_count += 1
        print(f"Message {i}: Blocked")


print(f"Blocked messages: {blocked_count}")
