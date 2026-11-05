class Cart:
    def __init__(self) -> None:
        self.items = []

    def add(self, item):
        self.items.append(item)
    
    def remove (self, item):
        if item in self.items:
            self.items.remove(item)
        else:
           return f"{item} is not in cart"
    
    def list_items(self):
        return self.items

    def __len__(self):
        return len(self.items)
    
    def __contains__(self, item):
        return item in self.items
    
    def __getitem__(self, i):
        return self.items[i]

    
    def __iter__(self):
        return iter(self.items)
    
cart = Cart()
cart.add('Laptop')
cart.add('Wireless mouse')
cart.add('Ergo keyboard')
cart.add('Monitor')

for item in cart:
   print(item, end=' ') # Laptop Wireless mouse Ergo keyboard Monitor

print(f"\n{len(cart)}") # 4
print(cart[3]) # Monitor

print('Monitor' in cart) # True
print('banana' in cart) # False

cart.remove('Ergo keyboard')

print(cart.list_items()) # ['Laptop', 'Wireless mouse', 'Monitor']

print(cart.remove('banana')) # banana is not in cart
