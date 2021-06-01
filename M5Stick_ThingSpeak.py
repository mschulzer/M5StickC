import urequests
import network
from m5stack import btnA
from m5stack import lcd

lcd.orient(lcd.LANDSCAPE)
lcd.clear()
lcd.print("System klar ...", 30, 32)

net = network.WLAN(network.STA_IF)
net.active(True)
net.connect("...", "...")

thingspeak_url = 'http://api.thingspeak.com/update?api_key='
thingspeak_key = '...'

field1 = '10'
field2 = '11'

data = {'field1':field1, 'field2':field2}
headers = {'Content-Type': 'application/json'}

while True:
    if btnA.wasPressed():
        lcd.clear()
        lcd.print("Tryk registreret!", 30, 32)
        request = urequests.post(thingspeak_url + thingspeak_key,json=data,headers=headers)

        lcd.clear()
        lcd.print("System klar ...", 30, 32)

request.close()
