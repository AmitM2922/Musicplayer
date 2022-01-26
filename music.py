from tkinter import* # * call all the function present in tkinter like button , label , widgets
from tkinter import filedialog 
from mutagen.id3 import ID3


import pygame



pygame.mixer.init()
display=Tk()
display.geometry('450x250+100+100')
display.title('MUSIC MP3 BY AMIT MULMULE')
display.configure(bg='gray',relief=GROOVE,bd=8)

songname=StringVar()


def stopmp3():
    pygame.mixer.music.pause()
    display.stop.grid_remove()
    display.Resume.grid()

def resumemp3():
    pygame.mixer.music.unpause() 
    display.Resume.grid_remove()
    display.stop.grid()


def play():
    music=songname.get()
    pygame.mixer.music.load(music)
    pygame.mixer.music.play()


def mp3path():
    mp3=filedialog.askopenfilename()
    songname.set(mp3)
    listofsongs=[songname.set(mp3)]
    



def widgets():
    #label...
    music=Label(display,text='MUSIC MP3 By Amit Mulmule', bg='gray' ,font=('bold',20),fg='black',relief=GROOVE,bd=10)
    music.grid(row=0,column=1,columnspan=3)

    #entrybox...

    Box=Entry(display,bg='snow',width=32,bd=6,font=('bold',15),textvariable=songname,fg='blue',relief=RAISED)
    Box.grid(row=1,column=1)

    #search buttons..

    searchbutton=Button(display,text="Search",bg='Yellow',font=('bold',15),bd=8,activebackground='red',relief=GROOVE,command=mp3path)        
    searchbutton.grid(row=1,column=2)

#playbutton....

    playbutton=Button(display,text='PLAY',bg='red',font=('BOLD',17),bd=8,activebackground='gold',relief=GROOVE,command=play,fg='orange')
    playbutton.grid(row=2,column=1)

    

    #STOPBUTTON...
    display.stop=Button(display,text='STOP',bg='red',font=('BOLD',17),bd=8,activebackground='yellow',relief=GROOVE,command=stopmp3,fg='orange')
    display.stop.grid(row=3,column=1)


     #resumebutton...
    
    display.Resume=Button(display,text='Resume',bg='red',font=('bold',17),activebackground='orange',bd=8,relief=GROOVE,command=resumemp3,fg='orange')
    display.Resume.grid(row=3,column=1)
    display.Resume.grid_remove()


   

widgets()
display.mainloop() 
