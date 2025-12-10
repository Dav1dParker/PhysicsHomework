import matplotlib.pyplot as plt

from airplane import *
from rotation_matrixes import *
from scipy.spatial.transform import Rotation as R

def w(t):
    return np.array([0,0,1])

airplane_0 = A_z(90) @ airplane

delta_t = 0.1
draw(airplane_0)
plt.waitforbuttonpress()

A_i = np.eye(3)
t_i = 0
for i in range(100):
    [p, q, r] = w(t_i)
    Omega = np.array([[ 0, -r,  q],
                      [ r,  0, -p],
                      [-q,  p,  0]])
    A_i_dot = Omega @ A_i
    t_i += delta_t
    A_i += A_i_dot * delta_t
    print(f"t: {t_i}, det: {np.linalg.det(A_i)}")
    airplane_i = A_i @ airplane_0
    draw(airplane_i)
    plt.waitforbuttonpress()