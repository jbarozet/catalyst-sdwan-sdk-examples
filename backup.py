from pathlib import Path
from vmngclient.session import create_vManageSession
from vmngclient.model.tenant import TenantExport
from vmngclient.workflows.tenant_migration import migration_workflow

import urllib3

# Disable warnings because of no certificate on vManage
# urllib3.disable_warnings()
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


# ----------------------------------------------------------------------------------------------------
# Create Session
# ----------------------------------------------------------------------------------------------------
#
url = "10.62.190.144"
username = "jbarozet"
password = "tmetest123"

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
print(f"Version: {session.about().version}")
print(f"Application Version: {session.about().application_version}")

# ----------------------------------------------------------------------------------------------------
# Get the list of config_groups
# ----------------------------------------------------------------------------------------------------

origin_api = session.api.tenant_migration
tenant_file = Path("./tenant.tar.gz")
token_file = Path("./tenant-token.txt")

# export
export_task = origin_api.export_tenant(tenant=tenant)
remote_filename = export_task.wait_for_file()

# download
origin_api.download(export_path, remote_filename)
