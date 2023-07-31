import sympy as sp
import math
import matplotlib.pyplot as plt
import numpy as np

r = 1
k_0 = -0
m_0 = 0.9
n = 1.33

x, y = sp.symbols('x y')
line_eq = sp.Eq(y, k_0 * x + m_0)
circle_eq = sp.Eq(x**2 + y**2, r**2)
intersections = sp.solve((line_eq, circle_eq), (x, y))

if not intersections:
    print("No first intersections found.")

q_0, w_0 = intersections[0]
print(f"First intersection Point: x = {q_0}, y = {w_0}")

tangent_slope = -q_0 / w_0
a_0 = -1 / tangent_slope
b_0 = 0
print(f"Normal: {a_0}")

first_input_angle = math.atan(a_0) - math.atan(k_0)
print(f"First input angle: {abs(math.degrees(first_input_angle))} degrees")

first_output_angle = math.asin(math.sin(abs(first_input_angle))/n)
print(f"First output angle: {math.degrees(first_output_angle)} degrees")

k_1 = math.tan(first_output_angle + math.atan(a_0) - math.pi)
m_1 = w_0 - k_1 * q_0
print(f"First line: {k_1} x + {m_1}")






line_eq = sp.Eq(y, k_1 * x + m_1)
intersections = sp.solve((line_eq, circle_eq), (x, y))

if not intersections:
    print("No first intersections found.")

q_1, w_1 = intersections[1]
print(f"Second itersection Point: x = {q_1}, y = {w_1}")

a_1 = -q_1 / w_1
b_1 = w_1 - a_1 * q_1
print(f"Tangent: {a_1} x + {b_1}")

ref_angle = math.pi - (math.pi + math.atan(k_1) - math.atan(a_1))
print(f"Reflection angle: {math.degrees(ref_angle)} degrees")
k_2 = math.tan(ref_angle + math.atan(a_1))
m_2 = w_1 - k_2 * q_1
print(f"Second line: {k_2} x + {m_2}")




line_eq = sp.Eq(y, k_2 * x + m_2)
intersections = sp.solve((line_eq, circle_eq), (x, y))

if not intersections:
    print("No first intersections found.")

q_2, w_2 = intersections[0]
print(f"First intersection Point: x = {q_2}, y = {w_2}")

tangent_slope = -q_2 / w_2
a_2 = -1 / tangent_slope
b_2 = 0
print(f"Normal: {a_2}")

first_input_angle = math.atan(a_2) - math.atan(k_2)
print(f"First input angle: {abs(math.degrees(first_input_angle))} degrees")

first_output_angle = math.asin(math.sin(abs(first_input_angle))*n)
print(f"First output angle: {math.degrees(first_output_angle)} degrees")

k_3 = math.tan(math.atan(a_2) - first_output_angle)
m_3 = w_2 - k_3 * q_2
print(f"First line: {k_3} x + {m_3}")



total_diff = math.atan(k_0) - math.atan(k_3)

print(abs(math.degrees(total_diff)))


points = 100
delta = 0.8
theta = np.linspace(0, 2*np.pi, points)
x_circle = np.cos(theta)
y_circle = np.sin(theta)
plt.plot(x_circle, y_circle, color='black')

x_line = np.linspace(float(q_0 - delta), float(q_0), 100)
y_line = [k_0 * x + m_0 for x in x_line]
plt.plot(x_line, y_line, color='red')

x_line = np.linspace(float(q_0), float(q_1), 100)
y_line = [k_1 * x + m_1 for x in x_line]
plt.plot(x_line, y_line, color='red')

x_line = np.linspace(float(q_2), float(q_1), 100)
y_line = [k_2 * x + m_2 for x in x_line]
plt.plot(x_line, y_line, color='red')

x_line = np.linspace(float(q_2 - delta), float(q_2), 100)
y_line = [k_3 * x + m_3 for x in x_line]
plt.plot(x_line, y_line, color='red')

fix = delta*math.cos(math.atan(a_0))
x_line = np.linspace(float(q_0 - fix), float(q_0 + fix), 100)
y_line = [a_0 * x + b_0 for x in x_line]
plt.plot(x_line, y_line, color='blue', linestyle='dotted')

fix = delta*math.cos(math.atan(a_1))
x_line = np.linspace(float(q_1 - fix), float(q_1 + fix), 100)
y_line = [a_1 * x + b_1 for x in x_line]
plt.plot(x_line, y_line, color='blue', linestyle='dotted')

fix = delta*math.cos(math.atan(a_2))
x_line = np.linspace(float(q_2 - fix), float(q_2 + fix), 100)
y_line = [a_2 * x + b_2 for x in x_line]
plt.plot(x_line, y_line, color='blue', linestyle='dotted')


plt.axis('equal')
plt.grid()
plt.show()

