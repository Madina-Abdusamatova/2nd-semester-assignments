class StockItem:
    def __init__(self, name: str, price: float, quantity: int):
        self.name = name
        self.price = price
        self.quantity = quantity
    def __str__(self):
        return f"{self.name}: {self.quantity} in stock at ${self.price}"
    def __repr__(self):
        return f"StockItem('{self.name}', {self.price}, {self.quantity})"
    def __add__(self, other):
        if isinstance(other, StockItem):
            if self.name == other.name:
                return StockItem(self.name, self.price, self.quantity + other.quantity)
            else:
                return NotImplemented       
        if isinstance(other, int):
            return StockItem(self.name, self.price, self.quantity + other)        
        return NotImplemented
    def __eq__(self, other):
        if isinstance(other, StockItem):
            return self.name == other.name and self.price == other.price
        return NotImplemented
    def __bool__(self):
        return self.quantity > 0
       
item1 = StockItem("Apples", 2.5, 10)
item2 = StockItem("Apples", 2.5, 15)
item3 = StockItem("Bananas", 3.0, 0)

print(str(item1))
print(repr(item1))
print(item1 + item2)
print(item1 + 5)
print(item1 == item2)
print(bool(item1))
print(bool(item3))