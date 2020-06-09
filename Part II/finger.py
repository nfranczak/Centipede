import matplotlib.pyplot as plt
import tensorflow as tf
import numpy as np
import ardu_comm
import csv2motor
import audio


on = True

for i in csv2motor.call():
    i.pop(0) # removes midi_time
    motor = i[0]
    a = i[1] # attack
    r = i[2] # release

    learning_rate = 0.01
    attack = tf.Variable(np.random.uniform(0, 3), name = 'attack')
    release = tf.Variable(np.random.uniform(0, 10), name = 'release')

    def model():
        ardu_comm.call(attack, release) # passes the guess into the ardu
        attack, release = audio.call() # collects the produced amplitude and duration i.e. attack & release
        return (attack, release)

    def mean_square(attack, a, release, r):
        return tf.add(tf.reduce_mean(tf.square(attack - a)),
                      tf.reduce_mean(tf.square(release - r)))

    optimizer = tf.optimizers.SGD(learning_rate)

    def run_optimization():
        with tf.GradientTape() as g:
             pred = model()
             loss = mean_square(attack, a, release, r)
        gradients = g.gradient(loss, [attack, release])
        optimizer.apply_gradients(zip(gradients, [attack, release]))
        if loss < 0.1:
            on = False

    while on == True:
        run_optimization()

    # matplotlib stuff here for data visualization
    # when loss is low enuf add points to database
