from easyntp import *
ntp_client = EasyNTPClient()
print(ntp_client.now())
print(ntp_client.format_now('%Y/%m/%d'))
