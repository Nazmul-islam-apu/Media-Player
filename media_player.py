import os
from tkinter import *
from pygame import mixer
import tkinter.messagebox
from tkinter import filedialog
from tkinter import ttk
import time
from ttkthemes import themed_tk as tk

root = tk.ThemedTk()
root.get_themes()
root.set_theme("clearlooks")
mixer.init()

song_list = []
#create Menu
menu_bar = Menu(root)
root.config(menu=menu_bar)

status_bar = ttk.Label(root, text = "Welcome..", relief_ = SUNKEN, anchor = W)
status_bar.pack(side = BOTTOM, fill = X)

def open_file():
    global file_name
    file_name = filedialog.askopenfilename()
    add_to_playlist()
    mixer.music.queue(file_name)

def add_to_playlist():
    f = os.path.basename(file_name)
    index = 0
    play_list.insert(index,f)
    play_list.pack()
    song_list.insert(index,file_name)
    index+=1

def del_song():
    selected_song = play_list.curselection()
    selected_song = int(selected_song[0])
    play_list.delete(selected_song)
    song_list.pop(selected_song)


#create sub-menu
sub_menu = Menu(menu_bar, tearoff = 0)
menu_bar.add_cascade(label = "File", menu = sub_menu)
#sub_menu.add_command(label="Open", command = open_file)
sub_menu.add_command(label="Exit", command = root.destroy)


def about_us():
    tkinter.messagebox.showinfo("About Shiputhi", "This is a music player developed by Nazmul using Python Tkinter")


sub_menu = Menu(menu_bar, tearoff = 0)
menu_bar.add_cascade(label="Help", menu = sub_menu)
sub_menu.add_command(label="About Us", comman = about_us)

#root.geometry("400x250")
root.title("Shiputhi")
root.iconbitmap(r"icon.ico")



pause = False
def play_music():
    global pause
    if pause == True:
        mixer.music.unpause()
        pause = False
    else:
        try:
            stop_music()
            time.sleep(1)
            selected_song = play_list.curselection()
            selected_song = int(selected_song[0])
            play_it = song_list[selected_song]
            mixer.music.load(play_it)
            mixer.music.play()
            # mixer.music.load(file_name)
            # mixer.music.play()
            status_bar["text"] = "Playing Music:" + " " + os.path.basename(file_name)
        except:
            tkinter.messagebox.showerror("Error","File Not Found")


def stop_music():
    global pause
    mixer.music.stop()
    status_bar["text"] = "Music Stopped"
    pause = False

def music_pause():
    global pause
    pause = True
    mixer.music.pause()
    status_bar["text"] = "Music Paused"

def volume_control(val):
    volume = float(val)/100
    mixer.music.set_volume(volume)

play_image = PhotoImage(file="play.png")
stop_image = PhotoImage(file="stop.png")
pause_image = PhotoImage(file = "pause.png")


left_frame = Frame(root)
left_frame.pack(side = LEFT,padx = 20,pady = 15)
play_list = Listbox(left_frame)
play_list.pack()

btn1 = ttk.Button(left_frame, text = "+Add", command = open_file)
btn1.pack(side=LEFT,padx = 10,pady = 5)

btn2 = ttk.Button(left_frame, text = "-Delete", command = del_song)
btn2.pack(side = LEFT, padx=5, pady = 5)

right_frame = Frame(root)
right_frame.pack(side = RIGHT,padx = 15)

text = Label(right_frame, text="Let's sooth your ears.\n")
text.pack()

top_frame = Frame(right_frame)
top_frame.pack()


middle_frame = Frame(right_frame)
middle_frame.pack(padx = 10)

play_btn = ttk.Button(middle_frame, image = play_image, command = play_music)
play_btn.pack(side = LEFT,padx = 10)

pause_btn = ttk.Button(middle_frame,image = pause_image, command = music_pause)
pause_btn.pack(side=LEFT,padx = 10)

stop_button = ttk.Button(middle_frame,image=stop_image,command= stop_music)
stop_button.pack(side = LEFT,padx = 5)

bottom_frame = Frame(right_frame)
bottom_frame.pack()


volume_scale = ttk.Scale(bottom_frame, from_ = 0, to = 100, orient = HORIZONTAL, command = volume_control)
volume_scale.set(67)
mixer.music.set_volume(67)
volume_scale.pack(pady = 10)

root.mainloop()