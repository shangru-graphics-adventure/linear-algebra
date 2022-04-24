import numpy as np
import quaternion
import math
np.set_printoptions(suppress=True)

def from_axis_angle(axis, angle):
    s = math.sin(angle / 2)
    return np.quaternion(math.cos(angle / 2), axis[0] * s, axis[1] * s, axis[2] * s)

def get_normalized(vec3):
    return vec3 / np.linalg.norm(vec3)

def mat4_from_axis_non_normalized_angle_degrees(_axis, _angle):
    axis = get_normalized(np.array(_axis))
    angle = math.radians(_angle)
    quat = from_axis_angle(axis, angle)
    mat3 = quaternion.as_rotation_matrix(quat)
    mat4 = np.identity(4)
    mat4[0:3, 0:3] = mat3
    return mat4

def apply_axis_non_normalized_angle_degrees_to_vec4(_axis, _angle, _vec4):
    mat4 = mat4_from_axis_non_normalized_angle_degrees(_axis, _angle)
    vec4 = np.array(_vec4)
    vec4_rotated = mat4.dot(vec4)
    return vec4_rotated
v = apply_axis_non_normalized_angle_degrees_to_vec4([1, 1, 1], 120, [0, 1, 0, 1])
print(v)