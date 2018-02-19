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
    time.sleep(.7)

    pygame.mixer.quit()

# converts total time to seconds
def to_seconds(hours, minutes, seconds):
    return hours*60*60+minutes*60+seconds

# countdown timer
def set_alarm(time_in_seconds):
    if(time_in_seconds==0):
        print("Please enter a time")
        return

    print("Alarm will ring in %s seconds" % time_in_seconds)
    time.sleep(time_in_seconds)
    play_sound()
    print("Alarm rang. Exiting now.")


# pomodoro timer
def pomodoro():

    print("Pomodoro timer started, break time in 25 minutes.")

    while(True):
        time.sleep(25*60)

        play_sound()
        print("Break time! Come back to work in 5 minutes :)")

        time.sleep(5*60)

        play_sound()
        print("Back to work! You have 25 minutes left")
    

# cmd line functionality

# gets user inputted time from cmd line
parser = argparse.ArgumentParser(description='Set the alarm clock or start pomodoro timer.')

group = parser.add_mutually_exclusive_group()

group.add_argument('-p', '--pomodoro', action='store_true', default=False,
                    dest='pomodoro', help='start the pomodoro timer (25 minutes of work, 5 minutes break time)')

group.add_argument('-t', '--timer' , action='store_true', default=False, dest='timer', help='start the timer, -hr <HOUR> -m <MINUTES> -s <SECONDS>')

parser.add_argument('-hr', '--hours', nargs='?', default=0, type=int)

parser.add_argument('-m', '--minutes', nargs='?', default=0, type=int)

parser.add_argument('-s', '--seconds', nargs='?', default=0, type=int)

args = parser.parse_args()

if args.pomodoro:
    pomodoro()
elif args.timer:
    set_alarm(to_seconds( args.hours, args.minutes, args.seconds))
else:
    print("No inputs, please choose -t or -p")

