import tkinter as tk
import time
import math

def update_clock():

    current_time = time.localtime()
    hours = current_time.tm_hour % 12
    minutes = current_time.tm_min
    seconds = current_time.tm_sec

    second_angle = math.radians((seconds / 60) * 360 - 90)
    minute_angle = math.radians((minutes / 60) * 360 - 90)
    hour_angle = math.radians((hours / 12) * 360 + (minutes / 60) * 30 - 90)

    second_x = 150 + 100 * math.cos(second_angle)
    second_y = 150 + 100 * math.sin(second_angle)
    minute_x = 150 + 80 * math.cos(minute_angle)
    minute_y = 150 + 80 * math.sin(minute_angle)
    hour_x = 150 + 50 * math.cos(hour_angle)
    hour_y = 150 + 50 * math.sin(hour_angle)

    canvas.coords(second_hand, 150, 150, second_x, second_y)
    canvas.coords(minute_hand, 150, 150, minute_x, minute_y)
    canvas.coords(hour_hand, 150, 150, hour_x, hour_y)

    digital_time = time.strftime("%H:%M:%S")
    date_today = time.strftime("%A, %d %B %Y")
    digital_label.config(text=digital_time)
    date_label.config(text=date_today)

    canvas.after(1000, update_clock)

root = tk.Tk()
root.title("Relógio Analógico e Digital")

canvas = tk.Canvas(root, width=300, height=300, bg="white")
canvas.pack()

canvas.create_oval(50, 50, 250, 250, outline="black", width=2)

for i in range(12):
    angle = math.radians((i / 12) * 360)
    x_start = 150 + 90 * math.cos(angle)
    y_start = 150 + 90 * math.sin(angle)
    x_end = 150 + 100 * math.cos(angle)
    y_end = 150 + 100 * math.sin(angle)
    canvas.create_line(x_start, y_start, x_end, y_end, fill="black", width=2)

hour_hand = canvas.create_line(150, 150, 150, 100, fill="black", width=4)
minute_hand = canvas.create_line(150, 150, 150, 80, fill="blue", width=3)
second_hand = canvas.create_line(150, 150, 150, 50, fill="red", width=2)

digital_label = tk.Label(root, font=("Helvetica", 24), bg="black", fg="white")
digital_label.pack(fill="x")

date_label = tk.Label(root, font=("Helvetica", 16), bg="black", fg="white")
date_label.pack(fill="x")

update_clock()

root.mainloop()
