from AudPlay import AudioPlay
from VidPlay import VideoPlay
import time
#........................OUTPUT..........#
def output(bet):
    AudioPlay(bet)
    time.sleep(1)
    VideoPlay(bet)
    time.sleep(2)
    bet=bet.lower()
    AudioPlay(bet)
    time.sleep(1)
    VideoPlay(bet)
