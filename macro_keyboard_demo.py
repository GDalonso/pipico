import time
import digitalio
import board
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

#Configure which GPIO pin the buttons are at
btn1_pin = board.GP15

# Create the keyboard HID
keyboard = Keyboard(usb_hid.devices)

# Set the BTN1 GPIO and as default down, or False
btn1 = digitalio.DigitalInOut(btn1_pin)
btn1.direction = digitalio.Direction.INPUT
btn1.pull = digitalio.Pull.DOWN

#Initialize onboard LED to blink when btn pressed
led_onboard = digitalio.DigitalInOut(board.GP25)
led_onboard.direction = digitalio.Direction.OUTPUT
led_onboard.value = False

while True:
    if btn1.value: #Since the btn starts as DOWN, if it has value it was pressed
        led_onboard.value=True #Turn the LED on
        keyboard.press(Keycode.D, Keycode.T, Keycode.MINUS)
        keyboard.release(Keycode.D, Keycode.T, Keycode.MINUS)
        
        keyboard.press(Keycode.X, Keycode.ENTER)
        keyboard.release(Keycode.X, Keycode.ENTER)
            
        #This small delay prevents the button from being read hundreds of times at once
        time.sleep(0.2)
        led_onboard.value=False #Turn the LED off
    time.sleep(0.1)

