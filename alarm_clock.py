import webbrowser
import time
import random
import argparse

# returns total time in seconds
def get_seconds(hours, minutes, seconds):
    time_in_seconds = hours*60*60 + minutes*60 + seconds
    print("Alarm set for {} hours, {} minutes, {} seconds".format(hours,minutes,seconds))
    return time_in_seconds

# sets the alarm
def set_alarm(time_in_seconds):
    time.sleep(time_in_seconds)
    
    # open a random link from links in web browser
    webbrowser.open(random.choice(links), new=0, autoraise=True)

# start pomodoro timer
def pomodoro():
    print("Started pomodoro timer, alarm will ring in 25 minutes.")
    
    while True:
        time.sleep(25*60)
        print("Time to take a break.")
        webbrowser.open(random.choice(links), new=0, autoraise=True)
        time.sleep(5*60)
        print("Time to get back to work.")
        webbrowser.open(random.choice(links), new=0, autoraise=True)

# gets user inputted time from cmd line
parser = argparse.ArgumentParser(description='Set the alarm clock or start pomodoro timer.')

parser.add_argument('-p', '--pomodoro', action='store_true', default=False,
                    dest='pomodoro')
parser.add_argument('-hr', '--hours', nargs='?', default=0, type=int)
parser.add_argument('-m', '--minutes', nargs='?', default=0, type=int)
parser.add_argument('-s', '--seconds', nargs='?', default=0, type=int)
args = parser.parse_args()

# gets list of youtube links from file
with open("alarm_songs.txt", "r") as f:
    links = f.readlines()

if args.pomodoro:
    pomodoro()
else:
    set_alarm(get_seconds( args.hours, args.minutes, args.seconds))


