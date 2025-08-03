import numpy as np
import matplotlib.pyplot as plt

#Constants
G = 6.67e-11 #m^3/kg/s^2
m_earth = 5.97e24 #Kg
r_earth = 6371e3 #m
t = 0
v = 0
dt = 0.01

#Lists
height = []
time = []
acceleration = []
velocity = []

#Calculations
h0 = float(input("\nHeight of the satelite from the Earth's surface (m): "))

h = r_earth + h0

while h > r_earth:
    g = (G * m_earth)/h ** 2
    v += -g * dt
    h += v * dt
    t += dt

    height.append(h - r_earth)
    time.append(t)
    acceleration.append(g)
    velocity.append(-v)
    
#Graphs

#Height
plt.plot(time, height)
plt.xlabel("Time (s)")
plt.ylabel("Altitude (m)")
plt.title("Free fall with variable gravity")
plt.grid(True)
plt.show()

#Acceleration
plt.plot(time, acceleration)
plt.xlabel("Time (s)")
plt.ylabel("Acceleration (m/s^2)")
plt.title("Free fall with variable gravity")
plt.grid(True)
plt.show()

#Velocity
plt.plot(time, velocity)
plt.xlabel("Time (s)")
plt.ylabel("Velocity (m/s)")
plt.title("Free fall with variable gravity")
plt.grid(True)
plt.show()