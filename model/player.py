
class Player:
    def __init__(self):
        self.balance = 1000.0
        self.name = "Juan David"

    def get_balance(self):
        return self.balance

    def bet(self,amount):
        self.balance -= amount

    def earn(self,amount):
        self.balance += amount

    def get_name(self,):
        return self.name

    def print_balance(self,):
        print(f"Balance: ${self.balance}")
