from machine import Pin, I2C
import time

# Set up the button
button = Pin(22, Pin.IN, Pin.PULL_DOWN)

# Set up I2C channel 1
i2c = I2C(1, sda=Pin(14), scl=Pin(15))

# DS3231 RTC address
rtc_address = 0x68

# Convert the RTC's BCD value into a normal integer
def bcd_to_int(value):
    return ((value >> 4) * 10) + (value & 0x0F)


# Read the current time from the DS3231
def get_time():
    data = i2c.readfrom_mem(rtc_address, 0x00, 3)

    seconds = bcd_to_int(data[0])
    minutes = bcd_to_int(data[1])
    hours = bcd_to_int(data[2] & 0x3F)

    return hours * 3600 + minutes * 60 + seconds

# Open the log file in append mode
log = open("log.txt", "a")

try:
    while True:
        print("Press the button to start")

        # Wait for the first button press
        while button.value() == 0:
            pass

        time.sleep_ms(50)

        start_time = get_time()

        # Wait for the button to be released
        while button.value() == 1:
            pass

        time.sleep_ms(50)

        print("Count 15 seconds, then press the button again")

        # Wait for the second button press
        while button.value() == 0:
            pass

        time.sleep_ms(50)

        end_time = get_time()

        elapsed = end_time - start_time

        # Handle the case where the timer crosses midnight
        if elapsed < 0:
            elapsed += 24 * 60 * 60

        print("Your time was:", elapsed, "seconds")

        # Save the result to the log file
        log.write(str(elapsed) + "\n")
        log.flush()

        # Wait for the button to be released before starting again
        while button.value() == 1:
            pass

        time.sleep_ms(50)
finally:
    log.close()
