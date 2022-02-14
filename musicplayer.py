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
import simpleaudio
from mutagen.easyid3 import EasyID3
import taglib
import PySimpleGUI as sg
from io import BytesIO
from mutagen.id3 import ID3
from PIL import Image
import time
import re
import threading
import os
#import psutil

def plays():
    global title,sud,ext,bit,st,th,plpa,art,cover_img,value

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


    song = taglib.File(sud)
    title=str(song.tags['TITLE'])
    title=title.strip('[\'').strip('\']')

    art=str(song.tags['ARTIST'])
    art=art.strip('[\'').strip('\']')

    tags = ID3(sud)

    apic = tags.get("APIC:")

    cover_img = Image.open(BytesIO(apic.data))
    cover_img.save(f"art\\{art}_{title}.jpg")
    #image_elem.update(source=f"art\\{art}_{title}.jpg")
    #window['arrt'].update(f"art\\{art}_{title}.jpg")
    #window.find_element('arrt').Update(source=f"art\\{art}_{title}.jpg")
    #window.find_element('arrt').Update(f"art\\{art}_{title}.jpg")
    #cover_img.show()

    print('Title:',title,'\tFormat:',ext,'\ttime:',round(time1),'sec','\tBitrate:',bit//1000,'Kbps\n')
  
    simpleaudio.stop_all()
    plpa='icon\\play.png'

    thread5.start()
    th=1

    return

def pl():
    global sud,ext,bit,plf,a,th,plpa
    plpa='icon\\pause.png'
    sound=AudioSegment.from_file(sud,format=ext,bitrate=bit,stop=True)
    a=play(sound)
    st=2
    plf=th=1
    return


def stop():
    simpleaudio.stop_all()

def info():
    #print('Title:',ti1,'\tFormat:',ext,'\ttime:',round(time1),'sec','\tBitrate:',bit//1000,'Kbps','\tsamplerate:',slp,'Hz\n')
    #print('Title:',title,'\tFormat:',ext,'\ttime:',round(time),'sec','\tBitrate:',bit//1000,'Kbps\n')
    print('Title:',data[0],'\tFormat:',data[1],'\ttime:',round(data[2]),'sec','\tBitrate:',data[3]//1000,'Kbps\n')
    return

def playing():
    global plf
    while True:
        print('\rPlaying   ',end='')
        if plf==1:
            p=0
            break
        time.sleep(1)
        print('\rPlaying.  ',end='')
        if plf==1:
            p=0
            break
        time.sleep(1)
        print('\rPlaying.. ',end='')
        if plf==1:
            p=0
            break
        time.sleep(1)
        print('\rPlaying...',end='')
        if plf==1:
            p=0
            break
        time.sleep(1)
    return


border=0
plf=st=i=th=c=cc=0
plpa='icon\\play.png'
#gsud=gext=gtitle='f'
a=cover_img=None
art=title=value='None'
#sud = 'music\\Preserved Roses.mp3'


sg.theme('DarkBlack')

#ftm=sg.Frame('',[[sg.Button(image_filename=plpa,key='bb',button_color=('#ffffff', '#000000'),border_width=border)]],size=(680,100),border_width=border)
ftm=sg.Frame('',[[sg.Button('Play',key='bb',button_color=('#ffffff', '#000000'),border_width=1,size=(6,3),pad=((300,0),(20,0)))]],size=(680,100),border_width=border)

ftl=sg.Frame('',[
    [sg.Text('no title',key='tit',font=('Segoe UI Variable Small Light',15),pad=((30,0),(20,0)))],
    [sg.Text(key='art',font=('Segoe UI Variable Small Light',9),pad=((30,0),(0,0)))]
    ],size=(300,100),border_width=border)

ftr=sg.Frame('',[[sg.Button ('b',key='b'),sg.Button ('t',key='cc')]],size=(300,100),border_width=border)

fmi=sg.Frame('',[],size=(800,620),border_width=border)

image_elem=sg.Image(source=f"art\\{art}_{title}.jpg",key='arrt')
fle=sg.Frame('',[
    [image_elem]
    ],size=(230,620),border_width=border)

fri=sg.Frame('',[],size=(250,620),border_width=border)


layout=[
    [fle,fmi,fri],[ftl,ftm,ftr]
    ]

window=sg.Window('MusicPlayer',layout,resizable=True)

'''
thread1=threading.Thread(target=plays)
thread2=threading.Thread(target=info)
thread3=threading.Thread(target=playing)
thread5=threading.Thread(target=pl)'''




#print(song.tags)
#{'ALBUM': ['white forces'], 'ARTIST': ['fripSide'], 'COMMENT': ['Uploaded by Mashin'], 'DATE': ['2016'], 'GENRE': ['Anime'], 'TITLE': ['white forces'], 'TRACKNUMBER': ['1/4']}

while True:
    event,values=window.read()
    
    thread1=threading.Thread(target=plays)
    thread2=threading.Thread(target=info)
    thread3=threading.Thread(target=playing)
    thread5=threading.Thread(target=pl)



    if event is None:
        print('exit')
        break

    #print(st)


    if event=='bb':
        if st==1:pass
        else:
            #thread4.start()
            #i=0
            
            if cc==0:
                window['bb'].update('Pause')
                sud = 'music\\Preserved Roses.mp3'
                cc+=1
                print(cc)
            elif cc==1:
                stop()
                cc+=1
                print(cc)
            elif cc==2:
                window['bb'].update('Play')
                sud = 'music\\white forces.mp3'
                cc+=1
                print(cc)
            elif cc==3:
                stop()
                cc=0
                print(cc)

            if cc%2==0:
                print(cc)
                pass
            else:
                print(cc)
                plays()

            window['tit'].update(title)
            window['art'].update(art)

            if c==0:
                window['bb'].update('Pause')
                c=1
            else:
                window['bb'].update('Play')
                c=0

            #st=1

    if event=='cc':
        if st==1:pass
        else:
            #thread4.start()
            #i=1
            sud = 'music\\white forces.mp3'
            plays()
            #data=set()
            window['tit'].update(title)

    #else:pass
window.close()




'''


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



thread1=threading.Thread(target=plays)
thread2=threading.Thread(target=info)
thread3=threading.Thread(target=playing)




thread1.start()
thread2.start()

thread2.join()
thread3.start()

thread1.join()
plf=1
thread3.join()

print('\nBye')'''