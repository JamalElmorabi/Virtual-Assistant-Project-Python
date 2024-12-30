from tkinter import *
from PIL import Image, ImageTk
import speech_to_text
import action
import os
import sys

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    
    full_path = os.path.join(base_path, relative_path)
    print(f"Full path to image: {full_path}")
    return full_path

def center_window(root, width, height):
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = int((screen_width / 2) - (width / 2))
    y = int((screen_height / 2) - (height / 2))
    root.geometry(f"{width}x{height}+{x}+{y}")

root = Tk()
root.title("Virtual Assistant")
app_width, app_height = 550, 675
center_window(root, app_width, app_height)
root.resizable(False, False)
root.config(bg="#6F8FAF")

def ask():
    user_val = speech_to_text.speech_to_text()
    bot_val = action.action(user_val)
    text.insert(END, 'User ---> ' + user_val+"\n")
    if bot_val != None:
        text.insert(END, "BOT ---> "+str(bot_val)+"\n")
    if bot_val == "Ok sir, shutting down":
        root.destroy()

def delete():
    text.delete('1.0', "end")

def send():
    send = entry.get()
    bot = action.action(send)
    text.insert(END, 'User ---> ' + send+"\n")
    if bot != None:
        text.insert(END, "BOT ---> "+str(bot)+"\n")
    if bot == "Ok sir, shutting down":
        root.destroy()


frame = Frame(root, bg="#6F8FAF")
frame.pack(pady=20)

title_label = Label(frame, text="Virtual Assistant", font=("Arial", 16, "bold"), bg="#356696", fg="white", padx=20, pady=10)
title_label.pack()

try:
    image_path = resource_path('image/assistant.jpg')
    image = ImageTk.PhotoImage(Image.open(image_path).resize((240, 240)))
    image_label = Label(frame, image=image, bg="#6F8FAF")
    image_label.pack(pady=10)
except Exception as e:
    image_label = Label(frame, text="Image Not Found", bg="#6F8FAF", fg="red")
    image_label.pack(pady=10)

text_frame = Frame(root, bg="#6F8FAF")
text_frame.pack(pady=10)
text = Text(text_frame, font=('Arial', 10), bg="#356696", fg="black", wrap=WORD)
text.pack()
text.config(width=50, height=6)

entry = Entry(root, font=("Arial", 12), justify=CENTER, bg="#FFFFFF", fg="black")
entry.pack(pady=10)
entry.config(width=40)

button_frame = Frame(root, bg="#6F8FAF")
button_frame.pack(pady=20)

Button(button_frame, text="ASK", bg="#356696", fg="white", font=("Arial", 12, "bold"),
       pady=10, padx=20, borderwidth=3, relief=SOLID, command=ask).grid(row=0, column=0, padx=10)

Button(button_frame, text="DELETE", bg="#356696", fg="white", font=("Arial", 12, "bold"),
       pady=10, padx=20, borderwidth=3, relief=SOLID, command=delete).grid(row=0, column=1, padx=10)

Button(button_frame, text="SEND", bg="#356696", fg="white", font=("Arial", 12, "bold"),
       pady=10, padx=20, borderwidth=3, relief=SOLID, command=send).grid(row=0, column=2, padx=10)

root.mainloop()