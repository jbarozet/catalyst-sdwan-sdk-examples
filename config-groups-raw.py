import json
import click
from session import create_session


@click.group()
def cli():
    """Command line tool to showcase Catalyst SD-WAN Python SDK"""
    pass


@click.command()
def list_config_groups():
    """List all config-groups"""

    base = "dataservice/v1/config-group/"
    response = session.get(base)
    payload = response.json()
    payloadJSON = json.dumps(payload, indent=4)
    print(payloadJSON)


@click.command()
def list_config_group_details():
    """List specific config-group details"""

    base = "dataservice/v1/config-group/"
    # id = input("Enter config-group ID ❯ ")
    # id = "0ddae5ae-a865-4769-ae84-d749ad9f4f31"
    response = session.get(base)
    data = response.json()
    for key in data:
        print("Config Group ID: ", key["id"])
        url = base + key["id"]
        response = session.get(url)
        payload = response.json()
        payloadJSON = json.dumps(payload, indent=4)
        print(payloadJSON)


@click.command()
def list_feature_profiles():
    """Feature Profiles - Get all profiles"""

    response = session.get("dataservice/v1/feature-profile/sdwan/")
    payload = response.json()
    payloadJSON = json.dumps(payload, indent=4)
    print(payloadJSON)


@click.command()
def list_feature_profiles_system():
    """Feature Profiles - Get all system profiles"""

    response = session.get("dataservice/v1/feature-profile/sdwan/system")
    payload = response.json()
    payloadJSON = json.dumps(payload, indent=4)
    print(payloadJSON)


@click.command()
def list_feature_profile_details():
    """Feature Profiles - Get specific profile details (including associated parcels)"""

    base = "dataservice/v1/feature-profile/sdwan/system/"
    id = "a93d3266-1f6b-449e-bb9b-11cdb175c19c"
    url = base + id
    response = session.get(url)
    payload = response.json()
    payloadJSON = json.dumps(payload, indent=4)
    print(payloadJSON)


cli.add_command(list_config_groups)
cli.add_command(list_config_group_details)
cli.add_command(list_feature_profiles)
cli.add_command(list_feature_profiles_system)
cli.add_command(list_feature_profile_details)

session = create_session()

if __name__ == "__main__":
    cli()
