import redis

class RedisConnection:
    def __init__(self, host='localhost', port=6379, db=0):
        self._client = redis.Redis(host=host, port=port, db=db, decode_responses=True)

    def get_client(self):
        return self._client

    def close(self):
        self._client.close()

redisConnection = RedisConnection()