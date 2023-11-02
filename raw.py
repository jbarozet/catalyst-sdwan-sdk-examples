import json
from vmngclient.dataclasses import Personality
from vmngclient.session import create_vManageSession
import urllib3
import os

# Disable warnings because of no certificate on vManage
# urllib3.disable_warnings()
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# CREATE SESSION

url = os.environ.get("vmanage_host")
# vmanage_port = os.environ.get("vmanage_port")
username = os.environ.get("vmanage_username")
password = os.environ.get("vmanage_password")

session = create_vManageSession(url=url, username=username, password=password)
print(session.about())

# RAW APIs
response = session.get("/dataservice/device")
payload = response.json()
# print(payload)

payloadJSON = json.dumps(payload, indent=4)
print(payloadJSON)
