class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = list()

    def __str__(self) -> str:
        len_ast = (15-(len(str(self.name))/2)) if len(str(self.name))/2 == 0 else ((15-(len(str(self.name))/2))+0.5)
        title = F"{'*'*int(len_ast)}{self.name}{'*'*(int(len_ast))}"
        items = ''
        for l in self.ledger:
            dsc = l["description"]
            amnt = l["amount"]
            if len(dsc) > 23:
                dsc = dsc[:23]
            items += F"{dsc:<23}{amnt:>7}\n"
        total = F"Total: {self.get_balance()}"
        return F"{title}\n{items}\n{total}"
        
    def deposit(self, amount: float, description=''):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount: float, description=''):
        if self.check_funds(amount):
            self.ledger.append(
                {"amount": amount*-1, "description": description})
            return True
        else:
            return False

    def transfer(self, amount: float, category) -> bool:
        if self.check_funds(amount):
            self.withdraw(amount, F'Transfer to { category.name }')
            category.deposit(amount, F"Transfer from {self.name}")
            return True

        return False

    def check_funds(self, amount: float) -> bool:
        balance = self.get_balance()
        if balance >= amount:
            return True

        return False

    def get_balance(self) -> float:
        sum = 0.0
        for l in self.ledger:
            sum += l["amount"]

        return sum

# def create_spend_chart(categories):
    
