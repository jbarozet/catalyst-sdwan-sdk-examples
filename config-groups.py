from session import create_session
from vmngclient.api.config_group_api import ConfigGroupAPI
import urllib3

# Disable warnings because of no certificate on vManage
# urllib3.disable_warnings()
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Create vManage session
session = create_session()

# Get the list of config_groups
config_groups = session.api.config_group.get()

# config_groups_api = ConfigGroupAPI(session)
# config_groups = config_groups_api.get()

# Display the list of config_groups
for group in config_groups:
    print(
        f"Name: {group.name} - Description: {group.description} - Solution: {group.solution.value}"
    )
    for profile in group.profiles:
        print(
            f"- Id: {profile.id} - Name: {profile.name} - Type: {profile.type.value} - Last Update: {profile.last_updated_by} - Date: {profile.last_updated_on}"
        )


# ---END--
