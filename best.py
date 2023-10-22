import sympy as sp
import math
import matplotlib.pyplot as plt
import numpy as np

def refraction(k_in, m_in, first, q_old, w_old, refraction_index):
    x, y = sp.symbols('x y')
    line_eq = sp.Eq(y, k_in * x + m_in)
    circle_eq = sp.Eq(x**2 + y**2, CIRCLE_RADIUS**2)
    intersections = sp.solve((line_eq, circle_eq), (x, y))

    if not intersections:
        exit

    if first:
        q, w = intersections[0]
    elif round(intersections[0][0], 5) == round(q_old, 5) and round(intersections[0][1], 5) == round(w_old, 5):
        q, w = intersections[1]
    else:
        q, w = intersections[0]
        
    k_normal = w / q
    k_tan = -q / w

    angle_in = math.atan(k_in) - math.atan(k_tan)
    angle_out_sug1 = math.atan(k_normal) + math.asin(math.sin(abs(math.atan(k_normal) - math.atan(k_in)))*refraction_index) - math.atan(k_tan)
    angle_out_sug2 = math.atan(k_normal) - math.asin(math.sin(abs(math.atan(k_normal) - math.atan(k_in)))*refraction_index) - math.atan(k_tan)

    if angle_in < 0:
        angle_in += math.pi
    if angle_out_sug1 < 0:
        angle_out_sug1 += math.pi
    if angle_out_sug2 < 0:
        angle_out_sug2 += math.pi

    angle_in -= math.pi/2
    angle_out_sug1 -= math.pi/2
    angle_out_sug2 -= math.pi/2

    if np.sign(angle_in) == np.sign(angle_out_sug1):
        sign = 1
    else:
        sign = -1
    
    k_out = math.tan(math.atan(k_normal) + sign * math.asin(math.sin(abs(math.atan(k_normal) - math.atan(k_in)))*refraction_index))
    print(angle_in)
    print(angle_out_sug1)
    print(angle_out_sug2)

    m_out = w - k_out * q


    x_line = np.linspace(float(q_old), float(q), 100)
    y_line = [k_in * x + m_in for x in x_line]
    plt.plot(x_line, y_line, color='red')

    fix = DELTA*math.cos(math.atan(k_normal))
    x_line = np.linspace(float(q - fix), float(q + fix), 100)
    y_line = [k_normal * x for x in x_line]
    plt.plot(x_line, y_line, color='blue', linestyle='dotted')

    return k_out, m_out, q, w

# consts
CIRCLE_RADIUS = 1.2
INPUT_SLOPE = 0
INPUT_HEIGHT = 0.7
REFRACTION_INDEX = 1.9
POINTS = 100
DELTA = 0.8
INPUT_START = -1.8 * CIRCLE_RADIUS

# plot circle
theta = np.linspace(0, 2*np.pi, POINTS)
x_circle = CIRCLE_RADIUS*np.cos(theta)
y_circle = CIRCLE_RADIUS*np.sin(theta)
plt.plot(x_circle, y_circle, color='black')



k_1, m_1, q_0, w_0 = refraction(INPUT_SLOPE, INPUT_HEIGHT, True, INPUT_START, 0, 1/REFRACTION_INDEX)




x, y = sp.symbols('x y')
circle_eq = sp.Eq(x**2 + y**2, CIRCLE_RADIUS**2)
line_eq = sp.Eq(y, k_1 * x + m_1)
intersections = sp.solve((line_eq, circle_eq), (x, y))

if not intersections:
    exit



if round(intersections[0][0], 5) == round(q_0, 5) and round(intersections[0][1], 5) == round(w_0, 5):
    q_1, w_1 = intersections[1]
else:
    q_1, w_1 = intersections[0]
    

a_1 = -q_1 / w_1
b_1 = w_1 - a_1 * q_1

k_2 = math.tan(2*(math.pi + math.atan(a_1)) - math.atan(k_1) - math.pi)
m_2 = w_1 - k_2 * q_1





k_3, m_3, q_2, w_2 = refraction(k_2, m_2, False, q_1, w_1, REFRACTION_INDEX)



total_diff = math.atan(INPUT_SLOPE) - math.atan(k_3)

print(abs(math.degrees(total_diff)))




x_line = np.linspace(float(q_0), float(q_1), 100)
y_line = [k_1 * x + m_1 for x in x_line]
plt.plot(x_line, y_line, color='red')

fix = 2*DELTA*math.cos(math.atan(k_3))

if math.tan(k_3) > 0:
    x_line = np.linspace(float(q_2), float(q_2 + fix), 100)
else:
    x_line = np.linspace(float(q_2 + fix), float(q_2), 100)

y_line = [k_3 * x + m_3 for x in x_line]
plt.plot(x_line, y_line, color='red')

fix = DELTA*math.cos(math.atan(a_1))
x_line = np.linspace(float(q_1 - fix), float(q_1 + fix), 100)
y_line = [a_1 * x + b_1 for x in x_line]
plt.plot(x_line, y_line, color='green', linestyle='dotted')

plt.axis('equal')
plt.grid()
plt.show()

