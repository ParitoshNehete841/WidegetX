import numpy as np
import pyautogui
import tkinter as tk
from tkinter import filedialog
from PIL import ImageGrab
import cv2
import os
import time

root = tk.Tk()
root.resizable(False,False)
canvas = tk.Canvas(root, width=250,height=250, bg='gray',)
canvas.pack()
title=tk.Label(text=" WidgetX",font=("times new roman",25),bg='black',fg='white',anchor='w').place(x=0,y=0,relwidth=1)
SCREEN_SIZE = (1920, 1080)



def takeScreenshot():
    myScreenshot = pyautogui.screenshot()
    path = filedialog.asksaveasfilename(defaultextension='.png')
    myScreenshot.save(path)
    PAUSE=5


def screenrecording():

    # display screen resolution, get it from your OS settings
    SCREEN_SIZE = (1920, 1080)
    # define the codec
    fourcc = cv2.VideoWriter_fourcc(*"XVID")
    # create the video write object
    out = cv2.VideoWriter("output.avi", fourcc, 20.0, (SCREEN_SIZE))

    while True:
        # make a screenshot
        img = pyautogui.screenshot()
        # img = pyautogui.screenshot(region=(0, 0, 300, 400))
        # convert these pixels to a proper numpy array to work with OpenCV
        frame = np.array(img)
        # convert colors from BGR to RGB
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        # write the frame
        out.write(frame)
        # show the frame
        cv2.imshow("screenshot", frame)
        # if the user clicks q, it exits
        if cv2.waitKey(1) == ord("X"):
            break

    # make sure everything is closed when exited
    cv2.destroyAllWindows()
    out.release()


def takeaphoto():
    webcam= cv2.VideoCapture(0)
    cv2.waitKey(5)
    time.sleep(5)
    check, frame =webcam.read()
    cv2.waitKey(5)
    path= filedialog.asksaveasfilename(defaultextension='.png')
    cv2.imwrite(path,img=frame)
    frame.save()
    PAUSE = 5



def startrecording():
    # vid = cv2.VideoCapture(0)
    #
    # while (True):
    #
    #     # Capture the video frame
    #     # by frame
    #     ret, frame = vid.read()
    #
    #     # Display the resulting frame
    #     cv2.imshow('frame', frame)
    #
    #
    #     # the 'q' button is set as the
    #     # quitting button you may use any
    #     # desired button of your choice
    #     if cv2.waitKey(1) & 0xFF == ord('q'):
    #         break
    #
    #
    # # After the loop release the cap object
    # vid.release()
    # path = filedialog.asksaveasfilename(defaultextension='.mp4')
    # frame.save(path)
    # # Destroy all the windows
    # cv2.destroyAllWindows()
    import cv2

    # Capture video from webcam
    vid_capture = cv2.VideoCapture(0)
    vid_cod = cv2.VideoWriter_fourcc(*'XVID')
    output = cv2.VideoWriter("videos/cam_video.mp4", vid_cod, 20.0, (640, 480))


    while (True):
        # Capture each frame of webcam video
        ret, frame = vid_capture.read()
        cv2.imshow("My cam video", frame)
        output1=output.write(frame)
        # Close and break the loop after pressing "x" key
        if cv2.waitKey(1) & 0XFF == ord('X'):
            break


    # close the already opened camera
    vid_capture.release()
    # close the already opened file
    output.release()
    # path = filedialog.asksaveasfilename(defaultextension='.mp4')
    # output.release.save(path)
    # close the window and de-allocate any associated memory usage
    cv2.destroyAllWindows()



def storage():
    target="F:\Screenshot" #storing directory
    os.startfile(target)

btn1 = tk.Button(text='Take SS',command=takeScreenshot,bg='white',fg='black',anchor='center',font=5)
canvas.create_window(125,70,window=btn1)

btn2= tk.Button(text='Start Screen Recording',command=screenrecording,bg='white',fg='black',font=5)
canvas.create_window(125,110,window=btn2)

btn3= tk.Button(text='Take Snap',bg='white',command=takeaphoto,fg='black',font=5)
canvas.create_window(125,150,window=btn3)

btn4= tk.Button(text='Start Recording',command=startrecording,bg='white',fg='black',font=5)
canvas.create_window(125,190,window=btn4)

btn5= tk.Button(text='Storage',bg='white',command=storage,fg='black',font=5)
canvas.create_window(125,230,window=btn5)

root.mainloop()




