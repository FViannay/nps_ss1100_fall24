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

# Thrusters Orientations
thrusters = {
    1: 'X-axis (Forward )',
    2: 'Y-axis (Lateral)',
    3: 'Z-axis (Vertical)'}

print('\n#############################\n')

# Malfunction Detection. Return the malfunction check result
    # False = No Malfunction
    # True = Malfunction Detected
    
def check_thrust(thruster_num, flow_rate,effective_exaust_velocity):
    fr_diff = flow_rate - flow_rate_limit
    eev_diff = effective_exaust_velocity - exhaust_velocity_limit
    malfunction = False
    if fr_diff > 0:
        print(f"WARNING on Thruster {thruster_num}: Flow Rate limit exceeded by {fr_diff: .2f}")
        malfunction = True
    if eev_diff > 0:
        print(f"WARNING on Thruster {thruster_num}: Effective Exaust Velocity limit exceeded by {eev_diff: .2f}")
        malfunction = True
    return malfunction

# Velocity Change Calculation
def velocity_change(mass_flow_rate,effective_exaust_velocity,time_ellapsed):
    deltav=[0,0,0]
    print("Maneuver result:")
    for thr, eef,time,mfr in zip(thrusters,effective_exaust_velocity,time_ellapsed,mass_flow_rate):
        check_thrust(thr, mfr, eef)  # assuming the malfunction is detected after the maneuver
        deltav[thr-1] = (eef*mfr*time)/spacecraft_mass
        print(f"Delta V on {thrusters[thr]} = {deltav[thr-1]} m/s.")
    print('\n#############################\n')
    return deltav

# 1. Firing a thruster for 5 seconds, with ˙m = 0.02 and v e = 1000
# 2. Firing a thruster for 3 seconds, with ˙m = 0.06 and v e = 1000
# 3. Firing a thruster for 10 seconds, with ˙m = 0.05 and v e = 2000

time_ellapsed = [5,3,10]
mass_flow_rate = [0.02,0.06,0.05]
effective_exaust_velocity = [1000,1000,2000]
velocity_change(mass_flow_rate, effective_exaust_velocity, time_ellapsed)

# Firing Thruster 1 for 15 seconds, with ˙m = 0.04 and v e = 2000
# Firing Thruster 2 for 4 seconds, with ˙m = 0.03 and v e = 2000
# Firing Thruster 3 for 3 seconds, with ˙m = 0.01 and v e = 2000

time_ellapsed = [15,4,3]
mass_flow_rate = [0.04,0.03,0.01]
effective_exaust_velocity = [2000,2000,2000]
velocity_change(mass_flow_rate, effective_exaust_velocity, time_ellapsed)

# Firing Thruster 1 for 15 seconds, with ˙m = 0.04 and v e = 2000
# Firing Thruster 2 for 4 seconds, with ˙m = 0.06 and v e = 2000
# Firing Thruster 3 for 3 seconds, with ˙m = 0.01 and v e = 2020

time_ellapsed = [15,4,3]
mass_flow_rate = [0.04,0.06,0.01]
effective_exaust_velocity = [2000,2000,2020]
velocity_change(mass_flow_rate, effective_exaust_velocity, time_ellapsed)


# calling only the check_thrust function
check_thrust(1, 0.02, 1000)
check_thrust(2, 0.06, 1000)
check_thrust(3, 0.05, 2000)

