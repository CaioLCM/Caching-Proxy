from .connection import app
import uvicorn
from ..cache.functions import search_server_cache, cache_server_response
from ..cache.connection import redisConnection
import requests
from fastapi import Header, Response

r = redisConnection.get_client()

def start_http_server(port: int, host: str):
    @app.get("/")
    def read_root(x_cache: str = Header(None)):
        try:
            if requests.get(host).status_code != 200:
                return {"error": "Host is unreachable"}
            content = search_server_cache(host, r)
            if content:
                return Response(content=content, headers={"x-cache": "HIT"})
                
            response = requests.get(host).text
            cache_server_response(host, response, r)
            return Response(content=response, headers={"x-cache": "MISS"})
        except requests.RequestException:
            return {"error": "An error occurred while trying to reach the host."}
    
    
    uvicorn.run(app, host="0.0.0.0", port=port)