import machine

G_LED = machine.PWM(machine.Pin(33,machine.Pin.OUT))
B_LED = machine.PWM(machine.Pin(32,machine.Pin.OUT))

G_LED.freq(200)
B_LED.freq(600)
