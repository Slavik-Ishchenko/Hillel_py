import uuid
import datetime


class BankAccount:
    name_account = str()
    _id = str(uuid.uuid4())
    balance = float()
    transactions = []

    def __init__(self, name='Name is missing :(((', uid=uuid.uuid4()):
        self.name_account = name
        self.id = uid
        self.balance = 0.00
        self.transactions = []

    def deposit(self, amount):
        self.balance = self.balance + amount - (amount * 0.01)
        self.transactions.append(self.balance)
        self.transactions.append('deposit')

    def withdrawal_of_funds(self, amount):
        self.balance = self.balance - amount - (amount * 0.01)
        self.transactions.append(self.balance)
        self.transactions.append('withdrawal')

    def show_balance(self):
        return self.balance

    def show_transactions(self):
        date = datetime.datetime.now().strftime("%d.%m.%Y")
        self.transactions.append(date)
        return self.transactions


b = BankAccount()
b.deposit(100)
print(b.show_transactions())
