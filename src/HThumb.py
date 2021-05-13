from tkinter import *
from tkinter import filedialog, messagebox, ttk
import os
import cv2
import numpy as np
import shlex
import subprocess
import time

root = Tk()

root.attributes('-toolwindow', True)
root.resizable(False, False)
root.title("HThumb by @vladlearns")
root.geometry("500x300")


def start():
    path = filedialog.askdirectory();
    for root, dirs, files in os.walk(f'{path}'):
         for file in files:
            if file.endswith(".exr") == True:
                filePath = os.path.join(os.path.abspath(root), file).replace("\\", "/")
                im = cv2.imread(filePath, -1)
                im=im*65535
                im[im>65535]=65535
                im=np.uint16(im)
                cv2.imwrite(filePath + '.png', im)
            
            if file.endswith(".hdr") == True:
                filePath = os.path.join(os.path.abspath(root), file).replace("\\", "/")
                image = cv2.imread(filePath)
                cv2.imwrite(filePath + '.png', image, [int(cv2.IMWRITE_JPEG_QUALITY), 100])
                
            

    messagebox.showinfo("Info", "Your files are ready" )



button = Button(root, text="Select Folder", command=start)
button.place(x=0, y=0, relx=0.5, rely=0.5, anchor=CENTER)



root.mainloop()