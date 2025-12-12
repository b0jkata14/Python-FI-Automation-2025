class PriceDiscountMixin:
    def apply_discount(self, percentage):
        if percentage < 0:
            percentage = 0
        elif percentage > 90:
            percentage = 90

        self.price = self.price * (1 - percentage / 100)


class Clothing(PriceDiscountMixin):
    def __init__(self, name, price, size):
        self.name = name
        self.price = price
        self.size = size


class Electronics(PriceDiscountMixin):
    def __init__(self, name, price, warranty):
        self.name = name
        self.price = price
        self.warranty = warranty


def apply_bulk_discount(products, percentage):
    for p in products:
        p.apply_discount(percentage)