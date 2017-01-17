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
    # gets list of youtube links from file
    with open("alarm_songs.txt", "r") as f:
        links = f.readlines()

    time.sleep(time_in_seconds)
    
    # open a random link from links in web browser
    webbrowser.open(random.choice(links), new=0, autoraise=True)


# gets user inputted time from cmd line
parser = argparse.ArgumentParser(description='Set the alarm clock.')
parser.add_argument('-hr', '--hours', nargs='?', default=0, type=int)
parser.add_argument('-m', '--minutes', nargs='?', default=0, type=int)
parser.add_argument('-s', '--seconds', nargs='?', default=0, type=int)
args = parser.parse_args()


set_alarm(get_seconds( args.hours, args.minutes, args.seconds))


