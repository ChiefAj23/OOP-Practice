from abc import ABC, abstractmethod

class Item:
    def __init__(self, name, price, quantity=1):
        self.name = name
        self.price = price
        self.quantity = quantity

    def total(self):
        return self.price * self.quantity

class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        for it in self.items:
            if it.name == item.name and it.price == item.price:
                it.quantity += item.quantity
                return
        self.items.append(item)

    def subtotal(self):
        s = 0.0
        for it in self.items:
            s += it.total()
        return s

    def show(self):
        print("Cart:")
        if not self.items:
            print("  (empty)")
        for it in self.items:
            print(f"  {it.name}  ${it.price:.2f} x {it.quantity} = ${it.total():.2f}")
        print(f"Subtotal: ${self.subtotal():.2f}")

class DiscountRule(ABC):
    @abstractmethod
    def apply(self, cart):
        pass

    @abstractmethod
    def describe(self):
        pass

# Two example discount rules 10% off entire order(polymorphism)
class PercentageDiscount(DiscountRule):
    def __init__(self, percent):
        self.percent = percent

    def apply(self, cart):
        return cart.subtotal() * (self.percent / 100.0)

    def describe(self):
        return f"{self.percent}% off entire order"

# Buy 2 Get 1 Free on specific item
class BuyXGetYDiscount(DiscountRule):
    def __init__(self, item_name, buy_qty, free_qty):
        self.item_name = item_name
        self.buy_qty = buy_qty
        self.free_qty = free_qty

    def apply(self, cart):
        for it in cart.items:
            if it.name == self.item_name:
                group = self.buy_qty + self.free_qty
                if group <= 0:
                    return 0.0
                groups = it.quantity // group
                free_items = groups * self.free_qty
                return free_items * it.price
        return 0.0

    def describe(self):
        return f"Buy {self.buy_qty} Get {self.free_qty} Free on {self.item_name}"

class Checkout:
    def __init__(self, cart):
        self.cart = cart
        self.rules = []

    def add_discount(self, rule):
        self.rules.append(rule)

    def compute_total(self):
        sub = self.cart.subtotal()
        total_discount = 0.0
        applied = []
        for r in self.rules:
            amount = r.apply(self.cart)
            if amount > 0:
                applied.append((r.describe(), amount))
                total_discount += amount
        final_total = sub - total_discount
        if final_total < 0:
            final_total = 0.0
        return sub, applied, final_total

    def print_receipt(self):
        self.cart.show()
        sub, applied, total = self.compute_total()
        if applied:
            print("\nDiscounts:")
            for desc, amt in applied:
                print(f"  {desc}: -${amt:.2f}")
        print(f"\nFinal Total: ${total:.2f}")

def main():
    cart = ShoppingCart()
    cart.add_item(Item("Apple", 1.50, 5))
    cart.add_item(Item("Banana", 0.75, 6))
    cart.add_item(Item("Milk", 3.50, 2))

    checkout = Checkout(cart)
    checkout.add_discount(PercentageDiscount(10))# 10% off everything
    checkout.add_discount(BuyXGetYDiscount("Banana", 2, 1))# Buy 2 Get 1 free

    checkout.print_receipt()

    # for Open/Closed added a NEW discount without changing Cart or Checkout
    class FirstOrder15Off(DiscountRule):
        def apply(self, cart):
            return cart.subtotal() * 0.15
        def describe(self):
            return "First order 15% off"

    print("\n--- New customer example ---")
    new_cart = ShoppingCart()
    new_cart.add_item(Item("Laptop", 999.99, 1))
    new_checkout = Checkout(new_cart)
    new_checkout.add_discount(FirstOrder15Off())
    new_checkout.print_receipt()


if __name__ == "__main__":
    main()
