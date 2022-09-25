"""Using the pico temperature sensor"""

# pylint: disable=import-error
import machine
import utime

# Get the temperature from the internal RP2040 temperature sensor.
sensor_temp = machine.ADC(4)

# See Raspberry Pi Pico datasheet for the conversion factor.
CONVERSION_FACTOR = 3.3 / (65535)

# Set up LEDs.
led_onboard = machine.Pin(25, machine.Pin.OUT)

def leds_off():
    """Turn off all the LEDs."""
    led_onboard.value(0)

def leds_on():
    """Turn on all the LEDs."""
    led_onboard.value(1)

# Flash all the LEDs on startup.
leds_off()
leds_on()
utime.sleep(1)
leds_off()

# Go into a loop.
while True:
    # Get a temperature reading.
    reading = sensor_temp.read_u16() * CONVERSION_FACTOR

    # Convert the temperature into degrees celsius.
    temperature = 27 - (reading - 0.706)/0.001721
    print(temperature)
    
    # Sleep for 5 seconds.
    utime.sleep(5)
