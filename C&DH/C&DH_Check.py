system_dict = {
    "RCS" : "Reaction Control Subsystem",
    "TCS" : "Thermal Control Subsystem",
    "ACS" : "Attitude Control Subsystem",
    "CHD" : "Command & Data Handling",
    "TTC" : "Telemetry, Tracking, & Command",
    "EPS" : "Electrical Power Subsystem",
    "PL1" : "Payload System 1",
    "PL2" : "Payload System 2"
}
command_dict = {
    'CMD01' : {
        'RCS' : "THRUST_X",
        'TCS' : "HEATER_ON",
        'ACS' : "ROTATE_X",
        'CHD' : "TRANSMIT_HIGH",
        'TTC' : "TRANSMIT_MODE",
        'EPS' : "BATTERY_CHARGE_MODE",
        'PL1' : "START_DATA_ACQUISITION",
        'PL2' : "START_DATA_ACQUISITION"
    },
    'CMD02' : {
        'RCS' : "THRUST_Y",
        'TCS' : "HEATER_OFF",
        'ACS' : "ROTATE_Z",
        'CHD' : "TRANSMIT_LOW",
        'TTC' : "RECEIVE_MODE",
        'EPS' : "POWER_ON_MODULE",
        'PL1' : "STOP_DATA_ACQUISITION",
        'PL2' : "STOP_DATA_ACQUISITION"
    },
    'CMD03' : {
        'RCS' : "THRUST_Z",
        'TCS' : "VENT_OPEN_RADIATOR",
        'ACS' : "ROTATE_Z",
        'CHD' : "RECEIVE_MODE",
        'TTC' : "TRACKING_MODE",
        'EPS' : "POWER_OFF_MODULE",
        'PL1' : "CALIBRATE_SENSOR",
        'PL2' : "CALIBRATE_SENSOR"
    },
    'CMD04' : {
        'RCS' : "SAFE_MODE",
        'TCS' : "TEMP_SETPOINT",
        'ACS' : "SAFE_MODE",
        'CHD' : "SAFE_MODE",
        'TTC' : "SAFE_MODE",
        'EPS' : "VOLTAGE_SETPOINT",
        'PL1' : "SAFE_MODE",
        'PL2' : "SAFE_MODE"
    }
}

input_string = "EPS:CMD04:30"
parts = input_string.split(":")

