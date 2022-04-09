# CanSat (mini-satellite)

The CanSat will take measurements twice a second while in the air. 

The CanSat can be broken down in four main components (relevant to the codind aspects).  

## 1. Raspberry Pi Pico

The Raspberry Pi Pico serves as a mini-computer that controls and communicates with the three other components.  

## 2. PHT sensor

Adafruit's PHT Sensor will be used to measure the evolution of pressure, humidity and temperature throughout the flight. 

## 3. Air quality sensor

Adafruit's PMSA003I Air Quality Breakout will be utilized to track the presence of microparticules, heavy metals, as well 
  as other environmental metrics in the air throughout the flight.  

## 4. Onboard radio

Adafruit's RFM9X LoRa Radio will send the data to the ground station.
