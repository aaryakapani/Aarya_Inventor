from machine import Pin
import time

# Initialize LED
led = Pin("LED", Pin.OUT)

print("Starting LED test...")
print("LED should be ON")

# Turn on LED
led.value(1)

# Keep the program running
while True:
    time.sleep(1) 