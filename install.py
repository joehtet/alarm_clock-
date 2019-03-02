import os
import sys
import ctypes
import subprocess as sp
from getpass import getuser
from exception import AdminStateUnknownError

print("Installing pomodoro timer...")

# get permissions
def get_permissions():
    """Return True if user gave permission to install dependencies
    """
    yes = ['Y', 'y', 'yes', 'YES', 'Yes']
    no = ['N', 'n', 'no', 'NO', 'No']
    while True:
        # Fix Python 2.x.
        try: input = raw_input
        except NameError: pass

        user_input = input("Administrator rights required to install dependencies. Continue? Y/N ")
        if user_input in yes or no:
            break
        else:
            print("Please enter Y or N")

    if user_input in no:
        return False
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
PIP = "pip3" if sys.version[0]==3 else "pip"
PYTHON = "python3" if sys.version[0]==3 else "python"
PLATFORM = sys.platform

print("Installing dependencies...")

if "linux" in PLATFORM:
    if get_permissions():
        try:
            sp.check_call(["sudo", PIP, "install", "pygame", ])
        except sp.CalledProcessError:
            print("Please try again.")
            sys.exit()
    else:
        print("Okay. Exiting...")
        sys.exit()
elif "win" in PLATFORM or "cygwin" in PLATFORM:
    if not is_user_admin():
        print("Error. Please run the script as Administrator")
        sys.exit()
    else:
        sp.call([PIP, "install", "pygame", ])
        print('Success!')
else:
    print("Sorry. {} not supported".format(PLATFORM))
    sys.exit()


if "linux" in PLATFORM:
    # Write the shell script
    file = open("pomodoro", 'w')
    path = os.path.join( os.getcwd(), "pomodoro.py")
    command = PYTHON + " " + path + " $*"

    file.write("#!/bin/bash\n\n")
    file.write(command)
    file.close()

    os.chmod("pomodoro", 0o755) #leading 0 for linux systems

    # Move the script to bin
    try: 
        print("Installing pomodoro timer...")
        os.system(r'mv pomodoro ~/bin/pomodoro')
        print("Success!")

    except: 
        print("Error!")

else:
    # Write Batch file which enables "pomodoro" command to be called
    file = open("pomodoro.bat", 'w')
    path = os.path.join( os.getcwd(), "pomodoro.py")
    command = "start " + PYTHON + " {} %*".format(path)
    file.write(command)
    file.close()

    # Write Batch file to add this application's directory to PATH variable via Registry
    file = open("add_to_path.bat", 'w') 
    file.write(r"reg add HKEY_CURRENT_USER\Environment /v PATH /d \"%PATH%;{}\"".format(os.getcwd()))
    file.close()

    # Run the above batch file and delete it
    sp.call(["add_to_path.bat"])
    os.system("del /f /q add_to_path.bat")

    print("Done! Please restart your computer for the changes to take effect.")
   
