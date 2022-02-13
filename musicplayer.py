'''
musicplayer.py

Copyright (c) 2022 s1gnsgrfu

This software is released under the MIT License.
see https://github.com/s1gnsgrfu/MusicPlayer/blob/master/LICENSE
'''
#pydub,mutagen,pysimplegui,pytaglib
from pydub import AudioSegment
from pydub.utils import mediainfo
from pydub.playback import play
#from mutagen.easyid3 import EasyID3
import taglib
import PySimpleGUI as sg
import time
import re
import threading
import os

border=1
'''
sud = 'music\\white forces.mp3'
song = taglib.File(sud)
title=str(song.tags['TITLE'])
title=title.strip('[\'').strip('\']')
print(title)'''

sg.theme('DarkBlack')

ftm=sg.Frame('',[],size=(680,100),border_width=border)

ftl=sg.Frame('',[
    [sg.Text(key='tit')]
    ],size=(300,100),border_width=border)

ftr=sg.Frame('',[],size=(300,100),border_width=border)

fmi=sg.Frame('',[],size=(800,620),border_width=border)

fle=sg.Frame('',[],size=(230,620),border_width=border)

fri=sg.Frame('',[],size=(250,620),border_width=border)


layout=[
    [fle,fmi,fri],[ftl,ftm,ftr]
    ]

window=sg.Window('MusicPlayer',layout,resizable=True)

sud = 'music\\white forces.mp3'
song = taglib.File(sud)
title=str(song.tags['TITLE'])
title=title.strip('[\'').strip('\']')
print(title)
#print(song.tags)
#{'ALBUM': ['white forces'], 'ARTIST': ['fripSide'], 'COMMENT': ['Uploaded by Mashin'], 'DATE': ['2016'], 'GENRE': ['Anime'], 'TITLE': ['white forces'], 'TRACKNUMBER': ['1/4']}

while True:
    event,values=window.read()

    if event is None:
        print('exit')
        break
    window['out'].update(title)
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