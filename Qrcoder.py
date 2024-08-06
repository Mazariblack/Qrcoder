from generator import qrc
from tkinter import *
from tkinter import messagebox


root = Tk()

def btn_click():
    link = link1.get()
    size = link2.get()
    name = link3.get()
    size = int(size)
    Qr = qrc.CreateQr(link, size, name)
    messagebox.showinfo(title = 'Process ending', message = Qr)


title1 = Label(root, text = 'Type URL')
title1.pack()
link1 = Entry(root, font=('calibre',10,'normal'))
link1.pack()

title2 = Label(root, text = 'Type size of qrcode')
title2.pack()
link2 = Entry(root, font=('calibre',10,'normal'))
link2.pack()

title3 = Label(root, text = 'Type name of image file')
title3.pack()
link3 = Entry(root, font=('calibre',10,'normal'))
link3.pack()

btn = Button(text = 'Create', command = btn_click)
btn.pack()

root['bg'] = '#fafafa'
root.title('Qrcoder')
root.geometry('300x250')
root.resizable(width = False, height = False)
root.mainloop()
