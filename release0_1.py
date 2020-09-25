import click
import urllib3
import re
from colorama import Fore
import sys


def basic_file_read(file):
    try:
        file_data = open(file,'r',encoding="utf-8")
        pattern = re.findall(r'https?:[a-zA-Z0-9_.+-/#~]+', file_data.read())
        for l in pattern:
            q = l.strip()
            test_request(q)
    except OSError:
        print("The file cannot be opened! Make sure this file can be read and is legit.")

def test_request(q):
    try:
        h = urllib3.PoolManager()
        req = h.request('HEAD', q)
        if(req.status == 200):
            print(Fore.GREEN + f"{q}  passes with {req.status}!")
        elif (req.status == 403):
            print(Fore.WHITE + f"{q} looks sus, it returned {req.status}")
        else:
            print(Fore.RED + f"{q} is dead, as it returned {req.status}")
    except:
        print("Unknown Error: " + str(sys.exc_info()[0]))

@click.group()
def cli():
    pass

@cli.command('file')
@click.argument('file')
def file_reader(file):
    """this reads URL links from a file!"""
    basic_file_read(file)

@cli.command('url')
@click.argument('url')
def url_reader(url):
    """this reads a URL that you pass as an argument!"""
    test_request(str(url))



@cli.command('version')
def version_check():
    print(Fore.BLUE + "Version 0.1")




if __name__ == '__main__':
    cli()
