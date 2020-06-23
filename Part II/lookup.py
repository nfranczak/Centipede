from numpy import genfromtxt
import numpy as np

def look(motor, attack, release): #attack and release here are wrt piano metrics
    a = genfromtxt('piano database.csv', delimiter=',')
    if [motor, attack, release] in a:
        return True
    else:
        return False
