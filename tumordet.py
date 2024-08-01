# -*- coding: utf-8 -*-
"""
Created on Sun Jul 28 23:08:09 2024

@author: pkpat
"""
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from PIL import Image, ImageTk

# Function to open a file dialog and select a file
def select_file():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp *.tiff")])
    if file_path:
        file_label.config(text=file_path)
        img = Image.open(file_path)
        img = img.resize((300, 300))  # Resize the image to fit the display area
        img_tk = ImageTk.PhotoImage(img)
        image_label.config(image=img_tk)
        image_label.image = img_tk  # Keep a reference to avoid garbage collection

# Function to display about information
def show_about():
    messagebox.showinfo("About", "Brain Tumor Detection App\nVersion 1.0\nDeveloped by Students of RIT")

# Main application window
root = tk.Tk()
root.title("Brain Tumor Detection")
root.geometry("700x700")
root.configure(bg='#e0e0e0')

# Style configurations
style = ttk.Style()
style.configure('TFrame', background='#e0e0e0')
style.configure('TLabel', background='#e0e0e0', font=('Helvetica', 12))
style.configure('TButton', background='#007BFF', foreground='white', font=('Helvetica', 12))
style.map('TButton', background=[('active', '#0056b3')])

# Frame for the title
title_frame = ttk.Frame(root)
title_frame.grid(row=0, column=0, padx=20, pady=20, sticky="ew")

title_label = ttk.Label(title_frame, text="Brain Tumor Detection", font=("Helvetica", 24, "bold"), background='#e0e0e0')
title_label.pack()

# Frame for file selection
file_frame = ttk.Frame(root)
file_frame.grid(row=1, column=0, padx=20, pady=10, sticky="ew")

file_button = ttk.Button(file_frame, text="Select MRI Image", command=select_file)
file_button.grid(row=0, column=0, padx=5, pady=5)

file_label = ttk.Label(file_frame, text="No file selected", width=50, background='#f0f0f0', relief="sunken")
file_label.grid(row=0, column=1, padx=5, pady=5)

# Frame for displaying results
result_frame = ttk.Frame(root)
result_frame.grid(row=2, column=0, padx=20, pady=20, sticky="ew")

result_label = ttk.Label(result_frame, text="Prediction: N/A", font=("Helvetica", 14), background='#e0e0e0')
result_label.pack()

# Frame for image display
image_frame = ttk.Frame(root)
image_frame.grid(row=3, column=0, padx=20, pady=20, sticky="ew")

image_label = ttk.Label(image_frame)
image_label.pack()

# Make the columns expand proportionally
root.grid_columnconfigure(0, weight=1)

# Menu
menu = tk.Menu(root)
root.config(menu=menu)

file_menu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Select File", command=select_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

help_menu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="Help", menu=help_menu)
help_menu.add_command(label="About", command=show_about)

# Run the application
root.mainloop()
