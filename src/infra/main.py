from .cache.connection import redisConnection
from .server.functions.main import search_server_cache, cache_server_response

class ProxyExecutor:
    redis_client = redisConnection()
    r = redis_client.get_client()
    def __init__(self, redis_client):
        self.redis_client = redis_client
        self.r = redis_client.get_client()
        
    def execute_proxy(self, server_name: str):
        cached_response = search_server_cache(server_name, self.r)
        if cached_response:
            return cached_response
        # Here you would normally fetch the response from the actual server
        response = f"Response from {server_name}"
        cache_server_response(server_name, response, self.r)
        return response