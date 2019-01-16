import os
import time
from pygame import mixer

class Util:

    def play_sound():

        mixer.init()

        dir_path = os.path.dirname(os.path.realpath(__file__))

        mixer.music.load(os.path.join(dir_path, "sound.wav"))
        mixer.music.play()

        #pauses program so the sound can finish playing before pygame.mixer.quit() executes
        time.sleep(1)

        mixer.quit()

    # Converts total time to seconds
    def to_seconds(hours, minutes, seconds):
        return hours*60*60+minutes*60+seconds
