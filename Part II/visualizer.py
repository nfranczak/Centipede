from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from numpy import genfromtxt
import numpy as np

def view_piano():
    # to view databse of piano points that have been correctly approximated
    a = genfromtxt('piano database.csv', delimiter=',')
    all_motors = a[:, 0]
    all_attacks = a[:, 1]
    all_releases = a[:, 2]
    fig = plt.figure()
    ax = fig.gca(projection = '3d')
    ax.set_title('Piano Datapoints')
    ax.set_xlabel('note number')
    ax.set_ylabel('release')
    ax.set_zlabel('attack')
    ax.set_xlim(0, np.amax(all_motors))
    ax.set_ylim(0, int(np.amax(all_releases)) + 1)
    ax.set_zlim(0, np.amax(all_attacks))
    ax.scatter(all_motors, all_releases, all_attacks, c = all_attacks, cmap = 'viridis', linewidth=0.5);
    plt.show()

def view_centi():
    # to view databse of centipede points that have been correctly approximated
    a = genfromtxt('piano database.csv', delimiter=',')
    all_motors = a[:, 0]
    all_attacks = a[:, 1]
    all_releases = a[:, 2]
    fig = plt.figure()
    ax = fig.gca(projection = '3d')
    ax.set_title('Centipede Datapoints')
    ax.set_xlabel('note number')
    ax.set_ylabel('release')
    ax.set_zlabel('attack')
    ax.set_xlim(0, np.amax(all_motors))
    ax.set_ylim(0, int(np.amax(all_releases)) + 1)
    ax.set_zlim(0, np.amax(all_attacks))
    ax.scatter(all_motors, all_releases, all_attacks, c = all_attacks, cmap = 'viridis', linewidth=0.5);
    plt.show()
