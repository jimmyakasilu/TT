# Author: Siladittya Manna



import pygame as aud
import time, wave
#import pymedia.audio.sound as sound
aud.mixer.init()
Audpath = "H:\PROJECT\Alphabets\\"
AudCap = "AudioCap\\"
AudSmall = "AudioSmall\\"
audext = ".mp3"
#.........................playing voice...................#
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
def AudioPlay(bet):
    if bet.isupper():
        path = Audpath+AudCap+bet+audext
    if bet.islower():
        path = Audpath+AudSmall+bet+audext
    aud.mixer.music.load(path)
    aud.mixer.music.play()
