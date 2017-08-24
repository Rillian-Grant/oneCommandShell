#!/usr/bin/env python3

# OneCommandShell
import os
command = input ("Enter command to use as the : ")

while (1):
    entry = input (command + "> ")
    try:
        # If command starts with a backslash run it normally
        if (entry[0] == "\\"):
            os.system (entry[1:])
        else:
            os.system (command + " " + entry)
    except:
        # This is triggured when you press enter without entering anything
        os.system (command)
        
