import machine
import dht
import time

sensor = dht.DHT11(machine.Pin(33))
sensor.measure()


while(True):
  print(sensor.humidity())
  print(sensor.temperature())
  time.sleep(1)
