import click
import urllib3
import re
# check this with Click documentation
from colorama import Fore
import sys


def basic_file_read(file, *args):
    s = args[0]
    try:
        file_data = open(file, 'r', encoding="utf-8")
        pattern = re.findall(r'https?:[a-zA-Z0-9_.+-/#~]+', file_data.read())
        for l in pattern:
            q = l.strip()
            test_request(q)
            if (s):
                isHttp = re.match('(http)', q)
                if (isHttp):
                    q = re.sub('(http)', 'https', q)
                    test_request(q)
    except OSError:
        print("The file cannot be opened! Make sure this file can be read and is legit.")


def test_request(q):
    # try adding more support for other html codes
    try:
        h = urllib3.PoolManager()
        req = h.request('HEAD', q)
        if (req.status == 200):
            # this is not working with my machine. Perhaps check Click documentation and see what is going on with this
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
@click.option('--s', is_flag=True, default=False, help='Optional flag to check if https can be used instead of http')
def file_reader(file, s):
    """this reads URL links from a file!"""
    basic_file_read(file, s)


@cli.command('url')
@click.argument('url')
@click.option('--l', '-l', is_flag=True, help='look through the given website recursively and check the webpage for dead links')
def url_reader(url, l):
    """this reads a URL that you pass as an argument!"""
    test_request(str(url))


@cli.command('version')
def version_check():
    """Returns you the version number of this code"""
    print(Fore.BLUE + "Version 0.1")


if __name__ == '__main__':
    cli()
