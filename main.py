import board
import busio as io
import adafruit_mlx90614
from time import sleep
import photo
from tkinter import *
import threading
import PIL.Image
import PIL.ImageTk
import cv2
import time
import imagekit_config
import config
import random

top = Tk()
top.title('COVID TRACER')

name_var = StringVar()
mobile_var = StringVar()
temp_var = StringVar()
imageFrame = None
updater = None


def update_canvas():
    global photo, imageFrame, updater
    frame = photo.get_frame()
    imageFrame = frame
    img = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    panel.configure(image=img)
    panel.image = img
    updater = top.after(10, update_canvas)


def retry():
    retry_button["state"] = "disabled"
    temp_var.set("")
    name_var.set("")
    mobile_var.set("")
    complete_label.grid_forget()
    update_canvas()


retry_button = Button(top, text='Retry/Reset', command=retry,
                      font=('calibre', 10, 'normal'))
retry_button.grid(row=3, column=2, padx=50, pady=15, columnspan=2, sticky=W)
retry_button["state"] = "disabled"
complete_label = Label(top, text="Completed!", font=(
    'calibre', 20, 'normal'), fg="green")
complete_label.grid(row=4, column=1, padx=50, pady=15, columnspan=2)
complete_label.grid_forget()


def after_done():
    retry_button["state"] = "normal"
    complete_label.grid(row=4, column=0, padx=50,
                        pady=15, columnspan=2, sticky=W)


def submit_data():
    top.after_cancel(updater)
    img_name = "./images/capture_{}.png".format(time.time() * 1000)
    cv2.imwrite(img_name, cv2.cvtColor(imageFrame, cv2.COLOR_RGB2BGR))
    print("{} written!".format(img_name))
    url = imagekit_config.upload(img_name)
    after_done()
    values = {
        "name": name_var.get(),
        "mobile": mobile_var.get(),
        "temp": temp_var.get(),
        "image": url
    }
    x = config.mycol.insert_one(values)
    print(values) # Getting the all values for databsase storage


def read_temperature():
    # generate a randum integer between 0 and 100
    # temp = random.randint(0, 100)
    # temp_var.set(str(temp))
    io_port = io.I2C(board.SCL, board.SDA, frequency=100000)
    sensor = adafruit_mlx90614.MLX90614(io_port)

    anbientTemp = "{:.2f}".format(sensor.ambient_temperature)
    targetTemp = "{:.2f}".format(sensor.object_temperature)

    temp_var.set(str(targetTemp))

    sleep(1)

    print(anbientTemp)
    print(targetTemp)


name_label = Label(top, text='Full Name : ', font=('calibre', 10, 'bold'))
name_label.grid(row=0, column=0, sticky=W)
name_entry = Entry(top, textvariable=name_var, font=('calibre', 15, 'normal'))
name_entry.grid(row=0, column=1, padx=20, pady=5, sticky=W+E, columnspan=2)
mobile_label = Label(top, text='Mobile No. : ', font=('calibre', 10, 'bold'))
mobile_label.grid(row=1, column=0, sticky=W)
mobile_entry = Entry(top, textvariable=mobile_var,
                     font=('calibre', 15, 'normal'))
mobile_entry.grid(row=1, column=1, padx=20, pady=5, sticky=W+E, columnspan=2)
temp_label = Label(top, text='Temprature : ', font=('calibre', 10, 'bold'))
temp_label.grid(row=2, column=0, sticky=W)
temp_entry = Entry(top, textvariable=temp_var, font=('calibre', 15, 'normal'), state='readonly')
temp_entry.grid(row=2, column=1, padx=20, pady=5, sticky=W+E, columnspan=2)
capture_button = Button(top, text='Capture image & Submit',
                        command=submit_data, font=('calibre', 10, 'normal'))
capture_button.grid(row=3, column=0, pady=15, sticky=N)
temp_button = Button(top, text='Read Tempareture',
                        command=read_temperature, font=('calibre', 10, 'normal'))
temp_button.grid(row=3, column=1, padx=50, pady=15, sticky=N)
panel = Label(top, image=None)
panel.grid(row=5, column=0, columnspan=3, padx=10, pady=10)

update_canvas()
top.mainloop()
