import os
import sys

class Account:
    def __init__(self, filepath):
        self.filepath = filepath
        with open(filepath, 'r') as file:
            content = file.read().strip()
            self.balance = float(content) if content else 0.0
    
    def withdraw(self, amount):
        if amount > self.balance:
            print('No tienes suficiente saldo')
        else:
            self.balance -= amount
            self._commit()
    
    def deposit(self, amount):
        self.balance += amount
        self._commit()
    
    def _commit(self):
        with open(self.filepath, 'w') as file:
            file.write(str(self.balance))


class Checking:
    def __init__(self, filepath, fee):
        self.account = Account(filepath)
        self.fee = fee
    
    def transfer(self, amount):
        if amount > self.account.balance:
            print('No tienes suficiente saldo para transferir')
        else:
            self.account.balance -= amount - self.fee

def get_account_path():
    dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(dir, 'balance.txt')

if __name__ == '__main__':
    account = Account(get_account_path())
    print(account.balance)
    account.deposit(100)
    print(account.balance)
    account.withdraw(50)
    print(account.balance)