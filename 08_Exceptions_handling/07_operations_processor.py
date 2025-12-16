class OperationError(Exception):
    pass


class ParseError(OperationError):
    pass


class UnsupportedOperationError(OperationError):
    pass


class OperandParseError(OperationError):
    pass


class ZeroDivisionOperationError(OperationError):
    pass


class ExecutionError(OperationError):
    pass


def parse_operation(line):
    parts = line.split()

    if len(parts) != 3:
        raise ParseError(f"Expected 3 parts, got {len(parts)}")

    op, s1, s2 = parts[0], parts[1], parts[2]

    if op not in {"ADD", "SUB", "MUL", "DIV"}:  # не е речник а множество (set)
        raise UnsupportedOperationError(f"Unsupported operation '{op}'")

    try:
        a = float(s1)
    except (ValueError, TypeError):
        raise OperandParseError(f"Cannot parse operand '{s1}'")

    try:
        b = float(s2)
    except (ValueError, TypeError):
        raise OperandParseError(f"Cannot parse operand '{s2}'")

    if op == "DIV" and b == 0:
        raise ZeroDivisionOperationError("Division by zero")

    return op, a, b


def execute_operation(op: str, a: float, b: float) -> float: 
    # : str и : float са type hints (подсказки за типа)
    # те НЕ влияят на изпълнението на програмата
    # използват се само за по-лесно четене и разбиране на кода
    if op == "ADD":
        return a + b
    if op == "SUB":
        return a - b
    if op == "MUL":
        return a * b
    if op == "DIV":
        if b == 0:
            raise ZeroDivisionOperationError("Division by zero")
        return a / b

    raise UnsupportedOperationError(f"Unsupported operation '{op}'")


def safe_execute(line):
    try:
        op, a, b = parse_operation(line)
        return execute_operation(op, a, b)
    except OperationError as e:
        raise ExecutionError(f"Failed to execute: '{line}'") from e


lines = [
    "ADD 5 10",
    "SUB 10 3",
    "MUL a 5",
    "DIV 10 0",
    "UNKNOWN 1 2",
    "ADD 7",
]

for line in lines:
    try:
        result = safe_execute(line)
    except ExecutionError as e:
        cause = e.__cause__
        print(f"[ERROR] {e}")
        print(f"   Root cause: {type(cause).__name__}: {cause}")
    else:

        print(f"[OK] {line} = {result:.1f}")
