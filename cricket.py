import tkinter 
import cv2 
import PIL.Image, PIL.ImageTk  #its pillow module to run jpg file
from functools import partial
import threading
import time
import imutils #imutils for resizeing image using opencv 

stream = cv2.VideoCapture("clip.mp4")
flag = True
def play(speed):
    global flag
    print(f"You clicked on play. Speed is {speed}")

    # Play the video in reverse mode
    frame1 = stream.get(cv2.CAP_PROP_POS_FRAMES)
    stream.set(cv2.CAP_PROP_POS_FRAMES, frame1 + speed)

    grabbed, frame = stream.read()
    if not grabbed:
        exit()
    frame = imutils.resize(frame, width=SET_WIDTH, height=SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0,0, image=frame, anchor=tkinter.NW)
    if flag:
        canvas.create_text(134, 26, fill="black", font="Times 26 bold", text="Decision Pending")
    flag = not flag
    

def pending(decision):
    frame = cv2.cvtColor(cv2.imread("pending.jpg"), cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame, width=SET_WIDTH, height=SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0,0, image=frame, anchor=tkinter.NW)
   
    time.sleep(0.5)             #time between two image change

    
    frame = cv2.cvtColor(cv2.imread("sponsor.jpg"), cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame, width=SET_WIDTH, height=SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0,0, image=frame, anchor=tkinter.NW)

   
    time.sleep(1)
    
    #out or not out decision logic is here

    if decision == 'out':
        decisionImg = "out.jpg"
    else:
        decisionImg = "not out.jpg"
    frame = cv2.cvtColor(cv2.imread(decisionImg), cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame, width=SET_WIDTH, height=SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0,0, image=frame, anchor=tkinter.NW)


def out():
    thread = threading.Thread(target=pending, args=("out",))
    thread.daemon = 1
    thread.start()
    print("Player is out")


def not_out():
    thread = threading.Thread(target=pending, args=("not out",))
    thread.daemon = 1
    thread.start()
    print("Player is not out")


SET_WIDTH = 900
SET_HEIGHT = 500

# Tkinter gui 
window = tkinter.Tk()
window.title("LOCAL DRS BY FROSTING FIRE")
cv_img = cv2.cvtColor(cv2.imread("welcome23.jpg"), cv2.COLOR_BGR2RGB)
canvas = tkinter.Canvas(window, width=SET_WIDTH, height=SET_HEIGHT)
photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(cv_img))
image_on_canvas = canvas.create_image(0, 20, ancho=tkinter.NW, image=photo)
canvas.pack()

# Buttons to control
btn = tkinter.Button(window, text="<<<<< Previous (fast)",font="comicsansms 13 bold", width=50,pady=5,padx=5,bg="blue", command=partial(play, -25))
btn.pack()

btn = tkinter.Button(window, text="<<<<< Previous (slow)",font="comicsansms 13 bold", width=50,pady=5,padx=5,bg="yellow", command=partial(play, -2))
btn.pack()

btn = tkinter.Button(window, text="Next (slow) >>>>>",font="comicsansms 13 bold", width=50,pady=5,padx=5,bg="blue",  command=partial(play, 2))
btn.pack()

btn = tkinter.Button(window, text="Next (fast) >>>>>",font="comicsansms 13 bold", width=50,pady=5,padx=5,bg="yellow",  command=partial(play, 25))
btn.pack()

btn = tkinter.Button(window, text="Give Out",font="comicsansms 13 bold", width=50,pady=5,padx=5,bg="red", command=out)
btn.pack()

btn = tkinter.Button(window, text="Give Not Out",font="comicsansms 13 bold", width=50,pady=5,padx=5,bg="green", command=not_out)
btn.pack()
window.mainloop()
