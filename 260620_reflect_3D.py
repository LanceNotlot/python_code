# %%
import os
import sys
import numpy as np
import matplotlib.pyplot as plt


os.system("cls")

#%%
#  circle and sphere radius  
r = 1

# initial and final points
# p_initial_point = np.array([0.5,-0.5,0.5])
# p_final_point   = np.array([1.5,0.5,0.5]) 

p_initial_point = np.array([2.0, 0.0, 0.0])
p_final_point   = np.array([0.0, 0.0, 0.0])
                           
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
    sys.exit() 
t1 = (-b + np.sqrt(b**2 - 4*a*c)) / (2*a) # t solution 1
t2 = (-b - np.sqrt(b**2 - 4*a*c)) / (2*a) # t solution 2

# there are two points where the line intersects the sphere, we take the one that is in between initial and final points, which means the point closer to the final point is the one we want
p_intersection_1 = p_initial_point + t1 * v_initial_to_final
p_intersection_2 = p_initial_point + t2 * v_initial_to_final

if   0 <= t1 and t1 <= 1:
    p_intersection = p_intersection_1
elif 0 <= t2 and t2 <= 1: 
    p_intersection = p_intersection_2
else: 
    print("The line intersects the sphere, but neither intersection is on the segment.")
    p_intersection = p_intersection_1 # just take one of them
    # sys.exit()

# if np.linalg.norm(p_intersection_1 - p_final_point) < np.linalg.norm(p_intersection_2 - p_final_point):
#     p_intersection = p_intersection_1
# elif np.linalg.norm(p_intersection_1 - p_final_point) > np.linalg.norm(p_intersection_2 - p_final_point):
#     p_intersection = p_intersection_2
# else: 
#     print("Both intersection points are equidistant from the final point, which is unexpected.")
#     p_intersection = p_intersection_1 # just take one of them
 

# find the equation of the plane tangent to the sphere at the intersection point, which is the plane that reflects the line from the initial point to the final point
# the normal vector of the tangent plane is the same as the normal vector of the sphere at the intersection point, which is the vector from the origin to the intersection point
p_origin = np.array([0,0,0])

plane_normal_vector = p_intersection - p_origin # normal vector of the plane is the same as the normal vector of the sphere at the intersection point

plane_normal_A  = plane_normal_vector[0]
plane_normal_B  = plane_normal_vector[1] 
plane_normal_C  = plane_normal_vector[2]

# plane_normal_D  = - (plane_normal_A * p_intersection[0] + plane_normal_B * p_intersection[1] + plane_normal_C * p_intersection[2]) # D = - (A*x0 + B*y0 + C*z0) where (x0, y0, z0) is the point on the plane, which is the intersection point
# plane_D_x = plane_normal_A * p_intersection[0]
# plane_D_y = plane_normal_B * p_intersection[1]
# plane_D_z = plane_normal_C * p_intersection[2]

# the equation of the plane is plane_normal_A * (x - x0) + plane_normal_B * (y - y0) + plane_normal_C * (z - z0) = 0
# # Standard form:
# A*x + B*y + C*z + D = 0
# where D = -(A*x_ip + B*y_ip + C*z_ip)
# or we can write it as plane_normal_A * (x - plane_D_x ) + plane_normal_B * (y - plane_D_y ) + plane_normal_C * (z - plane_D_z ) = 0

# Vector from the sphere center to the intersection point.
# This is also the normal direction of the tangent plane.
v_origin_to_ip = plane_normal_vector # the vector from the final point to the reflection

# find the distance from the v_origin_to_ip to the v_origin to get the reflection point, which is the point on the plane that is in the direction from the final point to the intersection point and has the same distance from the final point as the intersection point has from the origin

# find the mid point between final point and the reflected point using the shortest distance from line p_final_point to p_reflection
# line goes through p_final_point with vector with vector v_origin_to_ip - p_intersection to find t
t_mid = (
      plane_normal_vector[0] * (p_intersection[0] - p_final_point[0])
    + plane_normal_vector[1] * (p_intersection[1] - p_final_point[1])
    + plane_normal_vector[2] * (p_intersection[2] - p_final_point[2])
) / (
      plane_normal_vector[0]**2
    + plane_normal_vector[1]**2
    + plane_normal_vector[2]**2
)

p_midpoint = p_final_point + t_mid * v_origin_to_ip

# p_reflect is exactly in the middle, that (p_final_point + p_reflect)/2
p_reflect_point = 2*p_midpoint - p_final_point



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
ax.scatter(p_intersection_1[0], p_intersection_1[1], p_intersection_1[2], color='green', s= 100, label='Intersection Point 1')
ax.scatter(p_intersection_2[0], p_intersection_2[1], p_intersection_2[2], color='green', s= 100, label='Intersection Point 2')
ax.scatter(p_intersection[0], p_intersection[1], p_intersection[2],  marker="o", facecolors='none', edgecolors='black', s= 300, label='Intersection Point real')

# plot the origin point
ax.scatter(p_origin[0], p_origin[1], p_origin[2], color='black', s=100, label='Origin Point')

# plot the line from origin to the intersection point
ax.plot( [p_origin[0], p_intersection[0]], [p_origin[1], p_intersection[1]], [p_origin[2], p_intersection[2]], color='black', label='line from origin to intersection')
ax.plot( [p_origin[0], 2.*p_intersection[0]], [p_origin[1], 2.*p_intersection[1]], [p_origin[2], 2.*p_intersection[2]], color='black', label='Line from Origin to Intersection') # make this line longer to show the normal vector of the plane

# plot the plane perpendicular to the vector from the intersection point to the origin at the intersection point, which is the plane that reflects the line from the initial point to the final point

# plot the line final point have the same vector as origin to intersection 
t_line = np.linspace(-2, 2, 100)

line_final_to_reflect = (p_final_point[None, :] + t_line[:, None] * v_origin_to_ip[None, :])

ax.plot( 
    line_final_to_reflect[:, 0],
    line_final_to_reflect[:, 1],
    line_final_to_reflect[:, 2],
    color="blue",
    linestyle="--",
    linewidth=2,
    label="Normal line through final point"
)

# plot the mid point
ax.scatter(p_midpoint[0], p_midpoint[1], p_midpoint[2], color='magenta', s=100, label='mid Point')

# plot the reflect point
ax.scatter(p_reflect_point[0], p_reflect_point[1], p_reflect_point[2], color='cyan', s=100, label='mid Point')



ax.grid()
# ax.legend(frameon=False, loc="upper left", fontsize=8)

ax.set_title("3D Sphere with Initial and Final Points", fontsize=14)
ax.tick_params(axis="x", labelsize=14)
ax.tick_params(axis="y", labelsize=14)
ax.tick_params(axis="z", labelsize=14)
ax.set_xlabel("X", fontsize=14)
ax.set_ylabel("Y", fontsize=14)
ax.set_zlabel("Z", fontsize=14)

plt.show()
print(distance)


