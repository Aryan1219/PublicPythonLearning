import tkinter as tk
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Ubuntu"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global reps
    window.after_cancel(timer)
    canvas.itemconfig(timer_text,text = f"00:00")
    timer_label.config(text='Timer',font=(FONT_NAME,40),bg=YELLOW,fg=GREEN)
    checkmark.config(text='')
    reps =0


    
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN*60
    short_break_sec=SHORT_BREAK_MIN*60
    long_break_sec = LONG_BREAK_MIN*60

    if reps %8 ==0:
        timer_label.config(text='Long Break',font=(FONT_NAME,40),bg=YELLOW,fg=RED)
        countdown(long_break_sec)


    elif reps % 2 ==0:
        timer_label.config(text='Short Break',font=(FONT_NAME,40),bg=YELLOW,fg=PINK)
        countdown(short_break_sec) 
    else :
        timer_label.config(text='Work',font=(FONT_NAME,40),bg=YELLOW,fg=GREEN)
        countdown(work_sec)
        



# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(count):
    count_min = count // 60 
    if count_min <10:
        count_min = f"0{count_min}"
    count_sec = count % 60
    if count_sec <10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text,text = f"{count_min}:{count_sec}")
    if count >0:
        global timer
        timer = window.after(1000,countdown,count-1)
    else:
        start_timer()
        checkmark.config(text='✔'*(reps//2),bg=YELLOW,fg=GREEN,font =('Ubuntu',20,'bold'))

        
# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title('Pomodoro')
window.config(padx=100, pady=50,bg= YELLOW)

#timer label
timer_label = tk.Label(text='Timer',font=(FONT_NAME,40),bg=YELLOW,fg=GREEN)
timer_label.grid(row=0,column=1)

#buttons
start_button = tk.Button(text='Start',width=8,font = FONT_NAME,highlightthickness=0 ,command=start_timer)
start_button.grid(row=2,column=0)
reset_button = tk.Button(text='Reset',width=8,font=FONT_NAME,highlightthickness=0, command=reset_timer )
reset_button.grid(row=2,column=2)

#checkmark
checkmark = tk.Label(bg=YELLOW,fg=GREEN,font =('Ubuntu',20,'bold'))
checkmark.grid(row=3,column=1)

#canvas
canvas = tk.Canvas(width=200,height=224,highlightthickness=0,bg=YELLOW)
tom_img = tk.PhotoImage(file='/home/aryan/Desktop/python/PublicPythonLearning/day12/pomodoro-start/tomato.png')
canvas.create_image(100, 112, image=tom_img)
timer_text = canvas.create_text(100,130,fill='White',font=(FONT_NAME,35,'bold'), text = '00:00')
canvas.grid(row=1,column=1) 





window.mainloop()