import matplotlib.pyplot as plt

from airplane import *
from rotation_matrixes import *


def w(t):
    return np.array([1,1,0])

airplane_0 = A_z(90) @ airplane

delta_t = 0.1

t_i = 0
phi_i = 0
psi_i = 0
tetta_i = np.pi/2
A_i = A_z(np.degrees(psi_i)) @ A_x(np.degrees(tetta_i)) @ A_z(np.degrees(phi_i))
airplane_i = A_i @ airplane_0
draw(airplane_i)
plt.waitforbuttonpress()
for i in range(100000):
    A_i = A_z(np.degrees(psi_i)) @ A_x(np.degrees(tetta_i)) @ A_z(np.degrees(phi_i))
    [p, q, r] = A_i.T @ w(t_i)
    print(np.degrees(psi_i),np.degrees(tetta_i),np.degrees(phi_i))
    tetta_i_dot = p * np.cos(phi_i) - q * np.sin(phi_i)
    psi_i_dot = (1/np.sin(tetta_i))*(p*np.sin(phi_i)+q*np.cos(phi_i))
    phi_i_dot = r - (1/np.tan(tetta_i))*(p*np.sin(phi_i)+q*np.cos(phi_i))
    psi_i += psi_i_dot * delta_t
    tetta_i += tetta_i_dot * delta_t
    phi_i += phi_i_dot * delta_t
    A_i = A_z(np.degrees(psi_i)) @ A_x(np.degrees(tetta_i)) @ A_z(np.degrees(phi_i))
    airplane_i = A_i @ airplane_0
    draw(airplane_i)
    plt.waitforbuttonpress()