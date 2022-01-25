
import tkinter as tk
from tkinter.tix import Tk
from PIL import Image, ImageTk

import cv2

win= Tk()

# Set the size of the window
win.geometry("700x350")# Create a Label to capture the Video frames
label =tk.Label(win)
label.grid(row=0, column=0)
cap= cv2.VideoCapture(0)

cv2image = cv2.cvtColor(cap.read()[1], cv2.COLOR_BGR2RGB)
img = Image.fromarray(cv2image)

# Convert image to PhotoImage
imgtk = ImageTk.PhotoImage(image=img)
label.imgtk = imgtk
label.configure(image=imgtk)

win.mainloop()

height = 300
width = 300
dimensions = (width, height)
new_image = cv2.resize(image, dimensions, interpolation=cv2.INTER_LINEAR)

