from machine import Pin, SoftI2C
from time import sleep

import ahtx0, bmp280

i2c=SoftI2C(sda=Pin(21), scl=Pin(22), freq=100000)

"""
0x38 - aht20
0x77 - bmp280
"""

senzor_aht=ahtx0.AHT20(i2c, 0x38)

senzor_bmp280=bmp280.BMP280(i2c, 0x77)

while True:
    
    print("AHT20 ====> ", "T = ", round(senzor_aht.temperature,2)," H= ", round(senzor_aht.relative_humidity,2)," ********    BMP280 ====> ", "T = " , round(senzor_bmp280.temperature,2)," P = ", round(senzor_bmp280.pressure,2)," ", end="\r")
    sleep(1)
