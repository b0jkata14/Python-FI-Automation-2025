def calculate_price(base_price: float, **modifiers):
    price = base_price

    for modifier, value in modifiers.items():
        if modifier == "tax":
            price = price * (1 + value)

        elif modifier == "discount":
            price = price * (1 - value)

        elif modifier == "early_bird":
            price = price * (1 - value)

        else:
            price = price + value

    return price


n = int(input())

for _ in range(n):
    parts = input().split()
    base_price = float(parts[0])

    kwargs = {}
    for part in parts[1:]:
        key, val = part.split("=")
        kwargs[key] = float(val)

    final_price = calculate_price(base_price, **kwargs)
    print(f"Final price: {final_price:.2f}")
