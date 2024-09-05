from typing import Protocol
import unittest
from unittest.mock import MagicMock, Mock


MAX_BALANCE = 100_000_000


class BankAccount:
    def __init__(self, balance: float) -> None:
        self._balance = 0.0 if balance <= 0.0 else balance
        self._deposit_status = 0
        self._withdraw_status = 0

    def deposit(self, amount: float) -> None:
        if amount <= 0.0:
            print(f"Error: deposit amount should be positive")
            self._deposit_status = 0
            return

        new_balance = self._balance + amount
        if new_balance >= MAX_BALANCE:
            print(f"Error: new balance is exceeding limit: {MAX_BALANCE}")
            self._deposit_status = 0
            return

        self._balance = new_balance
        self._deposit_status = 1

    def withdraw(self, amount: float) -> None:
        if amount <= 0.0:
            print(f"Error: withdraw amount should be positive")
            self._withdraw_status = 0
            return

        new_balance = self._balance - amount
        if new_balance < 0:
            print(f"Error: you have not enough money to withdraw")
            self._withdraw_status = 0
            return

        self._balance = new_balance
        self._withdraw_status = 1

    def get_balance(self) -> float:
        return self._balance

    def get_deposit_status(self) -> int:
        return self._deposit_status

    def get_withdraw_status(self) -> int:
        return self._withdraw_status


class TestBankAccount(unittest.TestCase):
    def setUp(self) -> None:
        self._bank_acc = BankAccount(100.0)

    def test_deposit_ok(self) -> None:
        self._bank_acc.deposit(110.3)
        self.assertEqual(210.3, self._bank_acc.get_balance())
        self.assertTrue(self._bank_acc.get_deposit_status() == 1)

    def test_withdraw_ok(self) -> None:
        self._bank_acc.withdraw(51.1)
        self.assertEqual(48.9, self._bank_acc.get_balance())
        self.assertTrue(self._bank_acc.get_withdraw_status() == 1)

    def test_deposit_exceeding_limit(self) -> None:
        self._bank_acc.deposit(100_000_000.0)
        self.assertTrue(self._bank_acc.get_balance() == 100.0)
        self.assertTrue(self._bank_acc.get_deposit_status() == 0)

    def test_deposit_neg_amount(self) -> None:
        self._bank_acc.deposit(-100.0)
        self.assertTrue(self._bank_acc.get_balance() == 100.0)
        self.assertTrue(self._bank_acc.get_deposit_status() == 0)

    def test_withdraw_exceeding_limit(self) -> None:
        self._bank_acc.withdraw(200.0)
        self.assertTrue(self._bank_acc.get_balance() == 100.0)
        self.assertTrue(self._bank_acc.get_withdraw_status() == 0)

    def test_withdraw_neg_amount(self) -> None:
        self._bank_acc.withdraw(-100.0)
        self.assertTrue(self._bank_acc.get_balance() == 100.0)
        self.assertTrue(self._bank_acc.get_withdraw_status() == 0)


if __name__ == "__main__":
    unittest.main()
