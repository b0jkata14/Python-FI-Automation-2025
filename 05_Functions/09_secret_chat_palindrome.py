def is_palindrome(text):
    if len(text) <= 1:
        return True

    if text[0] != text[-1]:
        return False

    return is_palindrome(text[1:-1])


def reverse_text(text):
    if text == "":
        return ""

    return text[-1] + reverse_text(text[:-1])


raw_text = input()

clean = raw_text.replace(" ", "").lower()


if is_palindrome(clean):
    print("Palindrome")
else:
    print("Not palindrome")

print(f"Reversed: {reverse_text(clean)}")
