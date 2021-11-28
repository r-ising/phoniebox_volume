#!/usr/bin/env python3

from mpd import MPDClient
from RPi import GPIO

# LED pin mapping.
red = 18
green = 15
blue = 14

# GPIO setup.
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(red, GPIO.OUT)
GPIO.setup(green, GPIO.OUT)
GPIO.setup(blue, GPIO.OUT)

# Set up colors using PWM so we can control individual brightness.
RED = GPIO.PWM(red, 100)
GREEN = GPIO.PWM(green, 100)
BLUE = GPIO.PWM(blue, 100)
RED.start(100)
GREEN.start(100)
BLUE.start(100)


# Set a color by giving R, G, and B values of 0-100.
def set_color(rgb=[]):
    RED.ChangeDutyCycle(rgb[0])
    GREEN.ChangeDutyCycle(rgb[1])
    BLUE.ChangeDutyCycle(rgb[2])


# volume 0 = 100 % green
# volume 25 = 75 % green && 25 % red
# volume 50 = 50% green && 50% red
# volume 100 = 0% green & 100 % red
def display_volume(volume):
    max_file = "/home/pi/RPi-Jukebox-RFID/settings/Max_Volume_Limit"
    vol = min(round(int(volume) / get_int(max_file) * 100), 100)
    set_color([100 - vol, 100, vol])


def get_int(file):
    try:
        with open(file) as f:
            lines = f.readlines()

        return int(lines[0])
    except:
        return -1


client = MPDClient()
client.timeout = 10
client.idletimeout = None
client.connect("localhost", 6600)

while True:
    display_volume(client.status()['volume'])
    # wait for change
    client.idle()

client.close()
client.disconnect()
