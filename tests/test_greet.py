import datetime
import unittest

from freezegun import freeze_time

import src.greet


class TestGreet(unittest.TestCase):
    @freeze_time('2019-10-01 05:00:00')
    def test_morning_1(self):
        # 引数をもたない関数でのテストです。
        expected = 'おはようございます'
        self.assertEqual(expected, src.greet.greet_1())

    def test_morning_2(self):
        # 引数をもつ関数でのテストです。
        expected = 'おはようございます'
        self.assertEqual(
            expected,
            src.greet.greet_2(
                lambda: datetime.datetime(2019, 10, 1, 5, 0, 0, 0)
            )
        )
