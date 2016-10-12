# Author: Siladittya Manna
#bet: Alphabet or Number; Single Character; String Format
# Basepath: Folder containing all the subfolders
# path: subfolder path containing the audios


import pygame as aud
import time, wave
#import pymedia.audio.sound as sound
aud.mixer.init()
Basepath = "H:\PROJECT\\"
audext = ".mp3"
#.........................playing voice...................#
#..............For '.wav' files using PyMedia..............#
'''def VoicePlay(bet):
    f = wave.open('H:\PROJECT\Alphabets\Voices\wavfiles\\'+bet+'.wav','rb')
    samplerate = f.getframerate()
    #print samplerate
    channels = f.getnchannels()
    format = sound.AFMT_S16_LE
    snd = sound.Output(samplerate,channels,format)
    s = f.readframes(441000)
    snd.play(s)
    while snd.isPlaying():
        time.sleep(0.05)'''
#.......................................................#
def AudioPlay(bet,path):
    path = Basepath+path+bet+audext
    aud.mixer.music.load(path)
    aud.mixer.music.play()
