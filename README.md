# physics-variable-gravity-free-fall-simulation
# Variable Gravity Simulation

This project simulates the free fall of a satellite towards Earth, taking into account the variation of gravitational acceleration with altitude.

## Description

Unlike simple free fall simulations that use a constant gravity value (9.81 m/s²), this simulation updates gravity at each time step based on the satellite's current altitude.  
It uses basic physics equations and numerical integration to compute position, velocity, and acceleration over time.

## Features

- Calculates gravitational acceleration, where 'r'  is the distance from Earth's center.
- Updates velocity and position iteratively using a small time step.
- Stops simulation when the satellite reaches Earth's surface.
- Plots graphs for altitude, velocity, and acceleration vs time using matplotlib.

## How to use

1. Run the Python script.
2. Input the initial height of the satellite above Earth's surface (in meters).
3. The program will simulate the fall and display three plots:
   - Altitude vs Time
   - Velocity vs Time
   - Acceleration vs Time

## Requirements

- Python 3.x
- numpy
- matplotlib

