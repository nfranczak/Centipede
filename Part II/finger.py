import tensorflow as tf
import numpy as np
import visualizer
import ardu_comm
import csv2motor
import lookup
import audyoo
import adder

for i in csv2motor.call():
    i.pop(0) # removes midi_time
    motor = i[0]
    a = i[1] # attack
    r = i[2] # release
    on = True

    attack = tf.Variable(np.random.uniform(0, 3), trainable = True, name = 'attack')
    release = tf.Variable(np.random.uniform(0, 10), trainable = True, name = 'release')

    def model(attack, a, release, r):
        ardu_comm.call(attack, release) # passes the guess into the ardu
        amp, dur = audyoo.call() # collects the produced amplitude and duration
        return tf.add(tf.reduce_mean(tf.square(amp - a)), tf.reduce_mean(tf.square(dur - r))) # MSE here

    optimizer = tf.optimizers.SGD(learning_rate = 0.1)

    while on == True:
        if lookup.look() == True:
            pass #make sure pass is working as exepected here
        else:
            with tf.GradientTape() as g:
                 loss = model(attack, a, release, r)
            gradients = g.gradient(loss, [attack, release])
            optimizer.apply_gradients(zip(gradients, [attack, release]))
            if loss < 0.01:
                on = False
                print('note: %i with attack: %i and release: %f has been correctly approximated.' % (motor, a, r))
                adder.append('piano databse.csv', [motor, a, r]) # adds (note, attack, release) to database
                adder.append('motor databse.csv', [motor, attack, release]) # adds (motor, velocity, stall) to database


print('all the inputs of this song have been approximated')
visualizer.view_piano()
visualizer.view_centi()
