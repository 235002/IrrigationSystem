import time
import datetime
import json
from Hardware import MoistureSensor

ms = MoistureSensor()
data = []
resultFile = "result.json"


try:
    while True:
        moistureLevel = ms.get_moisture()
        temperature = ms.get_temperature()
        t = time.localtime()
        data.append({"temp": temperature, "timestamp": time.strftime("%H:%M:%S", t), "moisture": moistureLevel})
        print("temp: " + str(temperature) + "  moisture: " + str(moistureLevel))
        time.sleep(1)
except KeyboardInterrupt:
    pass

with open(resultFile, "w") as file:
    json.dump(data, file)
