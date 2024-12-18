# -*- coding: utf-8 -*-
"""
Created on Sat Dec 14 18:22:14 2024

"""
import command_dict as cd

command_dict = cd.command_dict


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
