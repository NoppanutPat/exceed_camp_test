import urequests
import network
import json

station = network.WLAN(network.STA_IF)

station.active(True)

station.connect("SIR_PHOTOGRAPHER","NoppanutT.")

print("connecting Wifi....")

if station.isconnected():
  
  print("connected")

  r = urequests.get("http://duckduckgo.com/?q=micropython&format=json").json()

  print(r)
