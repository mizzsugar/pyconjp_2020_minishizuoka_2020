import dataclasses
from typing import Iterable


@dataclasses.dataclass(frozen=True)
class Item:
    name: str
    price: int


def price(items: Iterable[Item], eat_in: bool) -> int:
    if eat_in:
        return int(sum(item.price for item in items) * 1.1)
    return int(sum(item.price for item in items) * 1.08)
