import machine
import sdcard
import uos
"""
Reference video with pinout 
https://www.youtube.com/watch?v=JrYT7aJnP_I
https://github.com/garyexplains/examples/tree/master/Raspberry%20Pi%20Pico/sdcard_spi
backup link:
https://drive.google.com/file/d/1SFXGq-gllY5bWEF9OoG6Rt9Z9Xxbtv5W/view?usp=sharing
"""
# Assign chip select (CS) pin (and start it high)
cs = machine.Pin(1, machine.Pin.OUT)

# Intialize SPI peripheral (start with 1 MHz)
spi = machine.SPI(0,
                  baudrate=1000000,
                  polarity=0,
                  phase=0,
                  bits=8,
                  firstbit=machine.SPI.MSB,
                  sck=machine.Pin(2),
                  mosi=machine.Pin(3),
                  miso=machine.Pin(4))

# Initialize SD card
sd = sdcard.SDCard(spi, cs)

# Mount filesystem
vfs = uos.VfsFat(sd)
uos.mount(vfs, "/sd")

def write_to_file(name:str, content:str):
    name = f"/sd/{name}"
    with open(name, "a") as file:
        file.write(content)
        file.close()

