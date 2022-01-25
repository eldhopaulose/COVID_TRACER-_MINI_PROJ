# from tkinter import * 
# from PIL import Image, ImageTk
# from io import BytesIO

# import photo
# top = Tk() 

# URL = photo.i
# print(photo.i)
# raw_data = URL.read()
# URL.close()

# top.geometry("400x250")  
# im = Image.open(BytesIO(raw_data))
# phot = ImageTk.PhotoImage(im)
# photo.image_cap('eldho') 
# top.mainloop() 


import photo
from tkinter import * 
import cv2

top = Tk() 

top.geometry("400x250")  

canvas = Canvas(top, width = 100, height = 100)      
canvas.pack()      

img = cv2.imread('opencv_frame_{}.png'.format('eldho'), cv2.IMREAD_COLOR)
scale_percent = 10 # percent of original size
width = int(img.shape[1] * scale_percent / 100)
height = int(img.shape[0] * scale_percent / 100)
dim = (width, height)
  
# resize image
resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
cv2.imwrite('D:/opencv_frame_{}.png'.format('eldho'),resized) 
img = PhotoImage(file='D:/opencv_frame_{}.png'.format('eldho'))   
canvas.create_image(20,20, anchor=NW, image=img)     

photo.image_cap('eldho')
print(photo.img_name)
top.mainloop()