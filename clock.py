import time
import argparse
from util import Util


class Clock():

    def __init__(self):
        self.keyPressed = False 


# Countdown Timer

    def set_alarm(self,time_in_seconds):
        if(time_in_seconds==0):
            print("Please enter a time")
            return

        print("Alarm will ring in %s seconds. Press Ctrl+C to quit." % time_in_seconds)
        time.sleep(time_in_seconds)
        Util.play_sound()
        print("Alarm rang. Exiting now.")


# Pomodoro Timer

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
            time.sleep(0.5)

        Util.play_sound()


    def set_pomodoro(self):

        while(not self.keyPressed):
            for i in range(0,2):
                self._run(25)
                self._run(5)
            self._run(25)
            self._run(15)

