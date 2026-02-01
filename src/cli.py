import click

@click.command()
@click.option('--port', default='8080', help='Port to run the caching proxy on.')
@click.option('--url', default='http://example.com', help='URL to cache.')
def main(port, url):
    click.echo(f"This is the main function of the caching proxy CLI. Port: {port}, URL: {url}")
    
if __name__ == "__main__":
    main()