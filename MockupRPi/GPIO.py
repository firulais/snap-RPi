# Mockup for RPi.GPIO - A module to control Raspberry Pi GPIO channels
# https://pypi.python.org/pypi/RPi.GPIO
# You could try gpiozero library instead of RPi.GPIO.

BOARD = 1
OUT = 1
IN = 1
BCM = 1

def setmode(a):
   print("setmode", a)
def setup(a, b):
   print("setup", a, b)
def output(a, b):
   print("output", a, b)
def input(a):
   return 1
def cleanup():
   print('cleanup')
def setmode(a):
   print("setmode", a)
def setwarnings(flag):
   print(setwarnings, flag)