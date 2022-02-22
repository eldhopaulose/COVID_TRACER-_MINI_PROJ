from unicodedata import name
import cv2

img_name = ''

def image_cap(name):
    cv2.namedWindow("test")
    cam = cv2.VideoCapture(0)
    global img_name
    img_counter = 0

    while True:
        ret, frame = cam.read()
        if not ret:
            print("failed to grab frame")
            break
        cv2.imshow("test", frame)

        k = cv2.waitKey(1)
        if k % 256 == 27:
            # ESC pressed
            print("Escape hit, closing...")
            break
        elif k % 256 == 32:
            # SPACE pressed
            img_name = "opencv_frame_{}.png".format(name)
            print(img_name)
            cv2.imwrite(img_name, frame)
            print("{} written!".format(img_name))
            img_counter += 1

    cam.release()

cam = cv2.VideoCapture(0)
def get_frame():
    # img = cv2.namedWindow("test")
    ret, frame = cam.read()
    if not ret:
        return None
    return cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

def release():
    cam.release()
    cv2.destroyAllWindows()