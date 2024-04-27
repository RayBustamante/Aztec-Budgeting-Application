import tkinter as tk
from tkinter import messagebox
import subprocess
import sys
import csv
import os

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

#-----------------------------------------------------------------
# by Ramon C Bustamante
#-----------------------------------------------------------------


# Create Personal Information Window
#-----------------------------------------------------------------
root = tk.Tk()
root.title("Account Form")
root.geometry("1274x714")

# Create Background Image
#-----------------------------------------------------------------
background_image2 = tk.PhotoImage(file="Aztec_Menu_Background_Empty.png")
background_label = tk.Label(root, image=background_image2)
background_label.place(relwidth=1, relheight=1)

background_image_button = tk.PhotoImage(file="button_background_red.png")
  

# Entries and Labels
#-----------------------------------------------------------------
expensesTitle_label = tk.Label(root, text="Financial Advice", font=("Times New Roman", 28), bg='#9A162B')
expensesTitle_label.grid(row=0, column=0, padx=(150, 5), pady=(50, 10), sticky="w")

expensesTitle_label2 = tk.Label(root, text="Pick the question options that best describes your needs. \nAnd then enter your desired financial advice.", font=("Times New Roman", 11), bg='#9A162B', anchor="w")
expensesTitle_label2.grid(row=1, column=0, padx=(180, 5), pady=(10, 10), sticky="w")

# Leftsided Options
#-----------------------------------------------------------------

# Start the main event loop
root.mainloop()