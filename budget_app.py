class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append({'amount': amount, 'description': description})

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({'amount': - amount, 'description': description})
            return True
        return False

    def get_balance(self):
        total = 0
        for i in self.ledger:
            total += i['amount']
        return total

    def transfer(self, amount, other):
        if self.check_funds(amount):
            self.ledger.append({'amount': -amount, 'description': f"Transfer to {other.name}"})
            other.ledger.append({'amount': amount, 'description': f"Transfer from {self.name}"})
            return True
        return False


    def check_funds(self, amount):
        if amount > self.get_balance():
            return False
        return True
    
    def __str__(self):
        title = f"{self.name:*^30}\n"
        items = ""
        for item in self.ledger:
            description = item['description'][:23]
            amount = item['amount']
            items += f"{description:<23}{amount:>7.2f}\n"
        total = f"Total: {self.get_balance():.2f}"
            
        return title + items + total
        


def create_spend_chart(categories):
    #calculating percentage
    spent = []
    for category in categories:
        total = 0
        for money in category.ledger:
            if money['amount'] < 0:
                total += -money['amount']
        spent.append(total)
    
    total_spent = sum(spent)
    percentages = []
    for s in spent:
        s = (s * 100 / total_spent) // 10 * 10
        percentages.append(s)

    #BarChat

    chart = "Percentage spent by category\n"
    for level in range(100, -1, -10):
        chart += (f"{level:>3}|")
        for percent in percentages:
            if percent >= level:
                chart += (f" o ")
            else:
                chart += ("   ")
        chart += " \n"

    # comlumn names
    longest = max(len(c.name) for c in categories)
    len_of_cat = (len(categories) * 3 + 1) * "-"
    chart += "    " + len_of_cat
    chart += "\n"
    for i in range(longest):
        chart += "     "
        for c in categories:
            if i < (len(c.name)):
                chart += c.name[i] + "  "
            else:
                chart += "   "
        chart += "\n"
        
        
    return chart.rstrip("\n")
    




"""
You should have a function outside the Category class named create_spend_chart(categories) that takes a list of categories and returns a bar-chart string. To build the chart:

Start with the title Percentage spent by category.
Calculate percentages from withdrawals only and not from deposits. The percentage should be the percentage of the amount spent for each category to the total spent for all categories (rounded down to the nearest 10).
Label the y-axis from 100 down to 0 in steps of 10.
Use o characters for the bars.
Include a horizontal line two spaces past the last bar.
Write category names vertically below the bar.
This function will be tested with up to four categories.

Make sure to match the spacing of the example output exactly:
"""
    
food = Category('Food')
food.deposit(1000, 'initial deposit')
food.withdraw(10.15, 'groceries')
food.withdraw(15.89, 'restaurant and more food for dessert')
clothing = Category('Clothing')
food.transfer(50, clothing)
print(food)

brushes = Category('brushes')
brushes.deposit(500, 'initial deposit')
brushes.withdraw(13.2, '250')
brushes.withdraw(15.89, 'restaurant and more food for dessert')
clothing = Category('Clothing')
food.transfer(50, clothing)
print(food)


print(create_spend_chart([food, brushes, clothing]))






















