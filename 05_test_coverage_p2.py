from typing import Protocol, List
import unittest


class IGradeCalculator(Protocol):
    @staticmethod
    def calculate_average(grades: List[float]) -> float: ...

class GradeCalculator:

    @staticmethod
    def calculate_average(grades: List[float]) -> float:
        """Скажем, оценки студентов могут находиться в диапазоне от 0.0 до 100.0"""
        if not grades:
            raise ValueError("List should have at least 1 value")
        sum = 0.
        count = 0
        for i in grades:
            if not (0. <= i <= 100.):
                raise ValueError(f"Value {i} is not within allowed diapason of values")
            sum += i
            count += 1
        return sum / count


class TestAverageCalculator(unittest.TestCase):
    def setUp(self) -> None:
        self.grade_calc = GradeCalculator()

    def test_grade_calc_ok(self) -> None:
        """Корректно считает валидный список оценок"""
        res = self.grade_calc.calculate_average([75., 68., 95., 98.])
        self.assertEqual(res, 84.0)

    def test_grade_calc_none_argument(self) -> None:
        """Ошибка при передачи None"""
        with self.assertRaisesRegex(ValueError, "at least 1 value"):
            self.grade_calc.calculate_average(None)

    def test_grade_calc_empty_grade_list(self) -> None:
        """Ошибка при передачи пустого листа"""
        with self.assertRaisesRegex(ValueError, "at least 1 value"):
            self.grade_calc.calculate_average([])

    def test_grade_calc_negative_grades(self) -> None:
        """Ошибка при обработке негативных оценок"""
        with self.assertRaisesRegex(ValueError, "allowed diapason"):
            self.grade_calc.calculate_average([-82.0, 54.1, 91.1])

    def test_grade_calc_over_limit_grades(self) -> None:
        """Ошибка при обработке превышающих лимит оценок"""
        with self.assertRaisesRegex(ValueError, "allowed diapason"):
            self.grade_calc.calculate_average([102.0, 82.0, 77.0])
        

if __name__ == "__main__":
    unittest.main()
