from vmngclient.dataclasses import Personality
from vmngclient.session import create_vManageSession
import urllib3
import click
import tabulate
import os

# Disable warnings because of no certificate on vManage
# urllib3.disable_warnings()
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# ----------------------------------------------------------------------------------------------------
# Click CLI
# ----------------------------------------------------------------------------------------------------

@click.group()
def cli():
    """Command line tool to showcase Catalyst SD-WAN Python SDK
    """
    pass

# ----------------------------------------------------------------------------------------------------
# app-list
# ----------------------------------------------------------------------------------------------------

@click.command()
def app_list():
    # Raw APIs
    response = session.get("/dataservice/device/dpi/application-mapping")
    payload = response.json()

    ## Format output
    table = list()
    app_headers = ["App name", "Family", "ID"]

    for item in payload['data']:
        tr = [item['name'], item['family'], item['appId']]
        table.append(tr)

    click.echo(tabulate.tabulate(table, app_headers, tablefmt="fancy_grid"))


# ----------------------------------------------------------------------------------------------------
# Create session
# ----------------------------------------------------------------------------------------------------

url = os.environ.get("vmanage_host")
# vmanage_port = os.environ.get("vmanage_port")
username = os.environ.get("vmanage_username")
password = os.environ.get("vmanage_password")

if url is None or username is None or password is None:
    print("For Windows Workstation, vManage details must be set via environment variables using below commands")
    print("set vmanage_host=10.10.1.1")
    print("set vmanage_port=8443")
    print("set vmanage_username=admin")
    print("set vmanage_password=admin")
    print("For MAC OSX Workstation, vManage details must be set via environment variables using below commands")
    print("export vmanage_host=10.10.1.1")
    print("export vmanage_port=8443")
    print("export vmanage_username=admin")
    print("export vmanage_password=admin")
    exit()

session = create_vManageSession(url=url, username=username, password=password)
# print(session.about())

# ----------------------------------------------------------------------------------------------------
# Run commands
# ----------------------------------------------------------------------------------------------------

cli.add_command(app_list)

if __name__ == "__main__":
    cli()
