#Archivo boot.py
import network
import usocket

ap=network.WLAN(network.AP_IF)
ap.active(True)
password='123456789'
essid="ESP32-MicroPython"
ap.config(essid=essid,password=password)
print("AP iniciada")
print(ap.ifconfig())

