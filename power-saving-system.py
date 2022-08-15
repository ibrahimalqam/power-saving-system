from microbit import *
from ssd1306 import initialize, clear_oled
from ssd1306_text import add_text


initialize()
clear_oled()
sleep(1000)
cost = 0

while True:
    motion = pin1.read_digital()
    if motion == 1:
        pin0.write_digital(1)
        cost = cost + 1
        add_text(0, 0, "Light: ON ")
    else:
        pin0.write_digital(0)
        add_text(0, 0,"Light OFF")
        
    add_text(0, 1, "Running Time:")
    add_text(0,2, str(cost/10))

        