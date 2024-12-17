# -*- coding: utf-8 -*-
"""
Created on Sat Dec 14 18:22:14 2024

@author: ffvia
"""

command_dict = {
    "Reaction Control Subsystem": {
        "Code": "RCS",
        "Commands": {"CMD01":['THRUST_X', range(0,60)],
                     "CMD02":['THRUST_Y', range(0,60)],
                     "CMD03":['THRUST_Z', range(0,60)],
                     "CMD04":['SAFE_MODE', {0, 1}]}
    },
    "Thermal Control Subsystem": {
        "Code": "TCS",
        "Commands": {"CMD01":['HEATER_ON', {0, 1}],
                     "CMD02":['HEATER_OFF', {0, 1}],
                     "CMD03":['VENT_OPEN_RADIATOR', {0, 1}],
                     "CMD04":['TEMP_SETPOINT', range(-30,60)]}
    },
    "Attitude Control Subsystem": {
        "Code": "ACS",
        "Commands": {"CMD01":['ROTATE_X', range(-360,360)],
                     "CMD02":['ROTATE_Y', range(-360,360)],
                     "CMD03":['ROTATE_Z', range(-360,360)],
                     "CMD04":['SAFE_MODE', {0, 1}]}
    },
    "Command & Data Handling": {
        "Code": "CDH",
        "Commands": {"CMD01":['TRANSMIT_HIGH', {0, 1}],
                     "CMD02":['TRANSMIT_LOW', {0, 1}],
                     "CMD03":['RECEIVE_MODE',{0, 1}],
                     "CMD04":['SAFE_MODE', {0,1}]}
    },
    "Telemetry, Tracking, & Command": {
        "Code": "TTC",
        "Commands": {"CMD01":['TRANSMIT_MODE', {0,1}],
                     "CMD02":['RECEIVE_MODE', {0,1}],
                     "CMD03":['TRACKING_MODE', {0,1}],
                     "CMD04":['SAFE_MODE', {0,1}]}
    },
    "Electrical Power Subsystem": {
        "Code": "EPS",
        "Commands": {"CMD01":['BATTERY_CHARGE_MODE', {0,1}],
                     "CMD02":['POWER_ON_MODULE', {0,1,2,3,4}],
                     "CMD03":['POWER_OFF_MODULE', {0,1,2,3,4}],
                     "CMD04":['VOLTAGE_SETPOINT', range(0,120)]}
    },
    "Payload System 1": {
        "Code": "PL1",
        "Commands": {"CMD01":['START_DATA_ACQUISITION', {0,1}],
                     "CMD02":['STOP_DATA_ACQUISITION', {0,1}],
                     "CMD03":['CALIBRATE_SENSOR', {0,1}],
                     "CMD04":['SAFE_MODE', {0,1}]}
    },
    "Payload System 2": {
        "Code": "PL2",
        "Commands": {"CMD01":['START_DATA_ACQUISITION', {0,1}],
                     "CMD02":['STOP_DATA_ACQUISITION', {0,1}],
                     "CMD03":['CALIBRATE_SENSOR', {0,1}],
                     "CMD04":['SAFE_MODE', {0,1}]}
    }
}


def cpr(command):
    parsed = command.rsplit(":") 
    #CHeck if command has three pieces
    if len(parsed) != 3:
        print(f"ERROR - Command is not in the correct format.")
        return
    error = [True,True] # True == ERROR. First for subsystem and second for command.
    # iterates over all dictionary
    for i in command_dict:
        # If the trigram correspond to an subsystem in the dictionary
        if command_dict[i]["Code"] == parsed[0]:
            error[0] = False # No error for the first piece
            # iterates over all commands for the subsystem
            for j in command_dict[i]["Commands"]:
                # If the command is equal to a command on the dictionary
                if j == parsed[1]:
                    error[1]= False # No error for the command
                    try:
                        parsed[2] = int(parsed[2]) #Cast argument to integer
                        #Verify if the argument received is in tolerance
                        if int(parsed[2]) in command_dict[i]["Commands"][j][1]:
                            #assembling the result (Subsystem, Command, Value)
                            result = (i,command_dict[i]["Commands"][j][0],parsed[2])
                            print(f"Commanding {result[0]}. {result[1]} = {result[2]}")
                            return result
                        else:
                            print(f"ERROR ({i}) - Value {parsed[2]} is not in the valid range for command {command_dict[i]['Commands'][j][0]}.")
                    except:
                        print(f"ERROR - {parsed[2]} is not a valid value")
            if error[1]:
                print(f"ERROR - Command {parsed[1]} is not valid.")    
    if error[0]:
        print(f"ERROR - Subsystem {parsed[0]} not found.")

        
    
print(cpr("EPS:CMD01:1"))
print(cpr("ACS:CMD04:-1"))
print(cpr("RCS:INVALID:0"))
print(cpr("TCS:CMD04:-20"))
