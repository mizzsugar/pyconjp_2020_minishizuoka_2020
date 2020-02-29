import unittest
import src.calculate.calculate_1 as calculate


class TestCalculate(unittest.TestCase):
    def test_tax_should_be_included_in_sum(self):
        # 合計金額に8%の消費税も含まれて算出されるか確認
        item_1 = calculate.Item(name='sample_1', price=500)
        item_2 = calculate.Item(name='sample_2', price=1000)
        items = [item_1, item_2]
        actual = calculate.price(items)
        expected = 1620
        self.assertEqual(expected, actual)
