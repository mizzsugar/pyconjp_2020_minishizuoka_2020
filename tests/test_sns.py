import unittest
import unittest.mock

import src.sns as sns


class TestSNS(unittest.TestCase):
    @unittest.mock.patch('some_sns_module.share')
    def test_share(self, mock_share):
        text = 'シェアしたい文字列'
        sns.send_share_sns(text, True)
        mock_share.assert_called_once_with(text)
