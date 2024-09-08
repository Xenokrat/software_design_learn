from typing import Protocol, Optional, List
import unittest


class IAverageCalculator(Protocol):
    @staticmethod
    def calculate_average(numberts: List[int]) -> float: ...

class AverageCalculator:
    @staticmethod
    def calculate_average(numbers: List[int]) -> float:
        if not numbers:
            raise ValueError("List should have at least 1 value")
        sum = 0
        count = 0
        for i in numbers:
            sum += i
            count += 1
        return sum / count


class TestAverageCalculator(unittest.TestCase):
    def setUp(self) -> None:
        self.avg_calc = AverageCalculator()

    def test_avg_calc_ok(self) -> None:
        res = self.avg_calc.calculate_average([1, 2, 3, 4])
        self.assertEqual(res, 2.5)

    def test_avg_calc_emptyavg_calcay(self) -> None:
        with self.assertRaises(ValueError) as _:
            self.avg_calc.calculate_average([])
        
# Без 100% покрытия тесами мы могли бы не предусмотреть поведение
# функции когда ей на вход передаётся пустой массив 
# (можно было бы вернуть и NULL, но например в реализации этой же функции
# в Питоновском модуле statistics поднимается исключение)


if __name__ == "__main__":
    unittest.main()
