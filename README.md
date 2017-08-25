# oneCommandShell
A command shell written in Python that prefixes all commands with one you set.


## Use case
If you use docker a lot you will no doubt get sick of typing docker at the start of every command. oneCommandShell Will prompt you for a command at startup which will prefix all commands entered thereafter with it unless they start with a backslash.


## How to use

Download the oneCommandShell.py file and make it executable with:

> chmod u+x oneCommandShell.py

Now you can run the file. It takes one argument: oneCommandShell.py \[command prefix]
If you run it with no argument you will see a prompt looking like this:


> Enter command to use as prefix:


Now you will see a prompt like this:


> the-prefix-you-entered>


Now anything you enter will be prefixed by docker and a space.


## Platforms

Linux (Tested),
OSX and
Windows (You will need to install Python.)
