from cProfile import label
import photo
from tkinter import * 
import cv2

top = Tk() 

top.geometry("600x400")  

name_var=StringVar()
mobile_var=StringVar()
temp_var=StringVar()

canvas = Canvas(top, width = 200, height = 200)      
canvas.pack()    
canvas.grid(row=20, column=52, padx=5, pady=5)
name_label = Label(top, text = 'Full Name', font=('calibre',10, 'bold')) 
name_label.grid(row=40,column=50)
name_entry = Entry(top,textvariable = name_var, font=('calibre',10,'normal'))
name_entry.grid(row=40,column=52, padx=5, pady=5)
name=name_var.get()
mobile_label = Label(top, text = 'Mobile No.', font=('calibre',10, 'bold')) 
mobile_label.grid(row=52,column=50)
mobile_entry = Entry(top,textvariable = mobile_var, font=('calibre',10,'normal'))
mobile_entry.grid(row=52,column=52, padx=5, pady=5)
temp_label = Label(top, text = 'Temprature:-', font=('calibre',10, 'bold')) 
temp_label.grid(row=54,column=50)
temp_entry = Entry(top,textvariable = temp_var, font=('calibre',10,'normal'))
temp_entry.grid(row=54,column=52)

print(name)

photo.image_cap('2022')


img = cv2.imread('opencv_frame_{}.png'.format('eldho1'), cv2.IMREAD_COLOR)
scale_percent = 20 # percent of original size
width = int(img.shape[1] * scale_percent / 100)
height = int(img.shape[0] * scale_percent / 100)
dim = (width, height)
  
# resize image
resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
cv2.imwrite('D:/opencv_frame_{}.png'.format('eldho1'),resized) 
img = PhotoImage(file='D:/opencv_frame_{}.png'.format('eldho1'))   
canvas.create_image(20,20, anchor=NW, image=img)   

print(photo.img_name)
top.mainloop()