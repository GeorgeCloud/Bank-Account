from random import randint
bank_accounts = []

class BankAccount:
    def __init__(self, full_name):
        self.full_name      = full_name
        self.account_number = int(''.join(["{}".format(randint(0, 9)) for num in range(0, 8)])) # 8 digit number, unique per account.
        self.balance        = 0

    def __str__(self):
        return f'''
        Account Full Name:{self.full_name}
        Account No.: {''.join(["*", "*", "*", "*"] + list(str(self.account_number))[:4])}
        Balance: {self.balance}
        '''

    def deposit(self, amount):
        self.balance += amount
        print(f'Amount deposited: ${amount} new balance: ${self.balance}')

    def get_balance(self):
        return self.balance

    def add_interest(self):
        self.balance += self.balance * 0.00083


george_account = BankAccount('George Ceja')

print(george_account)
