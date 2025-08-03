import network
import time

ssid = 'PAL 5.0'
password = 'ManDunn123'

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(ssid, password)

# Wait for connection
while not wlan.isconnected():
    print('Connecting...')
    time.sleep(1)

print('Connected!')

ip_info = wlan.ifconfig()
print('IP address:', ip_info[0])