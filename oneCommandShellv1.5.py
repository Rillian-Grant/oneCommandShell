#!/usr/bin/env python3


# OneCommandShell
import os
import sys


# Puts the arguments into a string or if no arguments asks the user for some
if (len(sys.argv) > 1):
    command = sys.argv[1]
    for item in range(2,len(sys.argv)):
        command = command + " " + sys.argv[item]
else:
    command = input ("Enter the command: ")

    
# The main loop
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
