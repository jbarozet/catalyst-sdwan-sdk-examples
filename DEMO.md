# Demo Script

## DEMO1

use device_raw.py
show json output

## DEMO2

use device_api.py

## DEMO3

Open device_api.py
add:

```python
users = session.api.users.get()
alarms = session.api.alarms.get()
print(users)
```
