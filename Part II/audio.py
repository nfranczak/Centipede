import pygame
from pygame.locals import *
from pygame import midi
list = []
# list[0] is the velocity
# list[1] is the midi start time
# list[2] is the off velocity which is always 0
# list[3] is the midi end time

def call(input_device):
    # pygame.midi.init()
    while len(list) < 4:
        if input_device.poll() == True:
            event = input_device.read(1)[0]
            data = event[0]
            list.append(data[2])
            list.append(event[1])
    # pygame.midi.quit()
    time = (list[3] - list[1])/1000
    return (list[0], time)


if __name__ == '__main__':
    pygame.midi.init()
    print(call(pygame.midi.Input(0)))
    pygame.midi.quit()

    # time = (list[3] - list[1])/1000
    # print(list[0], time)
