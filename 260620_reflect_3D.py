# %%
import os
import numpy as np
import matplotlib.pyplot as plt
from sympy import false, true

os.system("cls")

#%%
#  circle and sphere radius  
r = 1

# initial and final points
p_initial_point = np.array([0.5,-0.5,0.5])
p_final_point   = np.array([1.5,1.5,1.5]) 

print(p_initial_point)
print(p_final_point)

distance = np.sqrt(np.sum((p_final_point - p_initial_point)**2))
# dist_ini = np.sqrt(p_initial_point[0]**2 + p_initial_point[1]**2 + p_initial_point[2]**2)
# dist_final = np.sqrt(p_final_point[0]**2 + p_final_point[1]**2 + p_final_point[2]**2)

# print(distance)
# print(dist_ini)
# print(dist_final)

#%%
# find the vector from initial to final point
v_initial_to_final = p_final_point - p_initial_point; 
 
# v_ini_to_final = p_initial_point + t * v_initial_to_final
# I want find the t such that the point is on the sphere, which means its distance from the origin is r(radius of the sphere)
# ||v_ini_to_final|| = r
# ||p_initial_point + t * v_initial_to_final|| = r
# (p_initial_point[0] + t * v_initial_to_final[0])**2 + (p_initial_point[1] + t * v_initial_to_final[1])**2 + (p_initial_point[2] + t * v_initial_to_final[2])**2 = r**2
#  expand the above equation and rearrange it to get a quadratic equation in t
# t**2 * (v_initial_to_final[0]**2 + v_initial_to_final[1]**2 + v_initial_to_final[2]**2) 
# + 2*t*(p_initial_point[0]*v_initial_to_final[0] + p_initial_point[1]*v_initial_to_final[1] + p_initial_point[2]*v_initial_to_final[2]) + 
# (p_initial_point[0]**2 + p_initial_point[1]**2 + p_initial_point[2]**2 - r**2) 
# = 0

a = (v_initial_to_final[0]**2 + v_initial_to_final[1]**2 + v_initial_to_final[2]**2)
b = 2*(p_initial_point[0]*v_initial_to_final[0] + p_initial_point[1]*v_initial_to_final[1] + p_initial_point[2]*v_initial_to_final[2])
c = (p_initial_point[0]**2 + p_initial_point[1]**2 + p_initial_point[2]**2 - r**2)

# solve the quadratic equation for t, there are two solutions, we take the positive one because we want the point in the direction from initial to final
discriminant = b**2 - 4*a*c
if discriminant < 0:
    print("No real solution for t, the line does not intersect the sphere.")    
t1 = (-b + np.sqrt(b**2 - 4*a*c)) / (2*a) # t solution 1
t2 = (-b - np.sqrt(b**2 - 4*a*c)) / (2*a) # t solution 2

# there are two points where the line intersects the sphere, we take the one that is in between initial and final points, which means the point closer to the final point is the one we want
p_intersection_1 = p_initial_point + t1 * v_initial_to_final
p_intersection_2 = p_initial_point + t2 * v_initial_to_final

if np.linalg.norm(p_intersection_1 - p_final_point) < np.linalg.norm(p_intersection_2 - p_final_point):
    p_intersection = p_intersection_1
elif np.linalg.norm(p_intersection_1 - p_final_point) > np.linalg.norm(p_intersection_2 - p_final_point):
    p_intersection = p_intersection_2
else: 
    print("Both intersection points are equidistant from the final point, which is unexpected.")
    p_intersection = p_intersection_1 # just take one of them







# theta and phi points for plotting the sphere
theta_points = np.linspace(-2*np.pi, 2*np.pi, 101)
phi_points = np.linspace(0, np.pi,101)


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

#%% creating plotting for sphere
theta_points_mesh, phi_points_mesh = np.meshgrid(theta_points, phi_points)

# points on the sphere
x_sphere = r * np.sin(phi_points_mesh) * np.cos(theta_points_mesh)
y_sphere = r * np.sin(phi_points_mesh) * np.sin(theta_points_mesh)
z_sphere = r * np.cos(phi_points_mesh)


# %% 
fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")

# plot sphere
# ax.plot_surface(x_sphere, y_sphere, z_sphere, alpha=0.3, color='orange', edgecolor='none')
ax.plot_surface(x_sphere, y_sphere, z_sphere, color="pink", alpha=0.2,edgecolor="black", linewidth=0.15, antialiased=True, shade=False)

# plot initial and final points
ax.scatter(p_initial_point[0], p_initial_point[1], p_initial_point[2], color='red', s=100, label='Initial Point')
ax.scatter(p_final_point[0], p_final_point[1], p_final_point[2], color='blue', s=100, label='Final Point')

# plot line between initial and final points
ax.plot( [p_initial_point[0], p_final_point[0]], [p_initial_point[1], p_final_point[1]], [p_initial_point[2], p_final_point[2]], color='black', label='Line between Points')  


# plot intersection points 
ax.scatter(p_intersection_1[0], p_intersection_1[1], p_intersection_1[2], color='magenta', s= 100, label='Intersection Point 1')
ax.scatter(p_intersection_2[0], p_intersection_2[1], p_intersection_2[2], color='green', s= 100, label='Intersection Point 2')
ax.scatter(p_intersection[0], p_intersection[1], p_intersection[2],  marker="o", facecolors='none', edgecolors='black', s= 300, label='Intersection Point real')




ax.grid()
ax.legend(frameon=False, loc="upper left", fontsize=8)

ax.set_title("3D Sphere with Initial and Final Points", fontsize=14)
ax.tick_params(axis="x", labelsize=14)
ax.tick_params(axis="y", labelsize=14)
ax.tick_params(axis="z", labelsize=14)
ax.set_xlabel("X", fontsize=14)
ax.set_ylabel("Y", fontsize=14)
ax.set_zlabel("Z", fontsize=14)


# axis_limit = 1.5 * r
# ax.set_xlim(-axis_limit, axis_limit)
# ax.set_ylim(-axis_limit, axis_limit)
# ax.set_zlim(-axis_limit, axis_limit)


# plt.tight_layout()  
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







