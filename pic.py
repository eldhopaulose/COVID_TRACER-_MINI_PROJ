import cv2
from PIL import Image, ImageTk


cap= cv2.VideoCapture(0)
img = ''
def img_cap(name):

    global img

    cv2image = cv2.cvtColor(cap.read()[1], cv2.COLOR_BGR2RGB)
    img = Image.fromarray(cv2image)
    print(img)


img_cap('name')