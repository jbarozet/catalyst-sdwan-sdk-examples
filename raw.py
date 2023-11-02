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

# RAW APIs
response = session.get("/dataservice/device")
payload = response.json()
# print(payload)

payloadJSON = json.dumps(payload, indent=4)
print(payloadJSON)
