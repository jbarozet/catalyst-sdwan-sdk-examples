import json
import os
from os.path import join
from pathlib import Path

import urllib3
from catalystwan.api.config_group_api import ConfigGroupAPI, ConfigGroupResponsePayload

from session import create_session


def create_backup_dir():
    workdir = "data/groups"
    # os.mkdir(workdir)
    # Check if workdir folder already exists. If yes, then stop backup process
    workdir = join(os.path.abspath(os.getcwd()), workdir)
    if os.path.isdir(workdir):
        exit(
            f"{workdir} folder is already in use. Please select a different workdir directory."
        )


def save_config_groups():
    """
    List specific config-group details
    But do not list parcels
    """

    workdir = "data/groups"
    base = "dataservice/v1/config-group/"
    data = session.get(base).json()

    for key in data:
        config_group_id = key["id"]
        config_group_name = key["name"]
        tmp = config_group_name + ".json"
        filename = join(workdir, tmp)
        print(f"> Config Group ID: {config_group_name}")
        url = base + config_group_id
        config_group = session.get(url).json()
        for item in config_group["profiles"]:
            print(item["id"])
        with open(filename, "w") as file:
            json.dump(config_group, file, indent=4)


def save_feature_profiles():
    """
    Feature Profiles - Get specific profile details
    Including associated parcels
    """

    base = "dataservice/v1/feature-profile/sdwan/service/"
    feature_profile_id = input("Enter feature-profile ID ❯ ")
    url = base + feature_profile_id
    data = session.get(url).json()
    data_formatted = json.dumps(data, indent=4)
    print(data_formatted)


# Disable warnings because of no certificate on vManage
# urllib3.disable_warnings()
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Create vManage session
session = create_session()

save_config_groups()
save_feature_profiles()
