current_temp = 10
target_temp = 5
i=1
import time

def temp_control(current_temp, target_temp):
    temp_diff = target_temp - current_temp
    temp_change = temp_diff * 0.25
    print(f"Target Temperature is: {target_temp: .2f}.")
    print(f"Difference: {temp_diff: .2f}")
    new_temp = current_temp + temp_change
    print(f"Changing the temperature by {temp_change: .2f}.New temperature is {new_temp: .2f}")
    print("####################################\n")
    return new_temp


# This code will test the function temp_control
while round(current_temp,2) != round(target_temp,2):
    print(f"{i} iteration")
    print(f"New Temperature: {current_temp: .2f}.")
    current_temp = temp_control(current_temp, target_temp)
    time.sleep(0.5)
    i+=1
    
