from tkinter import *
import pyqrcode
from PIL import ImageTk,Image
root= Tk()
def generate():
    link_name=nameentry.get()
    link=linkentry.get()
    file_name=link_name + ".png"
    url=pyqrcode.create(link)
    url.png(file_name,scale=4)
    image=ImageTk.PhotoImage(Image.open(file_name))
    image_label=Label(image=image)
    image_label.image=image
    canvas.create_window(200,450,window=image_label)
canvas=Canvas(root,width=500,height=1000)
canvas.pack()
app_label=Label(root,text="QR CODE GENERATOR",fg="blue",font=("Arial",30))
canvas.create_window(250,100,window=app_label)
name_label=Label(root,text="link name")
Link_label=Label(root,text="Link")
canvas.create_window(200,150,window=name_label)
canvas.create_window(200,200,window=Link_label)
nameentry=Entry(root)
linkentry=Entry(root)
canvas.create_window(200,180,window=nameentry)
canvas.create_window(200,230,window=linkentry)
button=Button(root,text="Generate QR Code",command=generate)
canvas.create_window(200,280,window=button)
root.mainloop()

