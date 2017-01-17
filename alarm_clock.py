import webbrowser
import time
import random
import argparse


def get_time(hours, minutes, seconds):
    time_in_seconds = hours*60*60 + minutes*60 + seconds
    print("Alarm set for {} hours, {} minutes, {} seconds".format(hours,minutes,seconds))
    return time_in_seconds

# sets the alarm
def set_alarm(time_in_seconds):
    time.sleep(time_in_seconds)
    
    # creates a list of youtube links from file
    with open("alarm_songs.txt", "r") as f:
        links = f.readlines()
    
    # open a random link from links in web browser
    webbrowser.open(random.choice(links), new=0, autoraise=True)


# gets input for alarm from cmd line
parser = argparse.ArgumentParser(description='Set the alarm clock.')
parser.add_argument('-hr', '--hours', nargs='?', const=0, default=0, type=int)
parser.add_argument('-m', '--minutes', nargs='?', const=0, default=0, type=int)
parser.add_argument('-s', '--seconds', nargs='?', const=0, default=0, type=int)
args = parser.parse_args()

set_alarm(get_time( args.hours, args.minutes, args.seconds))


