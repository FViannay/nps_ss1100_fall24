current_temp = float(10)
desired_temp = float(5)

def temp_control(current_temp, desired_temp):
    temp_diff = desired_temp - current_temp
    temp_change = current_temp - (temp_diff * 0.25)
    new_temp = current_temp + temp_change
    print(f"The TCS is changing the temperature by {temp_change} and the current temperature is {new_temp}")
    return new_temp

print(temp_control(current_temp, desired_temp))