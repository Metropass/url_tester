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
    print(url)
    try:
        print('create PoolManager')
        link = urllib3.PoolManager()
        print('begin request')
        res = link.request('HEAD', url)
        print('finished req')
        if(res.status == 200):
            print(Fore.GREEN + f"{url}  passes with {req.status}!")
        elif (res.status == 403):
            print(Fore.BLACK + f"{url} looks sus, it returned {req.status}")
        else:
            print(Fore.RED + f"{url} is dead, as it returned {req.status}")
    except OSError:
        print("The file cannot be opened! Make sure this file can be read and is legit.")
    except:
        print("Unknown Error: " + str(sys.exc_info()[0]))

if __name__ == '__main__':
    cli()
