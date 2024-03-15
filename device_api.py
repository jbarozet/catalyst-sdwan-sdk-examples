from catalystwan.dataclasses import Personality
from session import create_session

# Create session
session = create_session()


# ----------------------------------------------------------------------------------------------------
# Endpoints - Devices
# ----------------------------------------------------------------------------------------------------

device_inventory = session.endpoints.configuration_device_inventory
control_components = device_inventory.get_device_details('controllers')
manager_system_ip = control_components.filter(device_type='vmanage')[0].system_ip
validator_system_ip = control_components.filter(device_type='vbond')[0].system_ip
controller_system_ip = control_components.filter(device_type='vsmart')[0].system_ip

print(f"Manager System IP: {manager_system_ip}")
print(f"Validator System IP: {validator_system_ip}")
print(f"Controller System IP: {controller_system_ip}")

# ----------------------------------------------------------------------------------------------------
# Endpoints - Settings
# ----------------------------------------------------------------------------------------------------

settings = session.endpoints.configuration_settings
# Output of get_organisations is in the form of:
# Organization(
#     org: cml-sdwan-lab-tool,
#     domain_id: None,
#     control_connection_up: True,
# )

org_name = settings.get_organizations()[0].org
validator_fqdn = settings.get_devices()[0].domain_ip
print(f"Organization Name: {org_name}")
print(settings.get_devices())

# ----------------------------------------------------------------------------------------------------
# Endpoints - Config Groups
# ----------------------------------------------------------------------------------------------------

configuration_group = session.endpoints.configuration_group
toto = configuration_group.get()[0].name
print(toto)


# ----------------------------------------------------------------------------------------------------
# API Get the list of users
# ----------------------------------------------------------------------------------------------------

users = session.api.users.get()

# ----------------------------------------------------------------------------------------------------
# API - Get the list of alarms
# ----------------------------------------------------------------------------------------------------

alarms = session.api.alarms.get()


# ----------------------------------------------------------------------------------------------------
# API - Display Device list
# ----------------------------------------------------------------------------------------------------

# Get the list of devices
devices = session.api.devices.get()

# Filter vmanage devices
vmanage = devices.filter(personality=Personality.VMANAGE).single_or_default()

print("---------------------------------------------------------------------")
print(
    f"Hostname: {vmanage.hostname} - System-IP: {vmanage.local_system_ip} - Load: {vmanage.cpu_load} - Board serial: {vmanage.board_serial}"
)
print("---------------------------------------------------------------------")


# ----------------------------------------------------------------------------------------------------
# Display the list of devices
# ----------------------------------------------------------------------------------------------------

for dev in devices:
    print(f"{dev.hostname} - Load: {dev.cpu_load} - Board serial: {dev.board_serial}")
    # print(session.api.device_state.get_system_status(dev.id))

# ---END--
