import click
import urllib3
import re
from colorama import Fore
import sys
import json

"""This is the main fnuction that reads from a file"""
def basic_file_read(file, json_file, ignore):
    try:
        file_data = open(file, "r", encoding="utf-8")
        pattern = re.findall(r"https?:[a-zA-Z0-9_.+-/#~]+", file_data.read())
        list_of_status = []
        for l_e in pattern:
            q_e = l_e.strip()
            if ignore != q_e:
                list_of_status.append(test_request(q_e, json))
        return list_of_status
    except OSError:
        print(
            "The file cannot be opened! Make sure this file can be read and is legit."
        )
        sys.exit(1)


def test_request(q_e, json_file):
    try:

        h_p = urllib3.PoolManager()
        req = h_p.request("HEAD", q_e)
        if not json_file:
            if req.status == 200:
                print(Fore.GREEN + f"{q_e}  passes with {req.status}!")
            elif req.status == 403:
                print(Fore.WHITE + f"{q_e} looks sus, it returned {req.status}")

            else:
                print(Fore.RED + f"{q_e} is dead, as it returned {req.status}")
            return (0, req.status)
        else:
            conv = {"url": q_e, "status": req.status}
            print(conv)
            return(0, req.status)
    except:
        print("Unknown Error: " + str(sys.exc_info()[0]))
        return (-1,1000)


def telescope_urls(q_e, json_file=None):
    h_p = urllib3.PoolManager()
    req = h_p.request("HEAD", q_e)
    try:
        if not json_file:
            if req.status == 200:
                print(Fore.GREEN + f"{q_e}  passes with {req.status}!")
            elif req.status == 403:
                print(Fore.WHITE + f"{q_e} looks sus, it returned {req.status}")

            else:
                print(Fore.RED + f"{q_e} is dead, as it returned {req.status}")
            return 0
        else:
            conv = {"url": q_e, "status": req.status}
            print(conv)
    except:
        print("Unknown Error: " + str(sys.exc_info()[0]))
        return -1


@click.group()
def cli():
    pass


@cli.command("file")
@click.argument("file")
@click.option("--json", is_flag=True)
@click.option("--ignore", default=None, type=str)
def file_reader(file, json, ignore):
    """this reads URL links from a file!"""
    q_e = False
    if json:
        q_e = True
    a_e = basic_file_read(file, q_e, ignore)
    for x_e in list:
        if a_e[x_e][0] != 0:
            sys.exit(a_e[x_e][0])
    return a_e[0][1]


@cli.command("url")
@click.argument("url")
@click.option("--json", is_flag=True)
def url_reader(url, json_file):
    """this reads a URL that you pass as an argument!"""
    q_e = False
    if json_file:
        q_e = True
    a_e = test_request(str(url), q_e)
    if a_e[0] != 0:
        sys.exit(a_e[0])
    else:
        sys.exit(a_e[1])


@cli.command("telescope")
def telescope_reader():
    h_e = urllib3.PoolManager()
    telescope_str = "http://localhost:3000/posts"
    req = h_e.request("GET", telescope_str)
    try:
        posts = json.loads(req.data)
        for post in posts:
            telescope_urls(f"{telescope_str}/{post['id']}")
    except urllib3.exceptions.MaxRetryError as e:  # At this point, the connection attempt timed out and therfore, the url cannot be reached, so in this case, we skip the url entirely.
        print(str(e))


@cli.command("version")
def version_check():
    """Returns you the version number of this code"""
    print(Fore.BLUE + "Version 0.1")


if __name__ == "__main__":
    cli()
