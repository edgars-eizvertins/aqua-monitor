import network
import socket
import time
from machine import Pin

# Setup LED
led = Pin("LED", Pin.OUT)
led.off()

# Your Wi-Fi credentials
ssid = 'Home'
password = ''

# Connect to Wi-Fi
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(ssid, password)

print("Connecting to Wi-Fi...")
while not wlan.isconnected():
    time.sleep(1)
print("Connected!")
print("IP address:", wlan.ifconfig()[0])

# Create a socket server
addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]
s = socket.socket()
s.bind(addr)
s.listen(1)

print("Web server is running...")

# Turn LED on to show ready
led.on()

while True:
    client, addr = s.accept()
    print("Client connected:", addr)
    request = client.recv(1024)
    print("Request:", request)

    response = """\
HTTP/1.1 200 OK

Hello from Oskar!
"""
    client.send(response)
    client.close()
    
     # Blink LED once
    led.off()
    time.sleep(0.1)
    led.on()

s.close()