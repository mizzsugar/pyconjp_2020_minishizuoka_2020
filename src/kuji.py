import random


def kuji() -> str:
    is_lucky = random.choice([True, False])
    if is_lucky:
        return 'あたり'
    return 'はずれ'
