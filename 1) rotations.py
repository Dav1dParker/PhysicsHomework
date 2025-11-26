from airplane import *
from rotation_matrixes import *

A1 = A_x(46) @ A_y(13)
A2 = A_y(13) @ A_x(46)
print("Match: ", np.allclose(A1, A2))
A3 = A_x(90) @ A_y(180) @ A_z(180) @ A_x(90)
A4 = np.eye(3)
print("Match: ", np.allclose(A3, A4))


#draw(airplane)
#plt.pause(100)
