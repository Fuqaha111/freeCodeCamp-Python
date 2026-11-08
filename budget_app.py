class Category:
    def __init__(self, name):
        self.name = name
        self.leadger = []

    def deposit(self, amount, description=""):
        self.leadger.append({'amount': amount, 'description': description})

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.leadger.append({'amount': - amount, 'description': description})
            return True
        return False

    def get_balance(self):
        total = 0
        for i in self.leadger:
            total += i['amount']
        return total

    def transfer(self, amount, other):
        if self.check_funds(amount):
            self.leadger.append({'amount': -amount, 'description': f"Transfer to {other.name}"})
            other.leadger.append({'amount': amount, 'description': f"Transfer from {self.name}"})
            return True
        return False


    def check_funds(self, amount):
        if amount > self.get_balance():
            return False
        return True
    
    def __str__(self):
        title = f"{self.name:*^30}\n"
        items = ""
        for item in self.leadger:
            description = item['description'][:23]
            amount = item['amount']
            items += f"{description:<23}{amount:>7.2f}\n"
        total = f"Total: {self.get_balance()}"
            
        return title + items + total
        


def create_spend_chart(categories):
    pass



    
food = Category('Food')
food.deposit(1000, 'initial deposit')
food.withdraw(10.15, 'groceries')
food.withdraw(15.89, 'restaurant and more food for dessert')
clothing = Category('Clothing')
food.transfer(50, clothing)
print(food)























