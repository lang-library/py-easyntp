# py-easyntp

```
from easyntp import *

ntp_client = EasyNTPClient()
print(ntp_client.now())
print(ntp_client.format_now('%Y/%m/%d'))

"""
2024-05-16 18:03:10
2024/05/16
"""
```