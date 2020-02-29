import unittest
import src.calculate.calculate_2 as calculate


class TestCalculate(unittest.TestCase):
    def test_calculate_sum_eatin(self):
        item_1 = calculate.Item(name='sample_1', price=500)
        item_2 = calculate.Item(name='sample_2', price=1000)
        items = [item_1, item_2]
        actual = calculate.price(items, eat_in=False)
        expected = 1620
        self.assertEqual(expected, actual)

    def test_calculate_takeout(self):
        item_1 = calculate.Item(name='sample_1', price=500)
        item_2 = calculate.Item(name='sample_2', price=1000)
        items = [item_1, item_2]
        actual = calculate.price(items, eat_in=True)
        expected = 1650
        self.assertEqual(expected, actual)
