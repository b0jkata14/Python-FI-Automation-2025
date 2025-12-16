class SafeDivisionError(Exception):
    pass


def safe_divide(a, b):
    try:
        return a / b
    except Exception as e:
        raise SafeDivisionError("Division failed") from e


tests = [
    (10, 2),
    (5, 0),
    ("a", 3),
]

for x, y in tests:
    try:
        result = safe_divide(x, y)
    except SafeDivisionError as e:
        cause = e.__cause__
        print(f"Error: {e}")
        print(f"  Root cause: {type(cause).__name__}: {cause}")
    else:
        print(f"Result = {result}")