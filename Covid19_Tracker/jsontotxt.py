import json
import urllib.request as request
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from PIL import ImageTk, Image

HEIGHT = 1250
WIDTH = 1330

def on_configure(event):
    # update scrollregion after starting 'mainloop'
    # when all widgets are in canvas
    canvas.configure(scrollregion=canvas.bbox('all'))

root= tk.Tk()
root.title('Tamil State Result')

#Create Empty window width of 600 and height of 400
canvas = tk.Canvas(root, width = WIDTH, height = HEIGHT, bg = '#343a40', relief = 'raised')
canvas.pack(side=tk.LEFT)

scrollbar = tk.Scrollbar(root, command=canvas.yview)
scrollbar.pack(side=tk.LEFT, fill='y')
canvas.configure(yscrollcommand = scrollbar.set)
canvas.bind('<Configure>', on_configure)

with request.urlopen('https://api.covid19india.org/state_district_wise.json') as response:
    if response.getcode() == 200:
        source = response.read()
        data = json.loads(source)
        result_final = ""
        for state in data['Tamil Nadu']['districtData']:
            state = [state]
            for districts in state:
                activevalue = data['Tamil Nadu']['districtData'][districts]['active']
                confvalue = data['Tamil Nadu']['districtData'][districts]['confirmed']
                recovrvalue = data['Tamil Nadu']['districtData'][districts]['recovered']
                decevalue = data['Tamil Nadu']['districtData'][districts]['deceased']
                result = ('{:15}\t district details \tActive:{:5} \tConfirmed:{:5} \tRecovered:{:5} \tDecreased:{:5}'.format(districts,activevalue,confvalue,recovrvalue,decevalue))
                result_final += ("\n" + result)
    else:
        print("ERROR: Api server unable to reach -- failure")
print(result_final)
background_label = tk.Label(canvas, text=result_final,bg='#343a40', fg='white', font=('helvetica'))
background_label.config(font=("Helvetica", 13, "bold"))
background_label.place(relwidth=1, relheight=1)
root.mainloop()