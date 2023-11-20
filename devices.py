import os

import urllib3
from vmngclient.dataclasses import Personality
from vmngclient.session import create_vManageSession

# Disable warnings because of no certificate on vManage
# urllib3.disable_warnings()
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


# ----------------------------------------------------------------------------------------------------
# Create session
# ----------------------------------------------------------------------------------------------------
#
url = os.environ.get("vmanage_host")
# vmanage_port = os.environ.get("vmanage_port")
username = os.environ.get("vmanage_username")
password = os.environ.get("vmanage_password")

if url is None or username is None or password is None:
    print(
        "For Windows Workstation, vManage details must be set via environment variables using below commands"
    )
    print("set vmanage_host=10.10.1.1")
    print("set vmanage_port=8443")
    print("set vmanage_username=admin")
    print("set vmanage_password=admin")
    print(
        "For MAC OSX Workstation, vManage details must be set via environment variables using below commands"
    )
    print("export vmanage_host=10.10.1.1")
    print("export vmanage_port=8443")
    print("export vmanage_username=admin")
    print("export vmanage_password=admin")
    exit()

session = create_vManageSession(url=url, username=username, password=password)
print(session.about())

# ----------------------------------------------------------------------------------------------------
# Get the list of devices
# ----------------------------------------------------------------------------------------------------

devices = session.api.devices.get()

# Filter vmanage devices
vmanage = devices.filter(personality=Personality.VMANAGE).single_or_default()

print("---------------------------------------------------------------------")
print(
    f"Hostname: {vmanage.hostname} - Load: {vmanage.cpu_load} - Board serial: {vmanage.board_serial}"
)
print("---------------------------------------------------------------------")

# ----------------------------------------------------------------------------------------------------
# Display the list of devices
# ----------------------------------------------------------------------------------------------------

for dev in devices:
    print(f"{dev.hostname} - Load: {dev.cpu_load} - Board serial: {dev.board_serial}")
    print(session.api.device_state.get_system_status(dev.id))

# ---END--
