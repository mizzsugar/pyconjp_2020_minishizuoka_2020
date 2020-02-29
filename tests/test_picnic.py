import unittest
import unittest.mock

import responses

import src.picnic


class TestPicnic(unittest.TestCase):
    @unittest.mock.patch('requests.get')
    def test_go_on_a_picnic_if_sunny(self, mock_request):
        mock_request.return_value = unittest.mock.Mock(
            status_code=200
        )
        # 他の項目も入れるべきかは後続の処理によります。
        mock_request.return_value.json.return_value = {
            '天気': '晴れ'
        }
        actual = src.picnic.go_picnic(1050004)
        expected = True
        self.assertEqual(expected, actual)


class TestPicnicWithResponses(unittest.TestCase):
    @responses.activate
    def test_go_on_a_picnic_if_sunny(self):
        responses.add(
            responses.GET,
            'https://tenki.example.com/today/1050004',
            json={'天気': '晴れ'},
            status=200)
        actual = src.picnic.go_picnic(1050004)
        expected = True
        self.assertEqual(expected, actual)
