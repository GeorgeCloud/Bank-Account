from random import randint
bank_accounts = []


class BankAccount:
    def __init__(self, full_name):
        self.full_name      = full_name
        self.account_number = int(''.join(["{}".format(randint(0, 9)) for num in range(0, 8)])) # 8 digit number, unique per account.
        self.balance        = 0



george_account = BankAccount('George Ceja')
