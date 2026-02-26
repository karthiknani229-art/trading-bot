import argparse
import logging

from bot.logging_config import setup_logger
from bot.validators import validate_order_inputs
from bot.client import BinanceFuturesClient
from bot.orders import build_order_params, format_order_output

def main():
    setup_logger()
    logger = logging.getLogger("cli")

    parser = argparse.ArgumentParser(description="Binance Futures Testnet Trading Bot")

    parser.add_argument("--symbol", required=True)
    parser.add_argument("--side", required=True)
    parser.add_argument("--type", required=True)
    parser.add_argument("--quantity", required=True, type=float)
    parser.add_argument("--price", type=float)

    args = parser.parse_args()

    try:
        symbol, side, order_type, quantity, price = validate_order_inputs(
            args.symbol,
            args.side,
            args.type,
            args.quantity,
            args.price,
        )

        print("\n" + "=" * 30)
        print("===== ORDER SUMMARY =====")
        print("=" * 30)
        print(f"Symbol   : {symbol}")
        print(f"Side     : {side}")
        print(f"Type     : {order_type}")
        print(f"Quantity : {quantity}")
        if price:
            print(f"Price    : {price}")
        if price:
            print(f"Price    : {price}")

        client = BinanceFuturesClient()
        params = build_order_params(symbol, side, order_type, quantity, price)
        response = client.place_futures_order(**params)

        print(format_order_output(response))
        print("\n✅ Order placed successfully")

    except Exception as e:
        logger.exception("Order failed")
        print(f"\n❌ Error: {e}")


if __name__ == "__main__":
    main()