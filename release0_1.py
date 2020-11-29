import click
import urllib3
import re
from colorama import Fore
import sys
import json


def basic_file_read(file,json,ignore):
    try:
        file_data = open(file,'r',encoding="utf-8")
        pattern = re.findall(r'https?:[a-zA-Z0-9_.+-/#~]+', file_data.read())
        for l in pattern:
            q = l.strip()
            if(ignore != q):
                test_request(q,json)
    except OSError:
        print("The file cannot be opened! Make sure this file can be read and is legit.")
        sys.exit(1)

def test_request(q,json):
    try:

        h = urllib3.PoolManager()
        req = h.request('HEAD', q)
        if not json:
            if(req.status == 200):
                print(Fore.GREEN + f"{q}  passes with {req.status}!")
            elif (req.status == 403):
                print(Fore.WHITE + f"{q} looks sus, it returned {req.status}")

            else:
                print(Fore.RED + f"{q} is dead, as it returned {req.status}")
            return 0
        else:
            conv = {'url': q, 'status' : req.status}
            print(conv)
    except:
        print("Unknown Error: " + str(sys.exc_info()[0]))
        return -1



def telescope_urls(q, json=None):
    h = urllib3.PoolManager()
    req = h.request('HEAD', q)
    try:
        if not json:
            if(req.status == 200):
                print(Fore.GREEN + f"{q}  passes with {req.status}!")
            elif (req.status == 403):
                print(Fore.WHITE + f"{q} looks sus, it returned {req.status}")

            else:
                print(Fore.RED + f"{q} is dead, as it returned {req.status}")
            return 0
        else:
            conv = {'url': q, 'status' : req.status}
            print(conv)
    except:
        print("Unknown Error: " + str(sys.exc_info()[0]))
        return -1

@click.group()
def cli():
    pass

@cli.command('file')
@click.argument('file')
@click.option('--json', is_flag=True)
@click.option('--ignore', default=None, type=str)
def file_reader(file,json,ignore):
    """this reads URL links from a file!"""
    q = False
    if json:
        q = True
    a = basic_file_read(file,q,ignore)
    if (a != 0):
        sys.exit(a)

@cli.command('url')
@click.argument('url')
@click.option('--json', is_flag=True)



def url_reader(url,json):
    """this reads a URL that you pass as an argument!"""
    q = False
    if json:
        q = True
    a = test_request(str(url),q)
    if(a != 0):
        sys.exit(a)



@cli.command('telescope')
def telescope_reader():
    h = urllib3.PoolManager()
    telescope_str = 'http://localhost:3000/posts'
    req = h.request('GET', telescope_str)
    try:
        posts = json.loads(req.data)
        for post in posts:
            telescope_urls(f"{telescope_str}/{post['id']}")
    except urllib3.exceptions.MaxRetryError as e: # At this point, the connection attempt timed out and therfore, the url cannot be reached, so in this case, we skip the url entirely.
        print(str(e))




@cli.command('version')
def version_check():
    """Returns you the version number of this code"""
    print(Fore.BLUE + "Version 0.1")




if __name__ == '__main__':
    cli()
