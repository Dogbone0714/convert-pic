import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image

root= tk.Tk()
root.title("Pic Convert By HHK")
canvas1 = tk.Canvas(root, width=300, height=330, bg='lightsteelblue2', relief='raised')
canvas1.pack()



label1 = tk.Label(root, text='Pic Convert Tool', bg='lightsteelblue2')
label1.config(font=('helvetica', 20))
canvas1.create_window(150, 50, window=label1)


def getPic():
    global im1

    import_file_path = filedialog.askopenfilename()
    im1 = Image.open(import_file_path)


browseButton_Pic = tk.Button(text="    Import   PNG   File   ", command=getPic, bg='royalblue', fg='white',
                             font=('helvetica', 12, 'bold'))
canvas1.create_window(150, 120, window=browseButton_Pic)

def convertToJPG():
    global im1

    export_file_path = filedialog.asksaveasfilename(defaultextension='.jpg')
    im1.save(export_file_path)


saveAsButton_JPG = tk.Button(text=' Convert  Pic To JPG ', command=convertToJPG, bg='purple', fg='white',
                             font=('helvetica', 12, 'bold'))
canvas1.create_window(150, 180, window=saveAsButton_JPG)

def convertToPNG():
    global im1

    export_file_path = filedialog.asksaveasfilename(defaultextension='.png')
    im1.save(export_file_path)


saveAsButton_PNG = tk.Button(text=' Convert  Pic To PNG ', command=convertToPNG, bg='red2', fg='white',
                             font=('helvetica', 12, 'bold'))
canvas1.create_window(150, 240, window=saveAsButton_PNG)

def convertToico():
    global im1

    export_file_path = filedialog.asksaveasfilename(defaultextension='.ico')
    im1.save(export_file_path)


saveAsButton_ico = tk.Button(text='  Convert   Pic To  ico  ', command=convertToico, bg='green3', fg='white',
                             font=('helvetica', 12, 'bold'))
canvas1.create_window(150, 300, window=saveAsButton_ico)

root.mainloop()

