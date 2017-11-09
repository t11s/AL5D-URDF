import ikpy
import sys
import numpy as np
from ikpy import plot_utils
import matplotlib.pyplot as plt

def normalize(x):
	twopi=2*3.1415926535
	return x%twopi

my_chain = ikpy.chain.Chain.from_urdf_file("AL5D_arm.URDF")
target_vector = [int(sys.argv[1]),int(sys.argv[2]),int(sys.argv[3])] 
print target_vector
target_frame = np.eye(4)
target_frame[:3, 3] = target_vector
fk=map(normalize,my_chain.inverse_kinematics(target_frame))
print("The angles of each joints are : ", fk)
ax = plot_utils.init_3d_figure()
my_chain.plot(fk, ax, target=target_vector)
plt.show()
