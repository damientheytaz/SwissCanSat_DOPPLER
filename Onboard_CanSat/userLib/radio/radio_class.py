import adafruit_rfm9x
import board
import busio
import digitalio

class Radio :

    def __init__(self, spi) :
        self.cs = digitalio.DigitalInOut(board.GP17)
        self.reset = digitalio.DigitalInOut(board.GP22)
        self.frequency = 433.0
        self.tx_power = 13
        self.radio = adafruit_rfm9x.RFM9x(spi, self.cs, self.reset, self.frequency)

    def send(self, data):
        self.radio.send(bytes(str(data), "utf-8"))

    def __del__(self) :
        pass
