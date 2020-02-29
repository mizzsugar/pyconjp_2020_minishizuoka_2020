import dataclasses
from typing import Iterable


@dataclasses.dataclass(frozen=True)
class Item:
    name: str
    price: int


def price(items: Iterable[Item]) -> int:
    return int(sum(item.price for item in items) * 1.08)
