import board
from adafruit_seesaw.seesaw import Seesaw
from gpiozero import OutputDevice

class Relay(OutputDevice):
    def __init__(self, pin, active_high):
        super(Relay, self).__init__(pin, active_high)


class MoistureSensor():
    def __init__(self) -> None:
        self.i2c_bus = board.I2C()
        self.seesaw = Seesaw(self.i2c_bus, addr=0x36)

    def get_moisture(self):
        return self.seesaw.moisture_read()
    
    def get_temperature(self):
        return self.seesaw.get_temp()
