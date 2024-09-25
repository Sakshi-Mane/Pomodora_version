
from tkinter import Tk, Label, Button, Canvas, PhotoImage
import math


REPETITIONS = 0
TIMER = None


def reset_timer():
    window.after_cancel(TIMER)
    canvas.itemconfig(timer_text, text="00:00")
    text_label.config(text="Timer", fg="#C96868")
    global REPETITIONS
    REPETITIONS = 0


def start_timer():
    global REPETITIONS
    REPETITIONS += 1

    work_min = 25 * 60
    short_break = 5 * 60
    long_break = 20 * 60

    if REPETITIONS % 8 == 0:
        update_time(long_break)
        text_label.config(text="Break", fg="#E85C0D")
    elif REPETITIONS % 2 == 0:
        update_time(short_break)
        text_label.config(text="Break", fg="#C7253E")
    else:
        update_time(work_min)
        text_label.config(text="Work", fg="#54C392")


def update_time(count):

    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global TIMER
        TIMER = window.after(1000, update_time, count - 1)
    else:
        start_timer()


window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg="#FADFA1")


text_label = Label(text="Timer", fg="#C96868", bg="#FADFA1", font=("Courier", 35))
text_label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg="#FADFA1", highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=("Courier", 32, "bold"))
canvas.grid(column=1, row=1)

start_button = Button(text="Start", command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", command=reset_timer)
reset_button.grid(column=2, row=2)



window.mainloop()