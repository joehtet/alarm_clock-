import time
import argparse
from util import Util


class Clock():

#Countdown Timer
    def set_alarm(self,time_in_seconds):
        if(time_in_seconds==0):
            print("Please specify a time")
            return

        print("Alarm will ring in %s seconds. Press Ctrl+C to quit." % time_in_seconds)
        time.sleep(time_in_seconds)
        Util.play_sound()
        print("Alarm rang. Exiting now.")


#Pomodoro Timer
#       The Pomodoro technique is:
#           1) (Work - 25 mins, Rest - 5 mins)
#           2) Repeat Step 1 two more times
#           3) (Work - 25 mins, Rest - 15 mins)
#           4) Repeat 1-3

    def set_pomodoro(self):

        while(True):
            for i in range(0,2):
                self._run(25)
                self._run(5)
            self._run(25)
            self._run(15)

    def _run(self, time_type):
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

        Util.play_sound()

