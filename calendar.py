from tkinter import *
from tkinter import Tk, Label
from PIL import Image, ImageTK
import calendar

root=Tk, Tk()
root.geomentry('400x300')
root.title('calendar')

def show():

    m = int(month.get())
    y=  int(year.get())
    output = calendar.month(y,m)

    cal.insert('end' ,output)

def clear():
    cal.delete(1.0, 'end')

def exit():
    root.desteroy()



img = ImageTk .phtotimage(Image.open('calendar.png'))
label = Label(Image=img)
label.place(x=170, y=3)

m_label = Label(root, text='month', font=('10', 'verdana', 'bold'))
m_label.place(x=250, y=80)

month = Spinbox(root, from_=11, to = 12, width=5)
month.place(x=140, y=80)

year = Spinbox(root, from_=2023, to = 3000 , width="8")
year.place(x=260, y=80)

cal = Text(root, width=33, height=8 , relief=RIDGE, borderwidth=2)
cal.place(x=70, y=110)

show = (Button(root, text="show", font=('verdana', '10', 'bold'), relief = RIDGE, borderwidth=2, command=show))
show.place(x=140, y=250)

clear = (Button(root, text="clear", font=('verdana', '10', 'bold'), relief = RIDGE, borderwidth=2, command=clear))
clear.place(x=200, y=250)

exit = (Button(root, text='exit', font=('veranda', '10', 'bold'), relief = RIDGE, boederwidth=2, comand=clear))
exit.place(x=260, y=250)


root.mainloop()
