import matplotlib.pyplot as plt

from airplane import *
from rotation_matrixes import *
from scipy.spatial.transform import Rotation as R

airplane_0 = A_z(90) @ airplane

airplane_now = airplane_0
draw(airplane_0)
plt.pause(5)
airplane_now = A_y(90) @ airplane_now
draw(airplane_now)
plt.pause(5)
airplane_now = A_x(90) @ airplane_now
draw(airplane_now)
plt.pause(5)
airplane_now = A_z(120) @ airplane_now
draw(airplane_now)
plt.pause(5)