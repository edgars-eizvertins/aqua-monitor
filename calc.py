from utime import sleep

print(f"Iteration Oskar, {30+80}")

i = 2
while True:
    try:
        i = i * 2
        #pin.toggle()
        sleep(0.001) # sleep 1sec
        
        print(f"Next number, {i}")
    except KeyboardInterrupt: 
        break