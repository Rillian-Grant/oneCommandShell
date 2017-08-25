# oneCommandShell
A command shell written in Python that prefixes all commands with one you set.


## Use case
If you use docker a lot you will no doubt get sick of typing docker at the start of every command. oneCommandShell Will prompt you for a command at startup which will prefix all commands entered thereafter with it unless they start with a backslash.


## How to use

Download the oneCommandShell.py file, make it executable with: chmod u+x oneCommandShell.py and run it.
You will see a prompt looking like this:


> Enter command to use as prefix:


Enter your command, for example docker and you will see a prompt like this:


> docker>


Now anything you enter will be prefixed by docker and a space.


## Platforms

Linux (Tested),
OSX and
Windows (You will need to install Python.)
