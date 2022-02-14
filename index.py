from operator import ge
from tracemalloc import stop
from webbrowser import get
from click import command
import pygame
import tkinter as tk
from tkinter.filedialog import askdirectory
import os
from tkinter.ttk import *
import time

# Make the Music Player Window

music_player = tk.Tk()
music_player.title("MUSIC PLAYER")
music_player.geometry("600x450")
# p1 = PhotoImage(file = 'icon.jpeg')
# music_player.iconphoto(False, p1)
music_player.iconbitmap("icon.ico")

#Provide the directory where the music files are stored

directory= askdirectory()
os.chdir(directory)
song_list = os.listdir()

#List of songs in the playlist

play_list = tk.Listbox(music_player, font="Helvetica 12 bold", bg='#ffffff', selectmode=tk.SINGLE)

#Looping through each song

for item in song_list:
    pos = 0
    play_list.insert(pos,item)
    pos += 1

pygame.init()
pygame.mixer.init()

#Defining the functions

def play():
    pygame.mixer.music.load(play_list.get(tk.ACTIVE))
    var.set(play_list.get(tk.ACTIVE))
    pygame.mixer.music.play()

def fadeout():
    pygame.mixer.music.fadeout(1200)

def pause():
    pygame.mixer.music.pause()

def unpause():
    pygame.mixer.music.unpause()


#Making the buttons and assigning them for their particular function

Button1 = tk.Button(music_player , width = 6 , height = 4 , font = "Helvetica 12 bold", text = "PLAY", command = play,bg = "#11edb2", fg = "Black")

Button2 = tk.Button(music_player , width = 6 , height = 4 , font = "Helvetica 12 bold", text = "STOP", command = fadeout ,bg = "#d49a3d", fg = "Black") 

Button3 = tk.Button(music_player , width = 6 , height = 4 , font = "Helvetica 12 bold", text = "PAUSE", command = pause,bg = "#b611ed", fg = "Black")

Button4 = tk.Button(music_player , width = 6 , height = 4 , font = "Helvetica 12 bold", text = "UNPAUSE", command = unpause,bg = "#f51307", fg = "Black")



var = tk.StringVar()
song_title = tk.Label(music_player, font="Helvetica 12 bold", textvariable=var)
song_title.pack()
Button1.pack(fill = 'x')
Button2.pack(fill = 'x')
Button3.pack(fill = 'x')
Button4.pack(fill = 'x')

play_list.pack(fill = "both", expand = "yes")
music_player.mainloop()