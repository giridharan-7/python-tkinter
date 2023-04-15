from tkinter import *

window = Tk()
window.title("Mile to Km Convertor")
window.minsize(width=400,height=200)
# window.config(padx=10,pady=20)

my_label = Label(text="Miles", font=("Arial",10,"bold"))
my_label.grid(column=2, row=1)
my_label.config(padx=50,pady=50)

def button_clicked():
    new_text = input.get()
    my_label["text"] = new_text

button = Button(text="Click me", command=button_clicked)
# button.pack()
button.grid(column=1, row=0)

new_button = Button(text="New Button")
new_button.grid(column=2, row=0)

input = Entry(width=10)
# input.pack()
input.get()
input.grid(column=1, row=0)



window.mainloop()