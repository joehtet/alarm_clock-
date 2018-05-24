import os

# install dependencies
os.system(r'pip3 install pygame') 

# copy pomodoro shell script to ~/bin
# TODO: For windows as well

# Write the shell script
file = open("pomodoro", 'w')

path = os.path.join( os.getcwd(), "pomodoro.py")
command = "python3 " + path
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

