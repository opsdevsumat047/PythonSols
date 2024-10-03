import matplotlib.pyplot as plt
import numpy as np
# func  = input("Enter a function: ")
radius = float(input("Enter radius: "))
h = float(input("Enter x-coordinate of the Circle: "))
k = float(input("Enter y-coordinate of the Circle: "))
theta  = np.linspace(0, 2*np.pi, 400)
x = radius * np.cos(theta) + h
y = radius * np.sin(theta) + k
# z = eval(func)
plt.plot(x, y)
plt.title(f'Plot of f(x,y) = {func}')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.show()