try:
    subsystem = parts[0]
    command = parts[1]
    param = int(parts[2])
    system_dict[parts[0]]
    if subsystem == "RCS":
        if command == "CMD01":
            print(f"System: {system_dict[subsystem]}")
            print(f"Command: {command} - {command_dict[command][subsystem]}")
            print(f"Thrust on X axis {param}")
        if command == "CMD02":
            print(f"System: {system_dict[subsystem]}")
            print(f"Command: {command} - {command_dict[command][subsystem]}")
            print(f"Thrust on Y axis {param}")
        if command == "CMD03":
            print(f"System: {system_dict[subsystem]}")
            print(f"Command: {command} - {command_dict[command][subsystem]}")
            print(f"Thrust on Z axis {param}")
        if command == "CMD04":
            print(f"System: {system_dict[subsystem]}")
            print(f"Command: {command} - {command_dict[command][subsystem]}")
            print(f"Set thruster to safe")

    if subsystem == "TCS":
        if command == "CMD01":
            print(f"System: {system_dict[subsystem]}")
            print(f"Command: {command} - {command_dict[command][subsystem]}")
            print(f"Turn Heater on")
        if command == "CMD02":
            print(f"System: {system_dict[subsystem]}")
            print(f"Command: {command} - {command_dict[command][subsystem]}")
            print(f"Turn heater off")
        if command == "CMD03":
            print(f"System: {system_dict[subsystem]}")
            print(f"Command: {command} - {command_dict[command][subsystem]}")
            print(f"Open vent to radiator")
        if command == "CMD04":
            print(f"System: {system_dict[subsystem]}")
            print(f"Command: {command} - {command_dict[command][subsystem]}")
            print(f"Set Temperature to {param} C")

    if subsystem == "ACS":
        if command == "CMD01":
            print(f"System: {system_dict[subsystem]}")
            print(f"Command: {command} - {command_dict[command][subsystem]}")
            print(f"Rotate on X axis by {param} degrees")
        if command == "CMD02":
            print(f"System: {system_dict[subsystem]}")
            print(f"Command: {command} - {command_dict[command][subsystem]}")
            print(f"Rotate on Y axis by {param} degrees")
        if command == "CMD03":
            print(f"System: {system_dict[subsystem]}")
            print(f"Command: {command} - {command_dict[command][subsystem]}")
            print(f"Rotate on Z axis by {param} degrees")
        if command == "CMD04":
            print(f"System: {system_dict[subsystem]}")
            print(f"Command: {command} - {command_dict[command][subsystem]}")
            print(f"SAFE")

    if subsystem == "CHD":
        if command == "CMD01":
            print(f"System: {system_dict[subsystem]}")
            print(f"Command: {command} - {command_dict[command][subsystem]}")
            print(f"TRANSMITTING HIGH DATA RATE")
        if command == "CMD02":
            print(f"System: {system_dict[subsystem]}")
            print(f"Command: {command} - {command_dict[command][subsystem]}")
            print(f"TRANSMITTING LOW DATA RATE")
        if command == "CMD03":
            print(f"System: {system_dict[subsystem]}")
            print(f"Command: {command} - {command_dict[command][subsystem]}")
            print(f"RECEIVING")
        if command == "CMD04":
            print(f"System: {system_dict[subsystem]}")
            print(f"Command: {command} - {command_dict[command][subsystem]}")
            print(f"SAFE")

    if subsystem == "TTC":
        if command == "CMD01":
            print(f"System: {system_dict[subsystem]}")
            print(f"Command: {command} - {command_dict[command][subsystem]}")
            print(f"TRANSMITTING TTC")
        if command == "CMD02":
            print(f"System: {system_dict[subsystem]}")
            print(f"Command: {command} - {command_dict[command][subsystem]}")
            print(f"RECEIVING TTC")
        if command == "CMD03":
            print(f"System: {system_dict[subsystem]}")
            print(f"Command: {command} - {command_dict[command][subsystem]}")
            print(f"IN TRACKING MODE")
        if command == "CMD04":
            print(f"System: {system_dict[subsystem]}")
            print(f"Command: {command} - {command_dict[command][subsystem]}")
            print(f"SAFE")

    if subsystem == "EPS":
        if command == "CMD01":
            print(f"System: {system_dict[subsystem]}")
            print(f"Command: {command} - {command_dict[command][subsystem]}")
            print(f"BATTERY IS NOW CHARGING")
        if command == "CMD02":
            print(f"System: {system_dict[subsystem]}")
            print(f"Command: {command} - {command_dict[command][subsystem]}")
            print(f"MODULE IS POWERED ON")
        if command == "CMD03":
            print(f"System: {system_dict[subsystem]}")
            print(f"Command: {command} - {command_dict[command][subsystem]}")
            print(f"MODULE IS POWERED OFF")
        if command == "CMD04":
            print(f"System: {system_dict[subsystem]}")
            print(f"Command: {command} - {command_dict[command][subsystem]}")
            print(f"SET VOLTAGE TO {param}V")

    if subsystem == "PL1":
        if command == "CMD01":
            print(f"System: {system_dict[subsystem]}")
            print(f"Command: {command} - {command_dict[command][subsystem]}")
            print(f"STARTING DATA ACQUISITION")
        if command == "CMD02":
            print(f"System: {system_dict[subsystem]}")
            print(f"Command: {command} - {command_dict[command][subsystem]}")
            print(f"STOPPING DATA ACQUISITION")
        if command == "CMD03":
            print(f"System: {system_dict[subsystem]}")
            print(f"Command: {command} - {command_dict[command][subsystem]}")
            print(f"CALIBRATING SENSOR")
        if command == "CMD04":
            print(f"System: {system_dict[subsystem]}")
            print(f"Command: {command} - {command_dict[command][subsystem]}")
            print(f"SAFE")

    if subsystem == "PL2":
        if command == "CMD01":
            print(f"System: {system_dict[subsystem]}")
            print(f"Command: {command} - {command_dict[command][subsystem]}")
            print(f"STARTING DATA ACQUISITION")
        if command == "CMD02":
            print(f"System: {system_dict[subsystem]}")
            print(f"Command: {command} - {command_dict[command][subsystem]}")
            print(f"STOPPING DATA ACQUISITION")
        if command == "CMD03":
            print(f"System: {system_dict[subsystem]}")
            print(f"Command: {command} - {command_dict[command][subsystem]}")
            print(f"CALIBRATING SENSOR")
        if command == "CMD04":
            print(f"System: {system_dict[subsystem]}")
            print(f"Command: {command} - {command_dict[command][subsystem]}")
            print(f"SAFE")

except KeyError:
    print("Invalid subsystem entered.")
    
except ValueError:
    print("The parameter entered is not an integer.")


