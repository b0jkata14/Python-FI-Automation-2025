class Product:
    def __init__(self, name, category, price, quantity):
        self.name = name
        self.category = category
        self.price = price
        self.quantity = quantity if quantity >= 0 else 0

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value < 0:
            value = 0

        self._price = value

    @property
    def total_value(self):
        return self.price * self.quantity

    def __repr__(self):
        return f"Product({self.name}, {self.category}, {self.price}, {self.quantity})"


class Inventory:
    def __init__(self, products=None):
        self.products = list(products) if products is not None else []

    def add_product(self, new_product):
        for product in self.products:
            if product.name == new_product.name and product.category == new_product.category:
                product.quantity += new_product.quantity
                return

        self.products.append(new_product)

    def remove_product(self, name, quantity):
        if quantity < 0:
            quantity = 0

        for product in self.products:
            if product.name == name:
                product.quantity = max(product.quantity - quantity, 0)
                return

    @staticmethod
    def apply_discount(price, percent):
        if percent < 0:
            percent = 0
        elif percent > 90:
            percent = 90

        return price * (1 - percent / 100)

    def discount_category(self, category, percent):
        for product in self.products:
            if product.category == category:
                product.price = self.apply_discount(product.price, percent)

    def get_low_stock(self, threshold):
        filtered_products = [pr for pr in self.products if pr.quantity <= threshold]

        return sorted(
            filtered_products,
            key=lambda pr: (pr.quantity, pr.name)
        )

    def most_valuable(self, n):
        return sorted(
            self.products,
            key=lambda pr: (-pr.total_value, pr.name)
        )[:n]

    def search_by_prefix(self, prefix):
        filtered_products = [pr for pr in self.products if pr.name.lower().startswith(prefix.lower())]

        return sorted(
            filtered_products,
            key=lambda pr: pr.name
        )