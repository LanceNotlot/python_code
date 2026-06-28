def reflection3D(r,p_initial, p_final):

    import numpy as np

    # Convert input points into NumPy arrays
    # p_initial = np.asarray(p_initial, dtype=float)
    # p_final   = np.asarray(p_final, dtype=float)

    # Vector from initial point to final point
    v_initial_to_final = p_final - p_initial

    # Find the intersection point with the sphere
    a = (
        v_initial_to_final[0]**2
        + v_initial_to_final[1]**2
        + v_initial_to_final[2]**2
    )

    b = 2 * (
        p_initial[0] * v_initial_to_final[0]
        + p_initial[1] * v_initial_to_final[1]
        + p_initial[2] * v_initial_to_final[2]
    )

    c = (
        p_initial[0]**2
        + p_initial[1]**2
        + p_initial[2]**2
        - r**2
    )

    discriminant = b**2 - 4*a*c

    if discriminant < 0:
        raise ValueError(
            "No real solution for t. The line does not intersect the sphere."
        )

    t1 = (-b + np.sqrt(discriminant)) / (2*a)
    t2 = (-b - np.sqrt(discriminant)) / (2*a)

    # Find intersection points
    p_intersection_1 = p_initial + t1 * v_initial_to_final
    p_intersection_2 = p_initial + t2 * v_initial_to_final

    # Choose the intersection located on the line segment
    if 0 <= t1 <= 1:
        p_intersection = p_intersection_1

    elif 0 <= t2 <= 1:
        p_intersection = p_intersection_2

    else:
        raise ValueError(
            "The line intersects the sphere, but neither intersection "
            "is between p_initial and p_final."
        )

    # Normal vector at the sphere surface
    p_origin = np.array([0.0, 0.0, 0.0])

    v_origin_to_ip = p_intersection - p_origin

    # Convert normal vector to a unit vector
    v_origin_to_ip_unit_vector = (
        v_origin_to_ip
        / np.linalg.norm(v_origin_to_ip)
    )

    # Vector from intersection point to final point
    v_ip_to_final = p_final - p_intersection

    # Signed perpendicular distance
    distance_mid_to_final = np.dot(
        v_ip_to_final,
        v_origin_to_ip_unit_vector
    )

    # Projection of final point onto the tangent plane and find the mid point
    p_mid = (
        p_final
        - distance_mid_to_final * v_origin_to_ip_unit_vector
    )

    # Reflected point
    p_reflect = (
        p_final
        - 2 * distance_mid_to_final * v_origin_to_ip_unit_vector
    )

    return p_reflect