'''
musicplayer.py

Copyright (c) 2022 s1gnsgrfu

This software is released under the MIT License.
see https://github.com/s1gnsgrfu/MusicPlayer/blob/master/LICENSE
'''

from pydub import AudioSegment
from pydub.utils import mediainfo
from pydub.playback import play
import PySimpleGUI as sg
import time
import threading
import os

sg.theme('DarkBlack')

fti=sg.Frame('',[],size=(1280,100),border_width=0)
fmi=sg.Frame('',[],size=(800,620),border_width=0)
fle=sg.Frame('',[],size=(230,620),border_width=0)
fri=sg.Frame('',[],size=(250,620),border_width=0)

layout=[
    [fle,fmi,fri],[fti]
    ]

window=sg.Window('MusicPlayer',layout,resizable=True)

while True:
    event,values=window.read()

    if event is None:
        print('exit')
        break

window.close()




'''
def plays():
    sound=AudioSegment.from_file(sud,format=ext,bitrate=bit)
    play(sound)

def info():
    print('Title:',ti1,'\tFormat:',ext,'\ttime:',round(time1),'sec','\tBitrate:',bit//1000,'Kbps\n')

def playing():
    while True:
        print('\rPlaying   ',end='')
        if plf==1:break
        time.sleep(1)
        print('\rPlaying.  ',end='')
        if plf==1:break
        time.sleep(1)
        print('\rPlaying.. ',end='')
        if plf==1:break
        time.sleep(1)
        print('\rPlaying...',end='')
        if plf==1:break
        time.sleep(1)
    #os.system('cls')

plf=0

thread1=threading.Thread(target=plays)
thread2=threading.Thread(target=info)
thread3=threading.Thread(target=playing)

sud = 'C:\Windows\Media\Ring10.wav'
bit = int(mediainfo(sud)['bit_rate'])


target='\\'
idx=sud[::-1].find(target)
ti=sud[-idx:]

target2='.'
idx2=ti.find(target2)
ext=ti[idx2+1:]
ti1=ti[:idx2]

sau = AudioSegment.from_file(sud, ext)
time1 = sau.duration_seconds


thread1.start()
thread2.start()

thread2.join()
thread3.start()

thread1.join()
plf=1
thread3.join()

print('\nBye')'''