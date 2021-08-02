from tkinter import *
import cv2


master4 = Tk()


cam = cv2.VideoCapture(0)

cv2.namedWindow("Face ID")

img_counter = 0

while True:
    ret, frame = cam.read()
    if not ret:
        print("failed to grab frame")
        break
    cv2.imshow("Face ID", frame)

    k = cv2.waitKey(1)
    if k%256 == 27:
        # ESC pressed
        print("Escape hit, closing...")
        break
    elif k%256 == 32:
        # SPACE pressed
        img_name = "captured_face{}.png".format(img_counter)
        cv2.imwrite(img_name, frame)
        print("{} written!".format(img_name))
        img_counter += 1
        
cam.release()

master4.destroy()
cv2.destroyAllWindows()
execfile('UserLogin.py')