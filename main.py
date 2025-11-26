from airplane import *
from rotation_matrixes import *
from scipy.spatial.transform import Rotation as R

# Эйлер (вырождаемость нутация 0 или 180 = "замок")
A_zxz = R.from_euler("ZXZ", [30, 180, 180], degrees=True)
A1 = A_zxz.as_matrix()
A2 = A_z(35) @ A_x(180) @ A_z(185)
print("Match: ", np.allclose(A1, A2))

# Самолётные (вырождаемость тангаж 90 или -90)
A_zxy = R.from_euler("ZXY", [30, 90, 180], degrees=True)
A3 = A_zxy.as_matrix()
A4 = A_z(25) @ A_x(90) @ A_y(185)
print("Match: ", np.allclose(A3, A4))

#draw(airplane)
#plt.pause(100)
