from pyfirmata import Arduino
from time import sleep

board = Arduino('/dev/cu.usbmodem14101')
servo = board.get_pin('d:9:s')
pos = 0
def call (x, y):
    for pos in range(0, 181):
        servo.write(pos)
        sleep(x)
    sleep(y)
    servo.write(0)
    sleep(0.1)
