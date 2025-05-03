import unittest

from src.addition import add


class TestAddition(unittest.TestCase):
    def test_add_positive_numbers(self):
        self.assertEqual(add(2, 3), 5)

    def test_add_negative_numbers(self):
        self.assertEqual(add(-2, -3), -5)

    def test_add_mixed_sign_numbers(self):
        self.assertEqual(add(-2, 3), 1)

    def test_add_zero(self):
        self.assertEqual(add(0, 5), 5)
        self.assertEqual(add(5, 0), 5)

    def test_add_large_numbers(self):
        self.assertEqual(add(1000000, 2000000), 3000000)
        self.assertEqual(add(-1000000, -2000000), -3000000)


if __name__ == "__main__":
    unittest.main()
