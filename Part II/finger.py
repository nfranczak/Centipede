import matplotlib.pyplot as plt
from ternsorflow import keras
import tensorflow as tf
import numpy as np
import ardu_comm
import csv2motor
import audio

for i in csv2motor.call():
    i.pop(0) # removes midi_time
    motor = i[0]
    a = i[1] # attack
    r = i[2] # release
    on = True

    attack = tf.Variable(np.random.uniform(0, 3), name = 'attack') #initialization at beginning of training for each (a,r)
    release = tf.Variable(np.random.uniform(0, 10), name = 'release')

    def model(attack, a, release, r):
        ardu_comm.call(attack, release) # passes the guess into the ardu
        amp, dur = audio.call() # collects the produced amplitude and duration
        return tf.add(tf.reduce_mean(tf.square(amp - a)), tf.reduce_mean(tf.square(dur - r))) # MSE here

    optimizer = tf.keras.optimizers.SGD(learning_rate = 0.1)

    while on == True:
        with tf.GradientTape() as g:
             loss = model(attack, a, release, r)
        gradients = g.gradient(loss, [attack, release])
        optimizer.apply_gradients(zip(gradients, [attack, release]))
        if loss < 0.1:
            on = False


    # graph 1: x: attack & y: release & z: note
    #       2: x: velcity & y:stall & z: motor
