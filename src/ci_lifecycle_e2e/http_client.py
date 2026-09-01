import requests
import urllib3


def fetch_text(url: str) -> str:
    response = requests.get(url, timeout=5)
    response.raise_for_status()
    return response.text


def create_connection_pool() -> urllib3.PoolManager:
    return urllib3.PoolManager(num_pools=2)
