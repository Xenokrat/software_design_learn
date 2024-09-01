from typing import Protocol
import unittest
from unittest.mock import MagicMock, Mock

class IPaymentProcessor(Protocol):
    def process_payment(self, amount: float) -> None: ...


class CreditCardProcessor:
    def process_payment(self, amount: float) -> None:
        print(f"Processing credit card payment of ${amount}")


class PayPalProcessor:
    def process_payment(self, amount: float) -> None:
        print(f"Processing PayPal payment of ${amount}")


class BankTransferProcessor:
    def process_payment(self, amount: float) -> None:
        print(f"Processing bank transfer payment of ${amount}")


class PaymentService:
    def __init__(self, payment_processor: IPaymentProcessor) -> None:
        self._payment_processor = payment_processor

    def process_payment(self, amount: float) -> None:
        self._payment_processor.process_payment(amount)

    def set_payment_processor(self, payment_processor: IPaymentProcessor) -> None:
        self._payment_processor = payment_processor


class PaymentProcessorTest(unittest.TestCase):
    def setUp(self) -> None:
        self._credit_card_processor = CreditCardProcessor()
        self._pay_pal_processor = PayPalProcessor()
        self._bank_transfer_processor = BankTransferProcessor()

    def test_credit_card_processor(self) -> None:
        try:
            self._credit_card_processor.process_payment(100.0)
        except Exception as e:
            self.fail(f"credit_card_processor raises: {e}")

    def test_pay_pal_processor(self) -> None:
        try:
            self._pay_pal_processor.process_payment(100.0)
        except Exception as e:
            self.fail(f"pay_pal_processor raises: {e}")

    def test_bank_transfer_processor(self) -> None:
        try:
            self._bank_transfer_processor.process_payment(100.0)
        except Exception as e:
            self.fail(f"bank_transfer_processor raises: {e}")


class OrderService:
    def __init__(self, payment_processor: IPaymentProcessor) -> None:
            self._PAYMENT_PROCESSOR = payment_processor

    def process_order(self, amount: float) -> None:
        print("Processing order...")
        self._PAYMENT_PROCESSOR.process_payment(amount)
        print("Order processed.")


class MockPaymentProcessor:
    def __init__(self) -> None:
        self._payment_processed = False

    def process_payment(self, amount: float) -> None:
        self._payment_processed = True
        print(f"Fake processing payment of ${amount}")

    def is_payment_processed(self) -> bool:
        return self._payment_processed


class OrderServiceTest(unittest.TestCase):
    def test_process_order(self) -> None:
        mock_payment_processor = MockPaymentProcessor()
        order_service = OrderService(mock_payment_processor)
        order_service.process_order(100.0)
        self.assertTrue(mock_payment_processor.is_payment_processed)


class BankAccount:
    def __init__(self, balance: float) -> None:
        self._balance = balance

    def deposit(self, amount: float) -> None:
        self._balance += amount

    def withdraw(self, amount: float) -> None:
        self._balance -= amount

    def get_balance(self) -> float:
        return self._balance


class TestBankAccount(unittest.TestCase):
    def setUp(self) -> None:
        self._bank_acc = BankAccount(100.0)

    def test_deposit_ok(self) -> None:
        self._bank_acc.deposit(100.0)
        self.assertEqual(200.0, self._bank_acc.get_balance())

    def test_withdraw_ok(self) -> None:
        self._bank_acc.withdraw(50.0)
        self.assertEqual(50.0, self._bank_acc.get_balance())

    def test_deposit_not_ok(self) -> None:
        # Показывает, что метод может обрабатывать отрицательные суммы, а это неправильно
        self._bank_acc.deposit(-200.0)
        self.assertTrue(self._bank_acc.get_balance() >= 0)

    def test_withdraw_not_ok(self) -> None:
        # Показывает, что метод баланс может оказаться отрицательным при снятии денег, а это плохо
        self._bank_acc.withdraw(1000.0)
        self.assertTrue(self._bank_acc.get_balance() >= 0)


if __name__ == "__main__":
    unittest.main()
