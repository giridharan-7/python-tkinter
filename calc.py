from tkinter import *

def m_t_k():
    miles = float(m_i.get())
    km = miles*1.609
    kr_l.config(text=f"{km}")

window = Tk()
window.title("Miles to kilometer convertor")
window.config(padx=20, pady=20)

m_i = Entry(width=7)
m_i.grid(column=1, row=0)

m_l = Label(text="Miles")
m_l.grid(column=2, row=0)

e_l = Label(text="is equal to")
e_l.grid(column=0,row=1)

kr_l = Label(text="0")
kr_l.grid(column=1, row=1)

k_l = Label(text="Km")
k_l.grid(column=2, row=1)

c_b = Button(text="Calculate", command=m_t_k)
c_b.grid(column=1, row=2)

window.mainloop()