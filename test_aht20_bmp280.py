
from machine import Pin, SoftI2C
from time import sleep

import ahtx0
import bmp280

i2c=SoftI2C(sda=Pin(21), scl=Pin(22), freq=100000)

senzor_aht=ahtx0.AHT20(i2c, 0x38)
senzor_bmp280=bmp280.BMP280(i2c, 0x77)

while True:
    print("AHT temp = ",round(senzor_aht.temperature,2)," ", "AHT humy = ",round(senzor_aht.relative_humidity,2)," **** ","BMP280 temp = ",round(senzor_bmp280.temperature,2)," ", " press = ",round(senzor_bmp280.pressure/100,2)," ", end="\r")
    
    sleep(1)
    