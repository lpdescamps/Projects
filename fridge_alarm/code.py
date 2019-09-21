# Write your code here :-)
# Green = Fridge
# Yellow = Freezer
# Red = Buzzer
# Black = GND

import time
import board
from digitalio import DigitalInOut, Direction, Pull
import adafruit_dotstar

ledrgb = adafruit_dotstar.DotStar(board.APA102_SCK, board.APA102_MOSI, 1)

led = DigitalInOut(board.D13)
led.direction = Direction.OUTPUT

buzzer = DigitalInOut(board.A2)
buzzer.direction = Direction.OUTPUT

fridge = DigitalInOut(board.D2)
fridge.direction = Direction.INPUT
fridge.pull = Pull.UP
freezer = DigitalInOut(board.D3)
freezer.direction = Direction.INPUT
freezer.pull = Pull.UP

timer = 30
ledrgb.brightness = 0.3

while True:
    if freezer.value:
        buzzer.value = False
        print('freezer door open')
        led.value = True
        count = 0
        while count < timer:
            ledrgb[0] = (0, 0, 0)
            time.sleep(1)
            count = count + 1
            print(count, 'sec')
            ledrgb[0] = (255, 255, 0)
            if freezer.value is False:
                break
        while freezer.value is True:
            print('freezer door open for over', count, 'sec')
            buzzer.value = True
            time.sleep(0.5)
            buzzer.value = False
            time.sleep(0.5)
        else:
            pass

    if fridge.value:
        print('fridge door open')
        buzzer.value = False
        led.value = True
        count = 0
        while count < timer:
            ledrgb[0] = (0, 0, 0)
            time.sleep(1)
            count = count + 1
            print(count, 'sec')
            ledrgb[0] = (0, 128, 0)
            if fridge.value is False:
                break
        while fridge.value is True:
            print('fridge door open for over', count, 'sec')
            buzzer.value = True
            time.sleep(0.5)
            buzzer.value = False
            time.sleep(0.5)
        else:
            pass

    else:
        print('doors closed')
        led.value = False
        buzzer.value = False
        ledrgb[0] = (0, 0, 0)

    time.sleep(0.01)
