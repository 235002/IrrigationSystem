#!/usr/bin/env python3
from Hardware import Relay
import time

relay = Relay(12, False)

time.sleep(1)
relay.on()
time.sleep(1)
relay.off()
