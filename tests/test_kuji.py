import random
import unittest
import unittest.mock

import src.kuji


class TestKuji(unittest.TestCase):
    def test_win_if_is_lucky(self):
        random.choice = unittest.mock.Mock(return_value=True)
        actual = src.kuji.kuji()
        expected = 'あたり'
        self.assertEqual(expected, actual)

    @unittest.mock.patch('random.choice')
    def test_win_if_is_lucky_patch(self, mock_choice):
        mock_choice.return_value = True
        actual = src.kuji.kuji()
        expected = 'あたり'
        self.assertEqual(expected, actual)
