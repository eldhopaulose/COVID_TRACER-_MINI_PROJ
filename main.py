from cProfile import label
import photo
from tkinter import * 
import threading
import PIL.Image, PIL.ImageTk
import cv2

top = Tk() 

# top.geometry("900x500")  

name_var=StringVar()
mobile_var=StringVar()
temp_var=StringVar()

name_label = Label(top, text = 'Full Name: ', font=('calibre',10, 'bold')) 
name_label.grid(row=0,column=0)
name_entry = Entry(top,textvariable = name_var, font=('calibre',10,'normal'))
name_entry.grid(row=0,column=1, padx=5, pady=5)
name=name_var.get()
mobile_label = Label(top, text = 'Mobile No.: ', font=('calibre',10, 'bold')) 
mobile_label.grid(row=1,column=0)
mobile_entry = Entry(top,textvariable = mobile_var, font=('calibre',10,'normal'))
mobile_entry.grid(row=1,column=1, padx=5, pady=5)
temp_label = Label(top, text = 'Temprature: ', font=('calibre',10, 'bold')) 
temp_label.grid(row=2,column=0)
temp_entry = Entry(top,textvariable = temp_var, font=('calibre',10,'normal'))
temp_entry.grid(row=2,column=1)
capture_button = Button(top, text = 'Capture image', command = None, font=('calibre',10,'normal'))
capture_button.grid(row=3,column=0, padx=20, pady=15, columnspan=2)
panel = Label(top, image=None)
panel.grid(row=4, column=0, padx=10, pady=10)


img = cv2.imread('opencv_frame_{}.png'.format('eldho1'), cv2.IMREAD_COLOR)
scale_percent = 20 # percent of original size
width = int(img.shape[1] * scale_percent / 100)
height = int(img.shape[0] * scale_percent / 100)
dim = (width, height)

def update_canvas():
    global photo
    frame = photo.get_frame()
    img = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(frame))
    panel.configure(image = img)
    panel.image = img    
    top.after(10, update_canvas)

update_canvas()
top.mainloop()
