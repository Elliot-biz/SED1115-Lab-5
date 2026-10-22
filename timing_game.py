from machine import Pin, I2C
import time

# Set up the button
button = Pin(22, Pin.IN, Pin.PULL_DOWN)

# Set up I2C channel 1
i2c = I2C(1, sda=Pin(14), scl=Pin(15))

# DS3231 RTC address
rtc_address = 0x68