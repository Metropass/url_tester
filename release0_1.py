import click
import urllib3
import re
from colorama import Fore
import sys


@click.group()
def cli():
    pass
    
@cli.command('url')
@click.argument('url')
def meme2(url):
    """this reads a url"""
    try:
        link = urllib3.PoolManager()
        res = link.request('HEAD', url)
        if(res.status == 200):
            print(Fore.GREEN + f"{url}  passes with {res.status}!")
        elif (res.status == 403):
            print(Fore.BLACK + f"{url} looks sus, it returned {res.status}")
        else:
            print(Fore.RED + f"{url} is dead, as it returned {res.status}")
    except OSError:
        print("The file cannot be opened! Make sure this file can be read and is legit.")
    except:
        print("Unknown Error: " + str(sys.exc_info()[0]))

if __name__ == '__main__':
    cli()
