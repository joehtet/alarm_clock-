import time
import pygame
import argparse

# play the alarm sound. quit mixer to stop CPU activity while idle
def play_sound():
    pygame.mixer.init()

    pygame.mixer.music.load("sound.wav")
    pygame.mixer.music.play()

    #pauses program so the sound can finish playing before pygame.mixer.quit() executes
    time.sleep(1)

    pygame.mixer.quit()

# converts total time to seconds
def to_seconds(hours, minutes, seconds):
    return hours*60*60+minutes*60+seconds

# countdown timer
def set_alarm(time_in_seconds):
    if(time_in_seconds==0):
        print("Please enter a time")
        return

    print("Alarm will ring in %s seconds. Press Ctrl+C to quit." % time_in_seconds)
    time.sleep(time_in_seconds)
    play_sound()
    print("Alarm rang. Exiting now.")

def run(time_type):
    print("\nPress Ctrl+C to quit\n")

    for i in range(time_type,0,-1):
        if(time_type==25):
            print("Pomodoro timer started, break time in %i minutes." % i, end="\r", flush=True)
        elif(time_type==5):
            print("\rBreak time! Come back to work in %i minutes :)" % i, end="\r", flush=True)
        else:
            print("\rYou've earned a long break time! Come back to work in %i minutes :)" % i, end="\r", flush=True)

        # sleep for 1 min
        time.sleep(60)

    play_sound()


# pomodoro timer
def pomodoro():
    keyPressed = False

    while(not keyPressed):
        for i in range(0,2):
            run(25)
            run(5)
        run(25)
        run(15)
       
    

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

try:
    if args.timer:
        set_alarm(to_seconds( args.hours, args.minutes, args.seconds))
    else:
        pomodoro()

except KeyboardInterrupt:
    print("\nGoodbye")
    

