# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 19:18:48 2024

Propulsion / Reaction Control Subsystem (RCS)

"""
# Spacecraft mass
spacecraft_mass = 500

# RCS Limits
thrust_limit = 100 # Neutons
flow_rate_limit = 0.05 #kg
exhaust_velocity_limit = 2000 #m/s

# Thruster Orientations
# Th1 = Forward (x-axis)
# Th2 = Lateral (y-axis)
# Th3 = Vertical (z-axis)

def check_thrust(thruster, flow_rate,effective_exaust_velocity):
    fr_diff = flow_rate - flow_rate_limit
    eev_diff = effective_exaust_velocity - exhaust_velocity_limit
    if fr_diff > 0:
        print(f"ALERT {thruster}: Flow Rate limit exceeded by {fr_diff: .2f}")
    if eev_diff > 0:
        print(f"ALERT {thruster}: Effective Exaust Velocity limit exceeded by {eev_diff: .2f}")
    return

def velocity_change(mass_flow_rate,effective_exaust_velocity,time_ellapsed):
    thrust = mass_flow_rate * effective_exaust_velocity
    deltav = (thrust * time_ellapsed)/spacecraft_mass
    print(f"DeltaV = {deltav} m/s")
    return deltav

check_thrust("thruster1", 0.02, 1000)
check_thrust("thruster2", 0.06, 1000)
check_thrust("thruster3", 0.05, 2020)

velocity_change(0.02, 1000, 5)
velocity_change(0.06, 1000, 3)
velocity_change(0.05, 2000, 10)