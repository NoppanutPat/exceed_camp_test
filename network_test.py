import network

station = network.WLAN(network.STA_IF)

station.active(True)

station.connect("SIR_PHOTOGRAPHER","NoppanutT.")

station.isconnected()

station.ifconfig()

station.disconnect()
