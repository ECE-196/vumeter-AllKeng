import board
from digitalio import DigitalInOut, Direction
from analogio import AnalogIn
from time import sleep
import math

# setup pins
microphone = AnalogIn(board.IO1)

status = DigitalInOut(board.IO17)
status.direction = Direction.OUTPUT

led_pins = [
    board.IO21,
    board.IO26, # type: ignore
    board.IO47,
    board.IO33, 
    board.IO34, 
    board.IO48,
    board.IO35,
    board.IO36,
    board.IO37,
    board.IO38,
    board.IO39
]

threshold = [
    24000,
    25181.82,
    26363.64,
    28545.46,
    29727.28,
    30909.1,
    32090.92,
    34272.74,
    36454.56,
    38636.38,
    45818.2
    ]
leds = [DigitalInOut(pin) for pin in led_pins]

for led in leds:
    led.direction = Direction.OUTPUT

# main loop
while True:
    volume = microphone.value

     # Check each threshold and turn on LED if volume exceeds threshold
    for i, thresh in enumerate(threshold):
        print(volume)
        if volume > thresh:
            leds[i].value = True
        else:
            leds[i].value = False

    sleep(0.15)  # Adjust sleep time as needed

    # max 48000
    # min 24000

    #leds[0].value = not leds[0].value
    #leds[1].value = not leds[0].value

    # instead of blinking,
    # how can you make the LEDs
    # turn on like a volume meter?
