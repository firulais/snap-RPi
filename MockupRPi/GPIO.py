# Mockup for RPi.GPIO - A module to control Raspberry Pi GPIO channels
# https://pypi.python.org/pypi/RPi.GPIO
# You could try gpiozero library instead of RPi.GPIO.

# version of RPi.GPIO
VERSION = 0

HIGH = 1
LOW = 0

HARD_PWM = 1

BOARD = 10
BCM = 11

OUT = 1
IN = 1

PUD_OFF = 1
PUD_UP = 1
PUD_DOWN = 1
RISING = 1
FALLING = 1
BOTH = 1

# discover information about your RPi
RPI_INFO = 1

# GPIO.setmode(GPIO.BOARD)
# python function setmode(mode)
def setmode(mode):
   print("setmode", mode)

# mode = GPIO.getmode()
def getmode():
   #The mode will be GPIO.BOARD, GPIO.BCM or None
   return 1

# GPIO.setup(channel, GPIO.IN)
# GPIO.setup(channel, GPIO.OUT, initial=GPIO.HIGH)
# GPIO.setup(chan_list, GPIO.OUT)
# python function setup(channel(s), direction, pull_up_down=PUD_OFF, initial=None)
def setup(channel, b):
   print("setup", channel, b)

# GPIO.output(channel, value)
# GPIO.output(chan_list, GPIO.LOW)
# GPIO.output(chan_list, (GPIO.HIGH, GPIO.LOW))
# python function output(channel(s), value(s))
def output(channel, value):
   print("output", channel, value)
# GPIO.input(channel)
def input(channel):
   return 1

# python function add_event_callback(gpio, callback)
def add_event_callback(gpio, callback):

# python function add_event_detect(gpio, edge, callback=None, bouncetime=None)
def add_event_detect(gpio, edge, callback=None, bouncetime=None):

# python function remove_event_detect(gpio)
def remove_event_detect(gpio):

# python function value = event_detected(channel)
def event_detected(channel):
	return 1

# python function channel = wait_for_edge(channel, edge, bouncetime=None, timeout=None)
def wait_for_edge(channel, edge, bouncetime=None, timeout=None):
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
def cleanup(channel):
   print('cleanup', channel)

# GPIO.setwarnings(False)
# python function setwarnings(state)
def setwarnings(state):
   print(setwarnings, state)