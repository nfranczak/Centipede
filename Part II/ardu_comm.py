from pyfirmata import Arduino
from time import sleep # this is in seconds NOT milliseconds
#ALWAYS CONNECT ARDU TO BOTTOM USB PORT
board = Arduino('/dev/cu.usbmodem14101')
servo = board.get_pin('d:9:s')
pos = 0
# make sure you open up the arduino ide and then do:
#   file --> examples --> firmata --> standardfirmata
#   upload this and then the code should work
# x controls how fast the servo descends downwards
# y controls how long the servo is in this position
# z controls how fast the servo goes back up
# NOTE: x and z are arrays that contain 55 unique values
# the fun is figuring out what those 55 values should be for each attack and release :)
def call (x, y, z):
    for pos in range(120, 65, -1):
        servo.write(pos)
        sleep(x)
    sleep(y)
    for pos in range(65, 120):
        servo.write(pos)
        sleep(z)
