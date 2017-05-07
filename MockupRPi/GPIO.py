#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Mockup for RPi.GPIO - A module to control Raspberry Pi GPIO channels
# https://pypi.python.org/pypi/RPi.GPIO
#
# Mockup file structure:
# /sys/class/gpio/export
# /sys/class/gpio/unexport
# /sys/class/gpio/gpio22/value
# /sys/class/gpio/gpio22/direction
# 
# /sys/class/gpio/gpio22/device
# /sys/class/gpio/gpio22/power
# /sys/class/gpio/gpio22/subsystem
# http://www.netzmafia.de/skripten/hardware/RasPi/RasPi_GPIO_Shell.html

import os

# version of RPi.GPIO
VERSION = "0.6.3"

LOW = 0
HIGH = 1

OUT = 0 # "out"
IN = 1 # "in"

HARD_PWM = 43

BOARD = 10
BCM = 11

PUD_OFF = 20
PUD_DOWN = 21
PUD_UP = 22

RISING = 31
FALLING = 32
BOTH = 33

# discover information about your RPi
RPI_INFO = {'P1_REVISION': 3, 'MANUFACTURER': 'Sony', 'REVISION': 'a02082', 'RAM': '1024M', 'PROCESSOR': 'BCM2837', 'TYPE': 'Pi 3 Model B'}

# Mockup Constants for file handling
IO_PATH = "/sys/class/gpio/"
IO_EXPORT = "export"
IO_UNEXPORT = "unexport"
IO_GPIO = "gpio"
IO_DIRECTION = "direction" # "in" or "out"
IO_VALUE = "value" # 0 (low) or 1 (high)
IO_EDGE = "edge" # "none", "rising", "falling", or "both"
IO_ACTIVE_LOW = "active_low" # 0 (false) or 1 (true)
IO_UEVENT = "uevent" # 

# /sys/class/gpio/export
# /sys/class/gpio/unexport
def _init():
    filename = IO_PATH + IO_EXPORT
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, "w") as f:
        f.write("")

    filename = IO_PATH + IO_UNEXPORT
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, "w") as f:
        f.write("")
        
# GPIO.setmode(GPIO.BOARD)
# python function setmode(mode)
def setmode(mode):       
    print ('setmode', mode)

# cat /sys/class/gpio/gpio22/value
# mode = GPIO.getmode()
def getmode():
   # The mode will be GPIO.BOARD, GPIO.BCM or None
    return 1
    
# GPIO.setup(channel, GPIO.IN)
# GPIO.setup(channel, GPIO.OUT, initial=GPIO.HIGH)
# GPIO.setup(chan_list, GPIO.OUT)
#
# echo "22" > /sys/class/gpio/export
# echo "out" > /sys/class/gpio/gpio22/direction
# echo "0" > /sys/class/gpio/gpio22/value
#
# python function setup(channel(s), direction, pull_up_down=PUD_OFF, initial=None)
def setup(channel, direction):
    print ('setup', channel, direction)
    
    # /sys/class/gpio/gpio22/direction .. "in" or "out"
    filename = IO_PATH + IO_GPIO + str(channel) + "/" + IO_DIRECTION
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, "w") as f:
        if direction == IN:
            f.write("in")
        if direction == OUT:
            f.write("out")

    # /sys/class/gpio/gpio22/value .. 0 (low) or 1 (high)
    value = 0
    filename = IO_PATH + IO_GPIO + str(channel) + "/" + IO_VALUE
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, "w") as f:
        f.write(str(value))   
        
# GPIO.output(channel, value)
# GPIO.output(chan_list, GPIO.LOW)
# GPIO.output(chan_list, (GPIO.HIGH, GPIO.LOW))
# python function output(channel(s), value(s))
def output(channel, value):
    print ('output', channel, value)

    filename = IO_PATH + IO_GPIO + str(channel) + "/" + IO_VALUE
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, "w") as f:
        f.write(str(value))

#simulate signal
def _signal(channel, value):
    print ('output', channel, value)

    filename = IO_PATH + IO_GPIO + str(channel) + "/" + IO_VALUE
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, "w") as f:
        f.write(str(value))
        
# GPIO.input(channel)
def input(channel):
    print ('input', channel)

    value = 0
    
    filename = IO_PATH + IO_GPIO + str(channel) + "/" + IO_VALUE
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, "r") as f:
        value = f.read()
        
    return value
    
# python function add_event_callback(gpio, callback)
def add_event_callback(gpio, callback):
    pass

# python function add_event_detect(gpio, edge, callback=None, bouncetime=None)
def add_event_detect(
    gpio,
    edge,
    callback=None,
    bouncetime=None,
    ):
    pass

# python function remove_event_detect(gpio)
def remove_event_detect(gpio):
    pass

# python function value = event_detected(channel)
def event_detected(channel):
    return 1

# python function channel = wait_for_edge(channel, edge, bouncetime=None, timeout=None)
def wait_for_edge(
    channel,
    edge,
    bouncetime=None,
    timeout=None,
    ):

    return 1

# python function value = gpio_function(channel)
def gpio_function(channel):
    return 1

# GPIO.cleanup()
def cleanup():
    print('cleanup')

# GPIO.cleanup(channel)
# GPIO.cleanup( (channel1, channel2) )
# GPIO.cleanup( [channel1, channel2] )
# echo "22" > /sys/class/gpio/unexport
def cleanup(channel):
    print ('cleanup', channel)
    
# GPIO.setwarnings(False)
# python function setwarnings(state)
def setwarnings(state):
    print (setwarnings, state)


if __name__ == '__main__':
    print('MockupGPIO')
    _init()
    setup(22, OUT)
    output(22, HIGH)
    setup(21, IN)
    _signal(21, HIGH) #simulate signal
    value = input(21)
    print("value="+value)
    print(str(RPI_INFO))
    print(str(RPI_INFO['P1_REVISION']))
    

			