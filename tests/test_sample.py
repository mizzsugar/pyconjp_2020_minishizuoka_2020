import unittest

import src.sample


class TestSample(unittest.TestCase):
    def test_get_num(self):
        src.sample.randint = unittest.mock.Mock(return_value=1)
        actual = src.sample.get_num()
        expected = 1
        self.assertEqual(actual, expected)
