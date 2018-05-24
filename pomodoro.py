from clock import Clock
from util import Util 
import argparse

# Commandline Functionality

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
    clk = Clock()

    if args.timer:
        clk.set_alarm(Util.to_seconds( args.hours, args.minutes, args.seconds))
    else:
        clk.set_pomodoro()

except KeyboardInterrupt:
    print("\n\nGoodbye")
    


