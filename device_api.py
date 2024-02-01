from vmngclient.dataclasses import Personality

from session import create_session

# Create session
session = create_session()

# Get the list of devices
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
    print(dev.id)
    print(f"{dev.hostname} - Load: {dev.cpu_load} - Board serial: {dev.board_serial}")
    # print(session.api.device_state.get_system_status(dev.id))

# ---END--
