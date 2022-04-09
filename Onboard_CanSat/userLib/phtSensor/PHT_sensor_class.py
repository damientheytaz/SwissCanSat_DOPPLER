from adafruit_ms8607 import MS8607

class PhtSensor :

    def __init__(self, i2c) :
        self.phtSensor = MS8607(i2c)
        self.phtValueDict = {}

    def getPhtValues(self) :
        pressure = self.phtSensor.pressure
        temperature = self.phtSensor.temperature
        relative_humidity = self.phtSensor.relative_humidity
        phtValueDict = {"P" : pressure , "H" : relative_humidity , "T" : temperature}
        return phtValueDict
