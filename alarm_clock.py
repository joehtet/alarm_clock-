import webbrowser
import time
import random
import argparse


# opens a random link in web browser
def open_link(links):
    webbrowser.open(random.choice(links), new=0, autoraise=True)
       
# converts total time to seconds
def get_seconds(hours, minutes, seconds):
    time_in_seconds = hours*60*60 + minutes*60 + seconds
    print("Alarm set for {} hours, {} minutes, {} seconds".format(hours,minutes,seconds))
    return time_in_seconds

# sets timer
def set_alarm(time_in_seconds, links):
    time.sleep(time_in_seconds)
    open_link(links)

# start pomodoro timer
def pomodoro(links):
    print("Started pomodoro timer, alarm will ring in 25 minutes.")
    
    while True:
        time.sleep(25*60)
        print("Time to take a break.")
        open_link(links)

        time.sleep(5*60)
        print("Time to get back to work.")
        open_link(links)


# gets user inputted time from cmd line
parser = argparse.ArgumentParser(description='Set the alarm clock or start pomodoro timer.')

group = parser.add_mutually_exclusive_group()

group.add_argument('-p', '--pomodoro', action='store_true', default=False,
                    dest='pomodoro', help='start the pomodoro timer (25 minutes of work, 5 minutes break time)')
group.add_argument('-t', '--timer' , action='store_true', default=False, dest='timer', help='start the timer, use -hr HOUR -m MINUTES -s SECONDS')
parser.add_argument('-hr', '--hours', nargs='?', default=0, type=int)
parser.add_argument('-m', '--minutes', nargs='?', default=0, type=int)
parser.add_argument('-s', '--seconds', nargs='?', default=0, type=int)
args = parser.parse_args()


# gets list of youtube links from file
with open("alarm_songs.txt", "r") as f:
    links = f.readlines()

if args.pomodoro:
    pomodoro(links)
elif args.timer:
    set_alarm(get_seconds( args.hours, args.minutes, args.seconds), links)
else:
    print("Do nothing")
