import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from PIL import ImageTk, Image

HEIGHT = 355
WIDTH = 535

root= tk.Tk()
root.title('BASE64 - Converter')

#Create Empty window width of 600 and height of 400
canvas = tk.Canvas(root, width = WIDTH, height = HEIGHT, bg = '#ffffff', relief = 'raised')
canvas.pack()

#Creating background image
#background_image = tk.PhotoImage(file='ssh.jpg')
background_image = ImageTk.PhotoImage(Image.open('ssh.jpg'))
background_label = tk.Label(root, text='BASE64 Decode and Encode - Converter', image=background_image)
background_label.config(font=("Helvetica", 20, "bold"))
#canvas.create_image(30, 30, image=background_label)
background_label.place(relwidth=1, relheight=1)

def test_function():
    print("Button Clicked!")
frame = tk.Frame(root, bg='#00ffff' ,bd=4)
frame.place(relx=0.5, rely=0.1, relwidth=0.70, relheight=0.09, anchor='n')
entry = tk.Entry(frame, font=40)
entry.place(relwidth=1,relheight=1)
button = tk.Button(frame,text="base64-encode", font=5,command=test_function)
button.place(relx=0.7,relheight=1,relwidth=0.3)

def exitApplication():
    MsgBox = tk.messagebox.askquestion ('Exit Application','Are you sure you want to exit the application',icon = 'warning')
    if MsgBox == 'yes':
       root.destroy()
exitButton = tk.Button (root, text='       exit      ',command=exitApplication, bg='#993333', fg='white', font=('helvetica', 10, 'bold'))
canvas.create_window(275, 340, window=exitButton)


root.mainloop()