from adafruit_pm25.i2c import PM25_I2C

class AirQuality:

    def __init__(self, i2c) :
        self.airQualitySensor = PM25_I2C(i2c)
        self.aqValueDict = {}

    def getAirQuality(self) :
        self.aqValueDict = self.airQualitySensor.read()
        #
        # Raccourcir les clés :
        #
        self.aqValueDict["pm10e"] = self.aqValueDict["pm10 env"]
        del self.aqValueDict["pm10 env"]
        #
        self.aqValueDict["pm25e"] = self.aqValueDict["pm25 env"]
        del self.aqValueDict["pm25 env"]
        #
        self.aqValueDict["pm100e"] = self.aqValueDict["pm100 env"]
        del self.aqValueDict["pm100 env"]
        #
        self.aqValueDict["pm10s"] = self.aqValueDict["pm10 standard"]
        del self.aqValueDict["pm10 standard"]
        #
        self.aqValueDict["pm25s"] = self.aqValueDict["pm25 standard"]
        del self.aqValueDict["pm25 standard"]
        #
        self.aqValueDict["pm100s"] = self.aqValueDict["pm100 standard"]
        del self.aqValueDict["pm100 standard"]
        #
        self.aqValueDict["prt03"] = self.aqValueDict["particles 03um"]
        del self.aqValueDict["particles 03um"]
        #
        self.aqValueDict["prt05"] = self.aqValueDict["particles 05um"]
        del self.aqValueDict["particles 05um"]
        #
        self.aqValueDict["prt10"] = self.aqValueDict["particles 10um"]
        del self.aqValueDict["particles 10um"]
        #
        self.aqValueDict["prt25"] = self.aqValueDict["particles 25um"]
        del self.aqValueDict["particles 25um"]
        #
        self.aqValueDict["prt50"] = self.aqValueDict["particles 50um"]
        del self.aqValueDict["particles 50um"]
        #
        self.aqValueDict["prt100"] = self.aqValueDict["particles 100um"]
        del self.aqValueDict["particles 100um"]
        #
        return self.aqValueDict
