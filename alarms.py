import vmngclient
from vmngclient.session import create_vManageSession
import urllib3

# Disable warnings because of no certificate on vManage
# urllib3.disable_warnings()
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# CREATE SESSION

url = "sandbox-sdwan-2.cisco.com"
username = "devnetuser"
password = "RG!_Yw919_83"

session = create_vManageSession(url=url, username=username, password=password)
print(session.about())

# GET ALARMS

alarms = session.api.alarms.get()
print(alarms)

template_api = 