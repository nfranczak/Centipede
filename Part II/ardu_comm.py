from pyfirmata import Arduino
from time import sleep # this is in seconds FYI not milli seconds
#ALWAYS CONNECT ARDU TO BOTTOM USB PORT
board = Arduino('/dev/cu.usbmodem14101')
servo = board.get_pin('d:9:s')
pos = 0
# make sure you open up the arduino ide and then do:
#   file --> examples --> firmata --> standardfirmata
#   upload this and then the code should work
# x controls how fast the servo descends
# y controls how long the servo is in this position
# z controls how much the finger descends between 120 and 0
def call (x, y, z):
    for pos in range(120, z, -1):
        servo.write(pos)
        sleep(x)
    sleep(y)
    servo.write(120)
    sleep(.1)
