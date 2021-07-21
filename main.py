from tkinter import *
from typing_test import TypingTest

# Constants
YELLOW = "#f7f5dd"

# Globals
elapsed_seconds = 0

test = TypingTest()
started = False


def start_test():
    global started
    if not started:
        started = True
        count_time()


def count_time():
    global elapsed_seconds
    minutes = elapsed_seconds // 60
    seconds = elapsed_seconds % 60
    timer_label.config(text=f"Elapsed Time: {minutes:02d}:{seconds:02d}")
    elapsed_seconds += 1
    if started:
        window.after(1000, count_time)


def submit_test():
    global started
    started = False
    raw_wpm, adjusted_wpm = test.check_test(typing_entry_field.get("1.0", END), elapsed_seconds)
    scores_label.config(text=f"Raw WPM: {raw_wpm}   Adjusted WPM: {adjusted_wpm}")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Frogo Typing Test App")
window.config(padx=50, pady=50, bg=YELLOW)

# LOGO AND APP NAME
canvas = Canvas(width=210, height=110, bg=YELLOW, highlightthickness=0)
logo = PhotoImage(file="assets/logo.png")
smaller_logo = logo.subsample(5, 5)
canvas.create_image(105, 40, image=smaller_logo)
canvas.create_text(105, 85, fill="green", font="Arial 20 normal",
                   text="Frogo Teaches Typing")
canvas.grid(row=0, column=2, columnspan=2)

# Instructions
instructions_label = Label(text="1. Start Typing Test by typing the passage on the left in the right box.\n2.When "
                                "finished, press the submit button below to see your results.",
                           justify=CENTER, fg="green", bg=YELLOW, font="Arial 15 normal", pady=10)
instructions_label.grid(row=1, column=1, columnspan=4)


# Sample Text
sample_label = Label(text="Sample Text", justify=CENTER, fg="green", bg=YELLOW, font="Arial 20 underline", pady=10)
sample_label.grid(row=2, column=1)
sample_text = Text(height=20, width=60, fg="green", bg=YELLOW, highlightthickness=0)
sample_text.insert(END, test.get_typing_text())
sample_text.config(state=DISABLED, wrap=WORD, font="Arial 15 normal")
sample_text.grid(row=3, column=0, columnspan=3, padx=25)

# User Entry
user_text = StringVar()
entry_label = Label(text="Type into Box Below", justify=CENTER, fg="green", bg=YELLOW,
                    font="Arial 20 underline", pady=10)
entry_label.grid(row=2, column=4)
typing_entry_field = Text(height=20, width=60, highlightcolor="#a9a9a9", borderwidth=1)
typing_entry_field.bind("<<Modified>>", func=lambda event: start_test())
typing_entry_field.config(wrap=WORD, font="Arial 15 normal")
typing_entry_field.grid(row=3, column=3, columnspan=3, padx=25)

# Results
results_label = Label(text="Results", justify=CENTER, fg="green", bg=YELLOW, font="Arial 18 underline", pady=10)
results_label.grid(row=4, column=0)
scores_label = Label(text="Raw WPM: 0   Adjusted WPM: 0", justify=CENTER, fg="green", bg=YELLOW, font="Arial 18 bold",
                     pady=10)
scores_label.grid(row=4, column=1, columnspan=2)

# Timer
timer_label = Label(text="Elapsed Time: 00:00", justify=CENTER, fg="red", bg=YELLOW, font="Arial 18 bold", pady=10)
timer_label.grid(row=4, column=3)

# Submit
submit_btn = Button(text="Submit", highlightthickness=0, command=submit_test, justify=CENTER)
submit_btn.grid(row=4, column=5, pady=10)

window.mainloop()
