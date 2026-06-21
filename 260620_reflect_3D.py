# %%
import os
import numpy as np
import matplotlib.pyplot as plt

os.system("cls")


#  circle and sphere radius  
r = 1

# initial and final points
initial_point = np.array([0.5,-0.5,0.5])
final_point   = np.array([1.5,1.5,1.5]) 

print(initial_point)
print(final_point)

distance = np.sqrt(np.sum((final_point - initial_point)**2))
# dist_ini = np.sqrt(initial_point[0]**2 + initial_point[1]**2 + initial_point[2]**2)
# dist_final = np.sqrt(final_point[0]**2 + final_point[1]**2 + final_point[2]**2)

# print(distance)
# print(dist_ini)
# print(dist_final)


# find the vector from initial to final point
v_initial_to_final = final_point - initial_point; 
 



# theta and phi points for plotting the sphere
theta_points = np.linspace(-2*np.pi, 2*np.pi, 1001)
phi_points = np.linspace(0, np.pi,1001)

# # plot circle and points
# plt.plot(r*np.cos(theta_points), r*np.sin(theta_points))
# plt.plot(initial_point[0],initial_point[1],'ro',markersize=5)
# plt.plot(final_point[0],  final_point[1],  'bo',markersize=5)
# plt.grid()
# plt.axis("equal")
# plt.title("plot circle and points")
# plt.xlabel("X")
# plt.ylabel("Y")
# plt.zlabel("Z")
# plt.show()

theta_points_mesh, phi_points_mesh = np.meshgrid(theta_points, phi_points)

# points on the sphere
x_sphere = r * np.sin(phi_points_mesh) * np.cos(theta_points_mesh)
y_sphere = r * np.sin(phi_points_mesh) * np.sin(theta_points_mesh)
z_sphere = r * np.cos(phi_points_mesh)


# %% 
fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")

# plot sphere
ax.plot_surface(x_sphere, y_sphere, z_sphere, alpha=0.3, color='orange', edgecolor='none')

# plot initial and final points
ax.scatter(initial_point[0], initial_point[1], initial_point[2], color='red', s=100, label='Initial Point')
ax.scatter(final_point[0], final_point[1], final_point[2], color='blue', s=100, label='Final Point')

# plot line between initial and final points
ax.plot( [initial_point[0], final_point[0]], [initial_point[1], final_point[1]], [initial_point[2], final_point[2]], color='black', label='Line between Points')  

ax.grid()
ax.legend(frameon=False, loc="best", fontsize=8)


ax.set_title("3D Sphere with Initial and Final Points", fontsize=14)
ax.tick_params(axis="x", labelsize=14)
ax.tick_params(axis="y", labelsize=14)
ax.tick_params(axis="z", labelsize=14)
ax.set_xlabel("X", fontsize=14)
ax.set_ylabel("Y", fontsize=14)
ax.set_zlabel("Z", fontsize=14)

plt.show()
print(distance)

# # plot initial and final points
# # fig = plt.figure()
# plt.plot(initial_point)
# plt.plot(final_point)

# plt.title("Initial and Final Points")
# plt.xlabel("X")
# plt.ylabel("Y")
# plt.zlabel("Z")
# plt.show()







