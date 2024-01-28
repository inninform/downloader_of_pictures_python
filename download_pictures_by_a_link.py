import requests
from tkinter import *
from tkinter import filedialog

program = Tk()
program.title("download photos")

lbl1 = Label(program,text="enter url of image : ")
lbl1.pack()

url_img = Entry(program)
url_img.pack(pady=20)

lbl2 = Label(program,text="enter name of image with his type : ")
lbl2.pack()

name_img = Entry(program)
name_img.pack(pady=20)

btn = Button(program,text="run")
btn.pack()

def func():
    dir = filedialog.askdirectory(title="ask for directory for saving the image")
    print(url_img.get())
    print(name_img.get())
    r = requests.get(url_img.get())
    with open(fR"{dir}/{name_img.get()}", 'wb') as f:
        f.write(r.content)
btn.config(command=func)

program.mainloop()