from machine import ADC
import time
from machine import Pin
from utime import sleep

pin = Pin("LED", Pin.OUT)

sensor_temp = ADC(4)
conversion_factor = 3.3 / (65535)

def get_temp():
    reading = sensor_temp.read_u16() * conversion_factor
    return 27 - (reading - 0.706)/0.001721

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

pin.off()

limit = 100000  # adjust this limit as you like
count = 0

print(f"Temperature before: {get_temp()}")

pin.toggle()

for num in range(2, limit + 1):
    if is_prime(num):
        print(num)
        count+=1
        
print(f"Prime number count: {count}")
print(f"Temperature after: {get_temp()}")
pin.off()

i = 0
while True:
    try:
        i += 1
        pin.toggle()
        sleep(000.1) # sleep 1sec
        print(f"Iteration Oskar, {i}")
    except KeyboardInterrupt: 
        break


