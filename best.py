import sympy as sp
import math
import matplotlib.pyplot as plt
import numpy as np

CIRCLE_RADIUS = 1
INPUT_SLOPE = 0
INPUT_HEIGHT = 0.7
REFRACTION_INDEX = 0.9

k_0 = INPUT_SLOPE
m_0 = INPUT_HEIGHT

x, y = sp.symbols('x y')
line_eq = sp.Eq(y, k_0 * x + m_0)
circle_eq = sp.Eq(x**2 + y**2, CIRCLE_RADIUS**2)
intersections = sp.solve((line_eq, circle_eq), (x, y))
if not intersections:
    print("No first intersections found.")

q_0, w_0 = intersections[0]

tangent_slope = -q_0 / w_0
a_0 = w_0 / q_0
b_0 = 0
k_1 = math.tan(math.asin(math.sin(abs(math.atan(a_0) - math.atan(k_0)))/REFRACTION_INDEX) + math.atan(a_0) - math.pi)
m_1 = w_0 - k_1 * q_0





line_eq = sp.Eq(y, k_1 * x + m_1)
intersections = sp.solve((line_eq, circle_eq), (x, y))

if not intersections:
    print("No first intersections found.")

q_1, w_1 = intersections[1]

a_1 = -q_1 / w_1
b_1 = w_1 - a_1 * q_1

k_2 = math.tan(2*(math.pi + math.atan(a_1)) - math.atan(k_1) - math.pi)
m_2 = w_1 - k_2 * q_1
print(m_2)




line_eq = sp.Eq(y, k_2 * x + m_2)
intersections = sp.solve((line_eq, circle_eq), (x, y))
if not intersections:
    print("No first intersections found.")

q_2, w_2 = intersections[1]
a_2 = w_2 / q_2
b_2 = 0
k_3 = math.tan(math.atan(a_2) - math.asin(math.sin(abs(math.atan(a_2) - math.atan(k_2)))*REFRACTION_INDEX))
m_3 = w_2 - k_3 * q_2



total_diff = math.atan(k_0) - math.atan(k_3)

print(abs(math.degrees(total_diff)))


points = 100
delta = 0.8
theta = np.linspace(0, 2*np.pi, points)
x_circle = np.cos(theta)
y_circle = np.sin(theta)
plt.plot(x_circle, y_circle, color='black')

fix = 2*delta*math.cos(math.atan(k_0))
x_line = np.linspace(float(q_0 - fix), float(q_0), 100)
y_line = [k_0 * x + m_0 for x in x_line]
plt.plot(x_line, y_line, color='red')

x_line = np.linspace(float(q_0), float(q_1), 100)
y_line = [k_1 * x + m_1 for x in x_line]
plt.plot(x_line, y_line, color='red')

x_line = np.linspace(float(q_2), float(q_1), 100)
y_line = [k_2 * x + m_2 for x in x_line]
plt.plot(x_line, y_line, color='red')

fix = 2*delta*math.cos(math.atan(k_3))
x_line = np.linspace(float(q_2), float(q_2 + fix), 100)
y_line = [k_3 * x + m_3 for x in x_line]
plt.plot(x_line, y_line, color='red')

fix = delta*math.cos(math.atan(a_0))
x_line = np.linspace(float(q_0 - fix), float(q_0 + fix), 100)
y_line = [a_0 * x + b_0 for x in x_line]
plt.plot(x_line, y_line, color='blue', linestyle='dotted')

fix = delta*math.cos(math.atan(a_1))
x_line = np.linspace(float(q_1 - fix), float(q_1 + fix), 100)
y_line = [a_1 * x + b_1 for x in x_line]
plt.plot(x_line, y_line, color='green', linestyle='dotted')

fix = delta*math.cos(math.atan(a_2))
x_line = np.linspace(float(q_2 - fix), float(q_2 + fix), 100)
y_line = [a_2 * x + b_2 for x in x_line]
plt.plot(x_line, y_line, color='blue', linestyle='dotted')


plt.axis('equal')
plt.grid()
plt.show()

