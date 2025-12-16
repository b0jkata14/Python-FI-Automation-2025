raw_orders = [
    {"id": 1, "product": "Laptop", "price": "1200.50", "quantity": "2", "discount": 0.10},
    {"id": 2, "product": "Mouse", "price": "25", "quantity": 3, "discount": "0.2"},
    {"id": 3, "product": "Keyboard", "price": "-50", "quantity": 1, "discount": 0},
    {"id": 4, "product": "Monitor", "price": "300.99", "quantity": "abc", "discount": 0.15},
    {"id": 5, "product": "", "price": "49.90", "quantity": 1, "discount": 0},
    {"id": 6, "price": "10", "quantity": 5, "discount": 0},
    {"id": 7, "product": "Headphones", "price": None, "quantity": 2, "discount": 0.5},
    {"id": 8, "product": "USB Cable", "price": "5.5", "quantity": 0, "discount": 0},
    {"id": 9, "product": "Webcam", "price": "89.90", "quantity": 1, "discount": 1.5},
    "not even a dict",
    {"id": 10, "product": "Chair", "price": "80.00", "quantity": 1},
]

total_revenue = 0
valid_orders = 0
invalid_orders = 0
invalid_ids = []
processed = 0

FIELDS = ("id", "product", "price", "quantity", "discount")

for order in raw_orders:
    processed += 1
    is_invalid = False
    order_id = "(no id)"

    try:
        if not isinstance(order, dict):
            print("Invalid order format -> skipping")
            invalid_orders += 1
            continue

        order_id = order.get("id", "(no id)")

        missing = False

        for field in FIELDS:
            if field not in order:
                print(f"Order {order_id}: Missing field '{field}'")
                missing = True

        if missing:
            is_invalid = True
            continue

        product = order["product"]
        price = float(order["price"])
        quantity = int(order["quantity"])
        discount = float(order["discount"])

        if product == "":
            raise ValueError("Empty product name")

        if price <= 0:
            raise ValueError("Price must be positive")
        if quantity <= 0:
            raise ValueError("Quantity must be positive")
        if not (0 <= discount <= 0.8):
            raise ValueError("Discount must be between 0 and 0.8")

    except ValueError as e:
        print(f"Order {order_id}: Value error -> {e}")

        is_invalid = True

    except TypeError as e:
        print(f"Order {order_id}: Type error -> {e}")

        is_invalid = True

    else:
        total_price = price * quantity * (1 - discount)

        print(f"Order {order_id} processed successfully -> {total_price:.2f} lv")

        total_revenue += total_price
        valid_orders += 1

    finally:
        if is_invalid:
            invalid_orders += 1

            if order_id != "(no id)":
                invalid_ids.append(order_id)

        print(f"Finished processing order {order_id}\n")


print("\n--- REPORT ---")
print("Processed orders:", processed)
print("Valid orders:", valid_orders)
print("Invalid orders:", invalid_orders)
print(f"Total revenue: {total_revenue:.2f} lv")
print("Invalid order IDs:", invalid_ids)