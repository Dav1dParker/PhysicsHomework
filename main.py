import matplotlib.pyplot as plt

from airplane import *
from rotation_matrixes import *
from scipy.spatial.transform import Rotation as R

airplane_0 = A_z(90) @ airplane
draw(airplane_0)
plt.waitforbuttonpress()

airplane_i = airplane_0
for i in range(36):
    airplane_i = A_z(i*10) @ airplane_0
    draw(airplane_i)
    plt.waitforbuttonpress()