from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
check = ""
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    timer_label.config(text="Timer", font=(FONT_NAME, 50), fg=GREEN, bg=YELLOW)
    global reps, check
    reps = 0
    check = ""
    checkmark_label.config(text=check)
    canvas.itemconfig(timer_text, text="00:00")


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    global check
    reps += 1
    if reps % 2 == 1:
        timer_label.config(text="Work", font=(FONT_NAME, 50), fg=GREEN, bg=YELLOW)
        count_down(WORK_MIN * 60)
    else:
        if reps % 8 == 0:
            timer_label.config(text="Break", font=(FONT_NAME, 50), fg=PINK, bg=YELLOW)
            count_down(LONG_BREAK_MIN * 60)
            check += "✔"
            checkmark_label.config(text=check)
        else:
            timer_label.config(text="Break", font=(FONT_NAME, 50), fg=RED, bg=YELLOW)
            count_down(SHORT_BREAK_MIN * 60)
            check += "✔"
            checkmark_label.config(text=check)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    minutes = int(count / 60)
    seconds = count % 60
    if seconds < 10:
        seconds = f"0{seconds}"
    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    elif count == 0:
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

timer_label = Label(text="Timer", font=(FONT_NAME, 50), fg=GREEN, bg=YELLOW)
timer_label.grid(row=0, column=1)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_image)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 25, "bold"))
canvas.grid(row=1, column=1)

start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(row=2, column=0)

reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(row=2, column=2)

checkmark_label = Label(fg=GREEN, bg=YELLOW)
checkmark_label.grid(row=3, column=1)

window.mainloop()
