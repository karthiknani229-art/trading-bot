import logging

logger = logging.getLogger(__name__)


def build_order_params(symbol, side, order_type, quantity, price=None):
    params = {
        "symbol": symbol,
        "side": side,
        "type": order_type,
        "quantity": quantity,
    }

    if order_type == "LIMIT":
        params.update({
            "price": price,
            "timeInForce": "GTC",
        })

    logger.info(f"Built order params: {params}")
    return params


def format_order_output(response: dict) -> str:
    return f"""
===== ORDER RESPONSE =====
Order ID     : {response.get('orderId', 'N/A')}
Status       : {response.get('status', 'N/A')}
Executed Qty : {response.get('executedQty', 'N/A')}
Avg Price    : {response.get('avgPrice', 'N/A')}
"""