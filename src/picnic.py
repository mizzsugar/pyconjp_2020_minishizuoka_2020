import http

import requests


def go_picnic(postal_code: str) -> bool:
    request_url = f'https://tenki.example.com/today/{postal_code}'
    response = requests.get(request_url)
    if response.status_code == http.HTTPStatus.NOT_FOUND:
        raise ValueError
    if response.json().get('天気') == '晴れ':
        return True
    return False
