import time
import board
import busio
import digitalio
import os
import storage
import adafruit_sdcard
from userLib.MicroSD.SD import SD
import adafruit_rfm9x
import json

# Atribution des pins et de la frequence de la radio :
RADIO_FREQ_MHZ = 433.0 # Frequence de la radio en Mhz. Doit matcher avec celle de la radio embarquée.
CS = digitalio.DigitalInOut(board.GP9) #GP13
RESET = digitalio.DigitalInOut(board.GP22)
LED = digitalio.DigitalInOut(board.GP25)
LED.direction = digitalio.Direction.OUTPUT

# Instanciation du bus SPI :
spi = busio.SPI(board.GP10, MOSI=board.GP11, MISO=board.GP8) #GP14 GP15 GP12

# Instanciation la carde microSD (Doit etre fait avant la radio!) :
microSD = SD(spi,board.GP13)

# Instanciation de la radio :
rfm9x = adafruit_rfm9x.RFM9x(spi, CS, RESET, RADIO_FREQ_MHZ)

# j ai changé le tx_power de 23 à 13
rfm9x.tx_power = 13


# Ouverture et mise à 0 (création) des fichiers de stockage sur la microSD, strucutre de vecteur destinee a Octave GUI :

# 1. PHT sensor :
with open("/sd/PHT/Pressure.txt", "w") as Pressure :
    Pressure.write("[")

with open("/sd/PHT/Humidity.txt", "w") as Humidity :
    Humidity.write("[")

with open("/sd/PHT/Temperature.txt", "w") as Temperature :
    Temperature.write("[")

#2. Air Quality sensor :

#   PM - Env :
with open("/sd/AQ/pm10e.txt", "w") as pm10e :
    pm10e.write("[")
with open("/sd/AQ/pm25e.txt", "w") as pm25e :
    pm25e.write("[")
with open("/sd/AQ/pm100e.txt", "w") as pm100e :
    pm100e.write("[")

#   PM - Standard :
with open("/sd/AQ/pm10s.txt", "w") as pm10s :
    pm10s.write("[")
with open("/sd/AQ/pm25s.txt", "w") as pm25s :
    pm25s.write("[")
with open("/sd/AQ/pm100s.txt", "w") as pm100s :
    pm100s.write("[")

#   Particles - um :
with open("/sd/AQ/prt03.txt", "w") as prt03 :
    prt03.write("[")
with open("/sd/AQ/prt05.txt", "w") as prt05 :
    prt05.write("[")
with open("/sd/AQ/prt10.txt", "w") as prt10 :
    prt10.write("[")
with open("/sd/AQ/prt25.txt", "w") as prt25 :
    prt25.write("[")
with open("/sd/AQ/prt50.txt", "w") as prt50 :
    prt50.write("[")
with open("/sd/AQ/prt100.txt", "w") as prt100 :
    prt100.write("[")

# Mise en marche de la radio sur le mode "reception" :

print("Waiting for packets...")

#while True:
for i in range(100):

    time.sleep(0.001)

    packet = rfm9x.receive()

    if packet is None :
        LED.value = False
    else:
        # Packet recu <--> Allumer la led :
        LED.value = True
        # Convertir le packet des raw bytes à un string :
        packet_text = str(packet, "ascii")
        # Modifier le string pour qu'il ait la structure d'un dictionnaire selon la syntaxe de JSON :
        valuesDict = packet_text.replace("[(","{")
        valuesDict = valuesDict.replace(")]","}")
        valuesDict = valuesDict.replace("})","}")
        valuesDict = valuesDict.replace("',","\":")
        valuesDict = valuesDict.replace("('","\"")
        valuesDict = valuesDict.replace("'","\"")
        # Convertir le string en un dictionnaire avec le module JSON :
        valuesDict = json.loads(valuesDict)
        print("\nData received from CanSat :\n{}".format(valuesDict))
        # Intensité du signal (optionnel) :
        rssi = rfm9x.last_rssi
        print("Signal strength: {0} dB".format(abs(rssi)))
        # Stockage des mesures sur la carte microSD :
        #
        # 1. PHT Sensor :
        #
        with open("/sd/PHT/Pressure.txt", "a") as Pressure :
            Pressure.write(str(valuesDict["PHT"]["P"]) + " , ")
        with open("/sd/PHT/Humidity.txt", "a") as Humidity :
            Humidity.write(str(valuesDict["PHT"]["H"]) + " , ")
        with open("/sd/PHT/Temperature.txt", "a") as Temperature :
            Temperature.write(str(valuesDict["PHT"]["T"]) + " , ")
        #
        #2. Air Quality sensor :
        #
        #   PM - Env :
        with open("/sd/AQ/pm10e.txt", "a") as pm10e :
            pm10e.write(str(valuesDict["AQ"]["pm10e"]) + " , ")
        with open("/sd/AQ/pm25e.txt", "a") as pm25e :
            pm25e.write(str(valuesDict["AQ"]["pm25e"]) + " , ")
        with open("/sd/AQ/pm100e.txt", "a") as pm100e :
            pm100e.write(str(valuesDict["AQ"]["pm100e"]) + " , ")
        #
        #   PM - Standard :
        with open("/sd/AQ/pm10s.txt", "a") as pm10s :
            pm10s.write(str(valuesDict["AQ"]["pm10s"]) + " , ")
        with open("/sd/AQ/pm25s.txt", "a") as pm25s :
            pm25s.write(str(valuesDict["AQ"]["pm25s"]) + " , ")
        with open("/sd/AQ/pm100s.txt", "a") as pm100s :
            pm100s.write(str(valuesDict["AQ"]["pm100s"]) + " , ")
        #
        #   #   Particles - um :
        with open("/sd/AQ/prt03.txt", "a") as prt03 :
            prt03.write(str(valuesDict["AQ"]["prt03"]) + " , ")
        with open("/sd/AQ/prt05.txt", "a") as prt05 :
            prt05.write(str(valuesDict["AQ"]["prt05"]) + " , ")
        with open("/sd/AQ/prt10.txt", "a") as prt10 :
            prt10.write(str(valuesDict["AQ"]["prt10"]) + " , ")
        with open("/sd/AQ/prt25.txt", "a") as prt25 :
            prt25.write(str(valuesDict["AQ"]["prt25"]) + " , ")
        with open("/sd/AQ/prt50.txt", "a") as prt50 :
            prt50.write(str(valuesDict["AQ"]["prt50"]) + " , ")
        with open("/sd/AQ/prt100.txt", "a") as prt100 :
            prt100.write(str(valuesDict["AQ"]["prt100"]) + " , ")


## micro SD card ##

# (Instanciation de la carte microSD au sommet du code pour raison technique)


with open("/sd/PHT/Pressure.txt", "r") as f:
    lines = f.readlines()
    print("Printing lines in file:\n")
    for line in lines:
        print(line)

#microSD.print_directory("/sd")


