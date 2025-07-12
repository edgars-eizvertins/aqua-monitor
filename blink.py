from machine import Pin
from utime import sleep

pin = Pin("LED", Pin.OUT)

print("LED starts flashing...")
i = 0
while True:
    try:
        i += 1
        pin.toggle()
        sleep(000.1) # sleep 1sec
        print(f"Iteration Oskar, {i}")
    except KeyboardInterrupt: 
        break
pin.off()
print("Finished.")
