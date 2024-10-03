import matplotlib.pyplot as plt
import numpy as np

a = int(input("Enter semi-major axis: "))
b = int(input("Enter semi-minor axis: "))
theta = np.linspace(0,2*np.pi,1000)
x = a*np.cos(theta)
y = b*np.sin(theta)
c = np.sqrt(a**2-b**2)
plt.plot(x,y)
plt.scatter([-c,c] , [0,0], color='red', label='Foci',zorder=5)
plt.text(c, 0 , 'F1', fontsize=12, ha='right')
plt.text(-c, 0 , 'F2', fontsize=12, ha='right')
plt.gca().set_aspect('equal', adjustable='box')
plt.axhline(0 ,color='black',linewidth = 0.5)
plt.axvline(0 ,color='black',linewidth = 0.5)
plt.show()