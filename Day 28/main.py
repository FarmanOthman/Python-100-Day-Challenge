import math
import tkinter as tk

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# Global variables to track the number of repetitions (reps) and the timer reference
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global reps, timer
    # Cancel the timer if it's running
    if timer is not None:
        window.after_cancel(timer)
        timer = None
    
    # Reset reps to 0
    reps = 0
    
    # Reset the timer text to "00:00"
    canvas.itemconfig(timer_text, text="00:00")
    
    # Reset the title label to "Timer"
    titleL.config(text="Timer")
    
    # Reset the check marks label to an empty string
    check_mark.config(text="")

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        time_down(long_break_sec)
        titleL.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        time_down(short_break_sec)
        titleL.config(text="Break", fg=PINK)
    else:
        time_down(work_sec)
        titleL.config(text="Work", fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def time_down(count):
    global timer
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        timer = window.after(1000, time_down, count - 1)
    else:
        start_timer()
        # Add checkmark after every completed work session (every 2 reps)
        if reps % 2 == 0:
            work_sessions = math.floor(reps / 2)
            marks = "✓" * work_sessions
            check_mark.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

titleL = tk.Label(text="Timer", font=(FONT_NAME, 50, "bold"), bg=YELLOW, fg=GREEN)
titleL.grid(row=0, column=1)

canvas = tk.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
photo = tk.PhotoImage(file=r"C:\Users\DELL\OneDrive\Desktop\coding\python\Day 28\tomato.png")
canvas.create_image(100, 112, image=photo)
canvas.grid(row=1, column=1)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))

start_button = tk.Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(row=3, column=0)
restart_button = tk.Button(text="Reset", highlightthickness=0, command=reset_timer)
restart_button.grid(row=3, column=2)
check_mark = tk.Label(text="", font=(FONT_NAME, 15, "bold"), bg=YELLOW, fg=GREEN)
check_mark.grid(row=4, column=1)

window.mainloop()
