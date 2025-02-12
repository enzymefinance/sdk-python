from decimal import Decimal


def to_decimal(value: int, decimals: int) -> Decimal:
    return Decimal(value) / Decimal(10**decimals)


def to_int(value: Decimal, decimals: int) -> int:
    return int(value * 10**decimals)
