"""
Catalyst SD-WAN Manager SDK - Config Groups and Feature Profiles
"""

from session import create_session
from catalystwan.api.config_group_api import ConfigGroupAPI
from catalystwan.api.config_group_api import ConfigGroupResponsePayload
import urllib3

# Disable warnings because of no certificate on vManage
# urllib3.disable_warnings()
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Create vManage session
session = create_session()

# Get the list of config_groups
config_groups = session.api.config_group.get()

print(ConfigGroupAPI.get())

# Display the list of config_groups
for group in config_groups:
    print(
        f"Name: {group.name} - Description: {group.description} - Solution: {group.solution.value}")
    for profile in group.profiles:
        print(f"- Profile Id: {profile.id}")
        print(f"  - Name: {profile.name}")
        print(f"  - Type: {profile.type.value}")
        print(f"  - Solution: {profile.solution}")
        print(f"  - Last Update: {profile.last_updated_by}")
        print(f"  - Date: {profile.last_updated_on}")

# ---END--
