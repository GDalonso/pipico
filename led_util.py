"""
Use the onboard LED to indicate progress
"""
from utime import sleep as utime_sleep
import machine
class ONBOARDLED:
    def __init__(self):
        self.led_onboard = machine.Pin(25, machine.Pin.OUT)
    
    def OFF(self):
        self.led_onboard.value(0)
    def ON(self):
        self.led_onboard.value(1)
    def BLINK(self):
        self.ON()
        utime_sleep(1)
        self.OFF()
