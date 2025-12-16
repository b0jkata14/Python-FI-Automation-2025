class BookingError(Exception):
    pass


class MissingFieldError(BookingError):
    pass


class InvalidAirportError(BookingError):
    pass


class PriceParseError(BookingError):
    pass


class NegativePriceError(BookingError):
    pass


ALLOWED_AIRPORTS = {"SOF", "VAR", "BOJ"}  # Това НЕ е речник (dictionary), а е множество (set)
# set (множество) – колекция от уникални стойности, няма дубликати
# използва се тук, за да проверяваме бързо дали даден код на летище е позволен


def validate(line):
    parts = line.split(";")

    if len(parts) != 3:
        raise MissingFieldError()

    ticket_id, airport, price_raw = parts[0], parts[1], parts[2]

    if airport not in ALLOWED_AIRPORTS:
        raise InvalidAirportError()

    try:
        price = float(price_raw)
    except (ValueError, TypeError):
        raise PriceParseError()

    if price < 0:
        raise NegativePriceError()

    return {"ticket_id": ticket_id, "airport": airport, "price": price}


def process(lines: list[str]) -> None:
    for line in lines:
        try:
            validate(line)
            print(f"[OK] {line}")
        except BookingError as e:
            print(f"[ERROR] {line} - {e.__class__.__name__}")


data = [
    "T1;SOF;120",
    "T2;INVALID;100",
    "T3;VAR;-10",
    "BROKEN LINE",
    "T4;BOJ;50",
    "T5;VAR;abc"
]

process(data)