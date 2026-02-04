import redis
from .connection import redisConnection

def search_server_cache(server_name: str, r: redis.Redis) -> str | None:
    """
    Search for a server in the Redis cache.

    Args:
        server (str): The server name to search for.

    Returns:
        str | None: The cached value if found, otherwise None.
    """
    cached_value = r.get(server_name)
    if cached_value:
        redisConnection.close()
    return cached_value


def cache_server_response(server_name: str, response: str, r: redis.Redis) -> bool:
    """
    Cache the server response in Redis.

    Args:
        server_name (str): The server name.
        response (str): The response to cache.
    """
    
    try:
        r.set(server_name, response)
        redisConnection.close()
        return True
    except Exception:
        return False