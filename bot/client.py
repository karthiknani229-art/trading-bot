import os
import logging
import time
from binance.client import Client
from dotenv import load_dotenv

load_dotenv()
logger = logging.getLogger(__name__)


class BinanceFuturesClient:
    def __init__(self):
        api_key = os.getenv("BINANCE_API_KEY")
        api_secret = os.getenv("BINANCE_API_SECRET")

        if not api_key or not api_secret:
            raise ValueError("API keys not found in environment variables")

        logger.info("Initializing Binance Futures Testnet client")


        self.client = Client(
            api_key,
            api_secret,
            testnet=True,
            requests_params={"timeout": 20},
        )


        self.client.FUTURES_URL = "https://testnet.binancefuture.com"


        try:
            server_time = self.client.get_server_time()["serverTime"]
            local_time = int(time.time() * 1000)
            self.client.timestamp_offset = server_time - local_time
            logger.info("Timestamp synchronized with Binance server")
        except Exception as e:
            logger.warning(f"Could not sync server time: {e}")

    def place_futures_order(self, **params):
        try:
            logger.info(f"Placing order: {params}")
            response = self.client.futures_create_order(**params)
            logger.info(f"Order response: {response}")
            return response
        except Exception as e:
            logger.exception("Error placing futures order")
            raise