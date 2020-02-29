import unittest
import src.calculate.calculate_3 as calculate


class TestCalculate(unittest.TestCase):
    # テイクアウトかつ現金
    def test_calculate_sum_takeout_cash(self):
        item_1 = calculate.Item(name='sample_1', price=500)
        item_2 = calculate.Item(name='sample_2', price=1000)
        items = [item_1, item_2]
        actual = calculate.price(items, eat_in=False, cash_less=False)
        expected = 1620
        self.assertEqual(expected, actual)

    # イートインかつ現金
    def test_calculate_takeout_cash(self):
        item_1 = calculate.Item(name='sample_1', price=500)
        item_2 = calculate.Item(name='sample_2', price=1000)
        items = [item_1, item_2]
        actual = calculate.price(items, eat_in=True, cash_less=False)
        expected = 1650
        self.assertEqual(expected, actual)

    # テイクアウトかつキャッシュレス
    def test_calculate_sum_eatin_cash_less(self):
        item_1 = calculate.Item(name='sample_1', price=500)
        item_2 = calculate.Item(name='sample_2', price=1000)
        items = [item_1, item_2]
        actual = calculate.price(items, eat_in=False, cash_less=True)
        expected = 1539
        self.assertEqual(expected, actual)

    # イートインかつキャッシュレス
    def test_calculate_takeout_cash_less(self):
        item_1 = calculate.Item(name='sample_1', price=500)
        item_2 = calculate.Item(name='sample_2', price=1000)
        items = [item_1, item_2]
        actual = calculate.price(items, eat_in=True, cash_less=True)
        expected = 1567
        self.assertEqual(expected, actual)
