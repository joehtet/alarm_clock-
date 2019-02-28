import subprocess as sp
import sys
from getpass import getuser
from exception import AdminStateUnknownError
import ctypes
import os

print("Installing pomodoro timer...")

# get permissions
def get_permissions():
    yes = ['Y', 'y', 'yes']
    no = ['N', 'n', 'no']
    while True:
        user_input = input("Administrator rights required to install dependencies. Continue? Y/N ")
        if user_input in yes or no:
            break
        else:
            print("Please enter Y or N")

    if user_input in no:
        print("Okay. Exiting...")
        sys.exit()

    return True

def is_user_admin():
    # type: () -> bool
    """Return True if user has admin privileges.

    Raises:
        AdminStateUnknownError if user privileges cannot be determined.
    """
    try:
        return os.getuid() == 0
    except AttributeError:
        pass
    try:
        return ctypes.windll.shell32.IsUserAnAdmin() == 1
    except AttributeError:
        raise AdminStateUnknownError


# install dependencies
PIP_VERSION = "pip3" if sys.version[0]==3 else "pip"
PLATFORM = sys.platform
print("Installing dependencies...")

if "linux" in PLATFORM:
    if get_permissions():
        try:
            sp.Popen(["sudo", PIP_VERSION, "install", "virtualenv", ])
        except sp.CalledProcessError:
            print("Please try again.")
            exit
if "win" in PLATFORM or "cygwin" in PLATFORM:
    if not is_user_admin():
        print("Error. Please run the script as Administrator")
    else:
        print("Installing Virtualenv")
        sp.call([PIP_VERSION, "install", "virtualenv", ])
else:
    print("Sorry. OS not supported")


# TODO: setup virtual env and install pygame

# copy pomodoro shell script to ~/bin

# Write the shell script
# file = open("pomodoro", 'w')

# path = os.path.join( os.getcwd(), "pomodoro.py")
# command = "python3 " + path
# file.write("#!/bin/bash\n\n")
# file.write(command)

# file.close()

# os.chmod("pomodoro", 0o755) #leading 0 for linux systems


# # Move the script to bin
# try: 
#     print("Installing pomodoro timer...")
#     os.system(r'mv pomodoro ~/bin/pomodoro')
#     print("Success!")

# except: 
#     print("Error!")

