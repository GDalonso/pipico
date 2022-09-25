import machine
import utime
import time
from time_formatter import TimeFormatter
from file_writer import write_to_file
from led_util import ONBOARDLED

def temperature_logger():
    sensor_temp = machine.ADC(machine.ADC.CORE_TEMP)

    conversion_factor = 3.3 / (65535)
    led = ONBOARDLED()
    
    while True:
      reading = sensor_temp.read_u16() * conversion_factor
      temperature = 27 - (reading - 0.706)/0.001721
      tempstr = str(TimeFormatter(time.gmtime()))+ " temp: "+ str(temperature) + "\n"
      print(tempstr)
      led.ON()
      utime.sleep(1)
      led.OFF()
      write_to_file(name="temps.txt", content=tempstr)

if __name__ == "__main__":
    temperature_logger()