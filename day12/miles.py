from tkinter import *
def calculate():
    num = int(mile.get())
    res = num*2
    km.config(text=str(res))



window = Tk()
# window.minsize(width=500,height=300)
window.config(padx=30,pady=30)
mile_label = Label(text='Miles')
mile_label.grid(column=3,row=0)


equal_label = Label(text='is equal to')
equal_label.grid(column=0,row=1)

km = Label(text='0')
km.grid(row=1,column=1)

km_label = Label(text='Km')
km_label.grid(row=1,column=2)


mile = Entry(width=5)
mile.grid(column=1,row=0)

button = Button(text='Calculate',command=calculate)
button.grid(row=2,column=1)





window.mainloop()