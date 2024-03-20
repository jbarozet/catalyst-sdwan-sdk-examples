# Backup Task
#
# config_groups
#   associated
#   groups
#   values
#
# feature_profiles
#   sdwan
#       cli
#       system
#       transport
#       service
#       policy_object

import json
import os
from os.path import join
from pathlib import Path

import urllib3
from catalystwan.api.config_group_api import ConfigGroupAPI, ConfigGroupResponsePayload

from session import create_session

profile_id_table = []
profile_id_dict = {}


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
    Get the list of feature profiles used but not parcels
    Need to use the API for profiles to get the list of associated parcels
    """

    workdir = "data/config_groups"
    base = "dataservice/v1/config-group/"
    data = session.get(base).json()

    for key in data:
        config_group_id = key["id"]
        config_group_name = key["name"]
        tmp = config_group_name + ".json"
        filename = join(workdir, tmp)
        print(f"> Config Group ID ❯ {config_group_name}")
        url = base + config_group_id
        config_group = session.get(url).json()
        for item in config_group["profiles"]:
            profile_id = item["id"]
            profile_type = item["type"]
            new_element = [profile_id, profile_type]
            profile_id_table.append(new_element)
            print(new_element)
        with open(filename, "w") as file:
            json.dump(config_group, file, indent=4)
    print(f"summary: {profile_id_table}")


def save_feature_profiles():
    """
    Feature Profiles - Get specific profile details
    Including associated parcels
    """

    base = "dataservice/v1/feature-profile/sdwan/service/"
    workdir_cli = "data/feature_profiles/cli"
    workdir_system = "data/feature_profiles/system"
    workdir_transport = "data/feature_profiles/transport"
    workdir_service = "data/feature_profiles/service"
    # feature_profile_id = input("Enter feature-profile ID ❯ ")

    for i in range(len(profile_id_table)):
        profile_id = profile_id_table[i][0]
        profile_type = profile_id_table[i][1]

        match profile_type:
            case "system":
                workdir = workdir_system
            case "transport":
                workdir = workdir_transport
            case "service":
                workdir = workdir_service
            case "cli":
                workdir = workdir_cli
            case _:
                workdir = "data/feature_profiles"

        url = base + profile_id
        data = session.get(url).json()
        profile_name = data["profileName"]
        tmp = profile_name + ".json"
        print(
            f"--- Profile Name ❯ {profile_name} - {profile_id} - {profile_type} - {workdir}"
        )
        filename = join(workdir, tmp)
        with open(filename, "w") as file:
            json.dump(data, file, indent=4)

    # for profile_id in profile_id_table[:]:
    #     url = base + profile_id
    #     data = session.get(url).json()
    #     profile_name = data["profileName"]
    #     print(f"--- Profile Name ❯ {profile_name}")
    #     tmp = profile_name + ".json"
    #     filename = join(workdir, tmp)
    #     with open(filename, "w") as file:
    #         json.dump(data, file, indent=4)


def save_associated_devices():
    """
    Get Devices associated with a specific config-group.
    'v1/config-group/{configGroupId}/device/associate'
    """


def config_group_values():
    """
    'v1/config-group/{configGroupId}/device/variables'
    store_path = ('config_groups', 'values')
    store_file = '{item_name}.json'
    """


def save_automated_rules():
    # base = "dataservice/tag/tagRules/"
    # base = "v1/config-group/{configGroupId}/rules"
    base = "dataservice/v1/config-group/"
    config_group_id = input("Enter config-group id: ")
    url = base + config_group_id + "/rules"
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
# save_automated_rules()
