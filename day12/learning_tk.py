import tkinter as tk
def button_clicked():
    new_text = input.get()
    my_label.config(text=new_text)
# Window
window =  tk.Tk() #creating window
window.minsize(height=300,width=500) #window size


#Title
window.title("TITLE") #Title name

#Label
my_label = tk.Label(text="I'm a label",font = ('Arial', 24, 'bold'))
my_label.pack() # center and displays the label

my_label['text'] = 'New Text'
my_label.config(text="New Text")

# Button

button  = tk.Button(text="click me",command=button_clicked) #command (function to call)
button.pack()


#Entry (input)
input = tk.Entry(width=12,)
input.insert('end',string = 'Email')
input.pack()

#text entry box (multi entry)
text_box = tk.Text(width=50,height=10)
text_box.focus()
text_box.insert("end",chars = "Example of multitext entry.")
text_box.pack()


# Spinbox

# Scale

#Check Button

# Radio Button

# List Box







#Keeps the window alive and listen to events
window.mainloop()