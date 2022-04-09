import time
import adafruit_sdcard
import board
import busio
import digitalio
import microcontroller
import storage
import userLib.SD as sd

# Define the onboard led
led = digitalio.DigitalInOut(board.GP25)
led.direction = digitalio.Direction.OUTPUT

SD_CS = board.GP13
spi = busio.SPI(board.GP10, board.GP11, board.GP8)
sdCard = sd.SD(spi,SD_CS)
print("Logging temperature to filesystem")
# append to the file!
#while True: # Tourne en continu
for i in range(10):
    # open file for append
    with open("/sd/temperature.txt", "a") as f:
        led.value = True   # turn on LED to indicate we're writing to the file
        t = microcontroller.cpu.temperature
        print("t =", t)
        print("Temperature = {:0.1f} en pourcents".format(t))
        f.write("nous affichons la variable:{:0.1f} en pourcents".format(t))
        led.value = False   # turn off LED to indicate we're done
    # file is saved
    time.sleep(1)
