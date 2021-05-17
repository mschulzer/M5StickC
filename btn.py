from m5stack import M5Led
from m5stack import btnA, btnB
import time

M5Led.off()
ledtoggle = 0

while True:
    if btnA.wasPressed():

        if ledtoggle == 0:
            M5Led.on()
            ledtoggle = 1
        else:
            M5Led.off()
            ledtoggle = 0
