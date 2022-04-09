import board
import busio
import digitalio
import time
from userLib.radio.radio_class import Radio
from userLib.phtSensor.PHT_sensor_class import PhtSensor
from userLib.airQuality.air_quality_class import AirQuality

# Initialisation des ports :

i2c = busio.I2C(scl=board.GP27,sda=board.GP26, frequency=100000)

spi = busio.SPI(clock=board.GP18, MOSI=board.GP19, MISO=board.GP16)


# Initialisation des objets :

radio = Radio(spi)

phtSensor = PhtSensor(i2c)

airQuality = AirQuality(i2c)


# Mesures, stockage local sous forme de dictionnaire (embarqué), envoi à la station au sol :

j = 0
while True :

    # Instanciation du dictionnaire d'empaquetage des données :

    valuesDict = {}
    

    # Prendre les mesures (1x par seconsde) sur le PHT sensor et les inscrire dans un dictionnaire

    phtValues = phtSensor.getPhtValues()
    

    # Prendre les mesures (1x par seconde) sur le air quality sensor et les inscrire dans un dictionnaire

    aqValues = airQuality.getAirQuality()
    

    # Empaquetage des données dans le i-ème dictionnaire :

    valuesDict["PHT"] = phtValues
    
    valuesDict["AQ"] = aqValues

    print("\nTable des données à t=" + str(j) + ":", sorted(valuesDict.items(), key=lambda t: t[0]))


    # Envoi du ième dictionnaire de la radio embarquée à la radio au sol :
    
    radio.send(sorted(valuesDict.items(), key=lambda t: t[0]))

    
    # Incrementer le compteur :
    
    j += 0.5
    

    # Boucle de 0.5 seconde :
    
    time.sleep(0.5)



