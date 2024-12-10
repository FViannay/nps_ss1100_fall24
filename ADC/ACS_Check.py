mass_flow_rate = 0.06
exhaust_velocity = 2000
time = 10

def malfunction_detection(mass_flow_rate, exhaust_velocity):

    if mass_flow_rate > 0.05 or exhaust_velocity > 2000:
        print("A Thruster is out of tolerance!")

    if mass_flow_rate > 0.05:
        diff = mass_flow_rate - 0.05
        print(f"The mass flow rate is {diff:.2f}kg/s out of tolerance.")

    if exhaust_velocity > 2000:
        diff = exhaust_velocity - 2000
        print(f"The exhaust velocity is {diff}m/s out of tolerance.")

    elif mass_flow_rate <= 0.05 and exhaust_velocity <= 2000:
        print(f"The mass flow rate and exhaust velocity are within tolerance.")

print(malfunction_detection(mass_flow_rate, exhaust_velocity))

def velocity_change(mass_flow_rate, exhaust_velocity, time):
    thrust = mass_flow_rate * exhaust_velocity
    delta_v = (thrust *  time)/500
    return delta_v

print(f"The change is velocity is {velocity_change(mass_flow_rate, exhaust_velocity, time)}m/s")