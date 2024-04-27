import network
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect('wifi_name', 'wifi_password')
print(wlan.isconnected())