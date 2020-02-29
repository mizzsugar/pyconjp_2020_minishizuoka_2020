import datetime
from typing import Final


def greet_1() -> str:
    """日時を引数にもたないバージョンです"""
    now: Final = datetime.datetime.now()
    if 5 <= now.hour < 12:
        return 'おはようございます'
    elif 12 <= now.hour < 18:
        return 'こんにちは'
    return 'こんばんは'


def greet_2(time=datetime.datetime.now) -> str:
    """日時を引数にもつバージョンです。

    datetime.datetime.now()にすると、関数を定義した日時が利用されるため、
    日時を返す関数を渡して関数内で実行しています。
    """
    now: Final = time()
    if 5 <= now.hour < 12:
        return 'おはようございます'
    elif 12 <= now.hour < 18:
        return 'こんにちは'
    return 'こんばんは'
