from typing import Optional


VALID_SIDES = {"BUY", "SELL"}
VALID_TYPES = {"MARKET", "LIMIT"}


def validate_order_inputs(
    symbol: str,
    side: str,
    order_type: str,
    quantity: float,
    price: Optional[float],
):
    if not symbol:
        raise ValueError("Symbol is required")

    side = side.upper()
    if side not in VALID_SIDES:
        raise ValueError("Side must be BUY or SELL")

    order_type = order_type.upper()
    if order_type not in VALID_TYPES:
        raise ValueError("Order type must be MARKET or LIMIT")

    if quantity <= 0:
        raise ValueError("Quantity must be greater than 0")

    if order_type == "LIMIT":
        if price is None:
            raise ValueError("Price is required for LIMIT orders")
        if price <= 0:
            raise ValueError("Price must be greater than 0")

    return symbol.upper(), side, order_type, quantity, price