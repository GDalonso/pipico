from print_temp_reads_memory import temperature_logger
import machine
import sdcard
import uos
"""
This is used to run the programs, runs the temperature_logger to sd card
working flawlesly as of now

The problem with that script is that the pi pico has no internal clock, so without an internet connection
it simply writes all logs as 

"2021-1-1 0:0 temp: 22.8311"

Making it mostly useless wihtout a clock

"""
temperature_logger()
