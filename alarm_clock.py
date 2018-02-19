<<<<<<< HEAD
import random
import argparse
import pygame
import time

# play the alarm sound. reinitialize and quit mixer to stop CPU activity while idle
def play_sound():
    pygame.mixer.init()

    pygame.mixer.music.load("sound.wav")
    pygame.mixer.music.play()

    #pauses program so the sound can finish playing before pygame.mixer.quit() executes
    time.sleep(.4)

    pygame.mixer.quit()

# converts total time to seconds
def to_seconds(hours, minutes, seconds):
=======
import webbrowser
import time
import random
import argparse


# opens a random link in web browser
def open_link(links):
    webbrowser.open(random.choice(links), new=0, autoraise=True)
       
# converts total time to seconds
def get_seconds(hours, minutes, seconds):
>>>>>>> 523206fe1a338b3023abcb94f7488bc9766870d1
    time_in_seconds = hours*60*60 + minutes*60 + seconds
    print("Alarm set for {} hours, {} minutes, {} seconds".format(hours,minutes,seconds))
    return time_in_seconds

<<<<<<< HEAD
# countdown timer
def set_alarm(time_in_seconds):

    time.sleep(time_in_seconds)
    play_sound()


# pomodoro timer
def pomodoro():
=======
# sets timer
def set_alarm(time_in_seconds, links):
    time.sleep(time_in_seconds)
    open_link(links)

# start pomodoro timer
def pomodoro(links):
>>>>>>> 523206fe1a338b3023abcb94f7488bc9766870d1
    print("Started pomodoro timer, alarm will ring in 25 minutes.")
    
    while True:
        time.sleep(25*60)
<<<<<<< HEAD
        print("Time to take a break. Alarm will ring in 5 minutes.")
        play_sound()

        time.sleep(5*60)
        print("Time to get back to work for 25 minutes.")
        play_sound()


# cmd line functionality
=======
        print("Time to take a break.")
        open_link(links)

        time.sleep(5*60)
        print("Time to get back to work.")
        open_link(links)


# gets user inputted time from cmd line
>>>>>>> 523206fe1a338b3023abcb94f7488bc9766870d1
parser = argparse.ArgumentParser(description='Set the alarm clock or start pomodoro timer.')

group = parser.add_mutually_exclusive_group()

group.add_argument('-p', '--pomodoro', action='store_true', default=False,
                    dest='pomodoro', help='start the pomodoro timer (25 minutes of work, 5 minutes break time)')
group.add_argument('-t', '--timer' , action='store_true', default=False, dest='timer', help='start the timer, use -hr HOUR -m MINUTES -s SECONDS')
parser.add_argument('-hr', '--hours', nargs='?', default=0, type=int)
parser.add_argument('-m', '--minutes', nargs='?', default=0, type=int)
parser.add_argument('-s', '--seconds', nargs='?', default=0, type=int)
args = parser.parse_args()

<<<<<<< HEAD
if args.pomodoro:
    pomodoro()
elif args.timer:
    set_alarm(to_seconds( args.hours, args.minutes, args.seconds))
    print("Alarm rang. Exiting now.")
else:
    print("No inputs, please choose -t or -p")
=======

# gets list of youtube links from file
with open("alarm_songs.txt", "r") as f:
    links = f.readlines()

if args.pomodoro:
    pomodoro(links)
elif args.timer:
    set_alarm(get_seconds( args.hours, args.minutes, args.seconds), links)
else:
    print("Do nothing")
>>>>>>> 523206fe1a338b3023abcb94f7488bc9766870d1
