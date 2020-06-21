from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers, models
import numpy as np
import ardu_comm
import csv2motor
import audio
import numpy

for i in csv2motor.call():
    i.pop(0) # removes midi_time
    motor = i[0]
    a = i[1] # attack
    r = i[2] # release
    on = True
    print(i)

    attack = tf.Variable(np.random.uniform(0, 3), trainable = True, name = 'attack')
    release = tf.Variable(np.random.uniform(0, 10), trainable = True, name = 'release')

    def model(attack, a, release, r):
        ardu_comm.call(attack, release) # passes the guess into the ardu
        amp, dur = audio.call() # collects the produced amplitude and duration
        return tf.add(tf.reduce_mean(tf.square(amp - a)), tf.reduce_mean(tf.square(dur - r))) # MSE here

    optimizer = tf.optimizers.SGD(learning_rate = 0.1)

    while on == True:
        with tf.GradientTape() as g:
             loss = model(attack, a, release, r)
        gradients = g.gradient(loss, [attack, release])
        optimizer.apply_gradients(zip(gradients, [attack, release]))
        if loss < 0.01:
            on = False
            print('motor: %i with attack: %i and release: %f has been correctly approximated.')
            # add (note, attack, release) to database
            # add (motor, velocity, stall) to databse


    print('all the inputs of this song have been approximated')
    # graph 1: (note, attack, release)
    g = numpy.array(csv2motor.call())
    h = numpy.delete(g, 0, 1) #removes the time
    all_motors = h[:, 0]
    all_attacks = h[:, 1]
    all_releases = h[:, 2]
    fig = plt.figure()
    ax = fig.gca(projection = '3d')
    ax.set_title('Sonate Opus 35 - Frederic Chopin')
    ax.set_xlabel('motor')
    ax.set_ylabel('release')
    ax.set_zlabel('attack')
    ax.set_xlim(0, numpy.amax(all_motors))
    ax.set_ylim(0, int(numpy.amax(all_releases)) + 1)
    ax.set_zlim(0, numpy.amax(all_attacks))
    ax.scatter(all_motors, all_releases, all_attacks, c = all_attacks, cmap = 'viridis', linewidth=0.5);
    plt.show()
    # graph 2: (motor, velocity, stall)
