from functions.functions import my_sum, my_subtract, my_divide, my_multiply
import unittest


class TestSum(unittest.TestCase):

    def test_my_sum(self):
        self.assertEqual(my_sum(5, 6), 11)

    def test_my_subtract(self):
        self.assertEqual(my_subtract(5, 6), -1)

    def test_my_divide(self):
        self.assertEqual(my_divide(12, 6), 2.0)

    def test_my_multiply(self):
        self.assertEqual(my_multiply(5, 6), 30)


if __name__ == '__main__':
    unittest.main()
