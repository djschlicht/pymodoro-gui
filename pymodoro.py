#!/usr/bin/env python3
# pymodoro.py is a pomodoro timer with customizable periods and sounds

import time
import vlc
import tkinter as tk

# settings() gets the variable info from config
# returns tuple (work, rest, sound) where work, rest are the times in 
#	seconds and sound is the filename of an mp3
def settings(config_file):
	with open(config_file) as config:
		for line in config:
			if('work' in line):
				work = line.split('=')[-1].rstrip('\n')
			if('break' in line):
				rest = line.split('=')[-1].rstrip('\n')
			if('sound' in line):
				sound = line.split('=')[-1].rstrip('\n')
	return (int(work)*60, int(rest)*60, sound)

# removes the button and starts pomodoro cycle
def start():
	btn_start.grid_forget()	
	cycle()

def cycle():
	total_pomodoros = 0
	lbl_total = tk.Label(master = window, text = f"Total Pomodoros: {total_pomodoros}")
	lbl_total.grid(row=2, column=0)
	while True:
		lbl_type["text"] = "Pomodoro"
		countdown(work)
		alarm(sound)
		lbl_type["text"] = "Break"
		countdown(rest)
		alarm(sound)
		total_pomodoros += 1
		lbl_total["text"] = f"Total Pomodoros: {total_pomodoros}"

def countdown(t):
	while(t > -1):
		mins, secs = divmod(t, 60)
		timer = '{:02d}:{:02d}'.format(mins, secs)
		lbl_timer["text"] = timer
		window.update()
		time.sleep(1)
		t -= 1

# alarm(f) plays the mp3 file specified by f
def alarm(f):
	p = vlc.MediaPlayer(f)
	p.audio_set_volume(70)
	if(p.play() != 0):
		print("Media not playing")
	time.sleep(3)
	
work, rest, sound = settings('config')
mins, secs = divmod(work, 60)
timer = '{:02d}:{:02d}'.format(mins, secs)


window = tk.Tk()
window.title('Pymodoro')

lbl_type = tk.Label(master = window, text = 'Welcome to Pymodoro!')
lbl_timer = tk.Label(master = window, text = timer)

btn_start = tk.Button(
	master = window,
	text = 'Start', 
	command = start
)

lbl_type.grid(row = 0, column = 0)
lbl_timer.grid(row = 1, column = 0)
btn_start.grid(row = 2, column = 0)

window.mainloop()



		


