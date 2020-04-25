import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from PIL import ImageTk, Image
import base64

HEIGHT = 355
WIDTH = 535

root= tk.Tk()
root.title('BASE64 - Converter')

#Create Empty window width of 600 and height of 400
canvas = tk.Canvas(root, width = WIDTH, height = HEIGHT, bg = '#e6ffff', relief = 'raised')
canvas.pack()

#Creating background image
#background_image = tk.PhotoImage(file='ssh.jpg')
background_image = ImageTk.PhotoImage(Image.open('ssh.jpg'))
background_label = tk.Label(root, text='BASE64 Decode and Encode - Converter', image=background_image)
background_label.config(font=("Helvetica", 20, "bold"))
#canvas.create_image(30, 30, image=background_label)
background_label.place(relwidth=1, relheight=1)

def encode_function(entry):
    print("This is the entry:", entry)
    message = entry
    message_bytes = message.encode('ascii')
    base64_bytes = base64.b64encode(message_bytes)
    base64_message = base64_bytes.decode('ascii')
    print(base64_message)
    label['text'] = base64_message

def decode_function(entry):
    print("This is the entry:", entry)
    base64_message = entry
    base64_bytes = base64_message.encode('ascii')
    message_bytes = base64.b64decode(base64_bytes)
    message = message_bytes.decode('ascii')
#    message_bytes = message.encode('ascii')
#    base64_bytes = base64.b64encode(message_bytes)
#    base64_message = base64_bytes.decode('ascii')
    print(message)
    label1['text'] = message
    
# Encoding from text to base64
frame = tk.Frame(root, bg='#00ffff' ,bd=4)
frame.place(relx=0.5, rely=0.1, relwidth=0.70, relheight=0.09, anchor='n')

entry = tk.Entry(frame, font=40)
entry.place(relwidth=1,relheight=1)

button = tk.Button(frame, text="base64-encode", font=5, command=lambda: encode_function(entry.get()))
button.place(relx=0.7,relheight=1,relwidth=0.3)

lower_frame = tk.Frame(root, bg='#00ffff' ,bd=4)
lower_frame.place(relx=0.5, rely=0.22, relwidth=0.70, relheight=0.20, anchor='n')

label = tk.Label(lower_frame, text="Result: ", font=40)
label.place(relwidth=1,relheight=1)



# Decoding from base64 to text
frame1 = tk.Frame(root, bg='#00ffff' ,bd=4)
frame1.place(relx=0.5, rely=1.1, relwidth=0.70, relheight=1.09, anchor='n')

entry1 = tk.Entry(frame1, font=40)
entry1.place(relwidth=1,relheight=1)

button1 = tk.Button(frame1, text="base64-decode", font=5, command=lambda: decode_function(entry.get()))
button1.place(relx=0.7,relheight=1,relwidth=0.3)

lower_frame1 = tk.Frame(root, bg='#00ffff' ,bd=4)
lower_frame.place(relx=0.5, rely=0.22, relwidth=0.70, relheight=0.20, anchor='n')

label1 = tk.Label(lower_frame1, text="Result: ", font=40)
label1.place(relwidth=1,relheight=1)

def exitApplication():
    MsgBox = tk.messagebox.askquestion ('Exit Application','Are you sure you want to exit the application',icon = 'warning')
    if MsgBox == 'yes':
       root.destroy()
exitButton = tk.Button (root, text='       exit      ',command=exitApplication, bg='#993333', fg='white', font=('helvetica', 10, 'bold'))
canvas.create_window(275, 340, window=exitButton)


root.mainloop()