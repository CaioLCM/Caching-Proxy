from .infra.http.main import start_http_server
import click

@click.command()
@click.option('--port', default='8080', help='Port to run the caching proxy on.')
@click.option('--url', default='http://example.com', help='URL to cache.')
@click.option('--clear_cache', is_flag=True, help='Clear the cache before starting the server.')
def main(port, url, clear_cache):
    if clear_cache:
        from .infra.cache.connection import redisConnection
        r = redisConnection.get_client()
        r.flushall()
        print("Cache cleared.")
    else:
        start_http_server(port=port, host=url)
    
if __name__ == "__main__":
    main()