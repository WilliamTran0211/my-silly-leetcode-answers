from typing import List
from collections import defaultdict


class Bank:

    def __init__(self, balance: List[int]):
        self.data = defaultdict(int)
        for i, m in enumerate(balance):
            self.data[i + 1] = m

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if account1 not in self.data:
            return False
        balance_acc1 = self.data[account1]
        if account2 in self.data.keys() and balance_acc1 >= money:
            self.data[account2] += money
            self.data[account1] -= money
            return True
        return False

    def deposit(self, account: int, money: int) -> bool:
        if account in self.data.keys():
            self.data[account] += money
            return True
        return False

    def withdraw(self, account: int, money: int) -> bool:
        if account not in self.data:
            return False
        balance_acc = self.data[account]
        if balance_acc >= money:
            self.data[account] -= money
            return True
        return False


bank = Bank([10, 100, 20, 50, 30])
print(bank.withdraw(3, 10))
print(bank.transfer(5, 1, 20))
print(bank.deposit(5, 20))
print(bank.transfer(3, 4, 15))
print(bank.withdraw(10, 50))
