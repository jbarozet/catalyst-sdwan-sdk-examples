import json
from vmngclient.dataclasses import Personality
from vmngclient.session import create_vManageSession
import urllib3

# Disable warnings because of no certificate on vManage
# urllib3.disable_warnings()
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# CREATE SESSION

# url = "https://35.180.218.171"
# username = "admin"
# password = "C1sco12345"

url = "sandbox-sdwan-2.cisco.com"
username = "devnetuser"
password = "RG!_Yw919_83"

session = create_vManageSession(url=url, username=username, password=password)
print(session.about())

# GET THE LIST OD DEVICES

devices = session.api.devices.get()

# Filter vmanage devices
vmanage = devices.filter(personality=Personality.VMANAGE).single_or_default()

print("---------------------------------------------------------------------")
print(f"Hostname: {vmanage.hostname} - Load: {vmanage.cpu_load} - Board serial: {vmanage.board_serial}")
print("---------------------------------------------------------------------")

# List all devices in the overlay

for dev in devices:
    print(f"{dev.hostname} - Load: {dev.cpu_load} - Board serial: {dev.board_serial}")
    print(session.api.device_state.get_system_status(dev.id))
