from vmngclient.session import create_vManageSession
import urllib3

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

# OMP PEERS

deviceid = "10.10.1.15"
omp_peers = session.api.omp.get_omp_peers(deviceid)
print(omp_peers)
