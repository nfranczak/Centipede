from pyfirmata import Arduino
from time import sleep # this is in seconds FYI not milli seconds
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
def call (x, y, z):
    for pos in range(120, 65, -1):
        servo.write(pos)
        sleep(x)
    sleep(y)
    for pos in range(65, 120):
        servo.write(pos)
        sleep(z)
# NOTE: the code below is used to create a practice trill to test how many times a key can be pressed in a second
# The answer is ~8 which should be suffice
# NOTE: there is a .mov in the design section showing the trill
# if __name__ == "__main__":
    # call(.000483, .025, .000483)
    # sleep(.01)
    # call(.000483, .025, .000483)
    # sleep(.01)
    # call(.000483, .025, .000483)
    # sleep(.01)
    # call(.000483, .025, .000483)
    # call(.000483, .025, .000483)
    # sleep(.01)
    # call(.000483, .025, .000483)
    # sleep(.01)
    # call(.000483, .025, .000483)
    # sleep(.01)
    # call(.000483, .025, .000483)
