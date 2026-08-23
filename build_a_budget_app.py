class Category:

    def __init__(self,name):
        self.name = name
        self.ledger = []
    
    def __str__(self):
        headline = f"{self.name:*^30}\n"
        entries = ""
        for l in self.ledger:
            desc = f"{l['description'][:23]:<23}"
            amt = f"{l['amount']:>7.2f}"
            entries += f"{desc}{amt}\n"
        total = f"Total: {self.get_balance():.2f}"
        return headline + entries + total

    def deposit(self, amount, description = ''):
        self.ledger.append({
            'amount':amount,
            'description': description
        })

    def withdraw(self, amount, description = ''):
        if self.check_funds(amount):
            self.ledger.append({
                'amount':amount*(-1),
                'description': description
            })
            return True
        return False

    def get_balance(self):
        total = 0
        for l in self.ledger:
            total += l['amount']
        return total
    
    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category.name}")
            category.deposit(amount, f"Transfer from {self.name}")
            return True
        return False
        
    
    def check_funds(self, amount):
        return amount <= self.get_balance()


def create_spend_chart(categories):
    chart = "Percentage spent by category\n"

    spending_cat = []
    total = 0

    for c in categories:
        current_spend = 0
        for l in c.ledger:
            amt = l["amount"]
            desc = l["description"]
            
            if amt < 0 and not desc.startswith("Transfer to"):
                current_spend += abs(amt)
        spending_cat.append(current_spend)
        total += current_spend
    
    perc = []

    for s in spending_cat:
        shift = (s / total) * 10
        rounding = int(shift) * 10
        perc.append(rounding)

    for row in range(100, -1, -10):
        chart += f"{row:>3}| "

        for p in perc:
            if p >= row:
                chart += "o  "
            else:
                chart += "   "

        chart += "\n"
    dash_count = 3 * len(categories) + 1
    chart += "    "
    chart += "-" * dash_count + "\n"

    max_length = max(len(c.name)for c in categories)

    for r in range(max_length):
        chart +="     "
        for c in categories:
            if r < len(c.name):
                chart += c.name[r] + "  "
            else:
                chart += "   "
        chart += "\n"

    return chart.rstrip("\n")

food = Category('Food')
food.deposit(1000, 'initial deposit')
food.withdraw(10.15, 'groceries')
food.withdraw(15.89, 'restaurant and more food for dessert')
clothing = Category('Clothing')

clothing = Category('Clothing')
clothing.deposit(500, 'initial deposit')
clothing.withdraw(50.00, 'new shoes')
clothing.withdraw(25.50, 't-shirt')

auto = Category('Auto')
auto.deposit(300, 'initial deposit')
auto.withdraw(60.00, 'gasoline')
auto.withdraw(15.00, 'car wash')

food.transfer(50, clothing)

print(food)
print(clothing)
print(auto)

my_categories = [food, clothing, auto]
print(create_spend_chart(my_categories))
