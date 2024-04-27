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


def backMenu():
    try:
        subprocess.Popen(["python", "main.py"])
        sys.exit()      
    except subprocess.CalledProcessError as e:
        print("Error occurred while running the Python file:", e)

def nextPageExpense():
    try:
        subprocess.Popen(["python", "main_ExpenseTracker.py"])
        sys.exit()
    except subprocess.CalledProcessError as e:
        print("Error occurred while running the Python file:", e)

# Entries and Labels
#-----------------------------------------------------------------
expensesTitle_label = tk.Label(root, text="Budgeting Tools Menu", font=("Times New Roman", 38),fg="#D0C395", bg='#9A162B')
expensesTitle_label.grid(row=0, column=0, padx=(150, 5), pady=(50, 10), sticky="w")

expensesTitle_label2 = tk.Label(root, text="Please choose one of the following options:", font=("Times New Roman", 12),fg="#D0C395", bg='#9A162B', anchor="w")
expensesTitle_label2.grid(row=1, column=0, padx=(180, 5), pady=(10, 10), sticky="w")

# Leftsided Options
#-----------------------------------------------------------------


#Expense Tracking
button2_label = tk.Label(root, text="Expense Tracking Tool (Working):", font=("Times New Roman", 16),fg="#D0C395", bg='#9A162B', anchor="e")
button2_label.grid(row=4, column=0, pady=(40, 5), padx=(180, 15), sticky="e")

button2 = tk.Button(root, text="Select", font=("Times New Roman", 15),fg="#D0C395", borderwidth=0, width=130, height=35, compound="center", image=background_image_button, relief="flat", command=nextPageExpense)
button2.grid(row=5, column=0, pady=(10, 5), padx=(180, 15), sticky="e")

button1_label_description = tk.Label(root, text="- Track your daily expenses and keep logs and notes using a \nMachine Learning model and recieve real-time financial \nadvice tailored to your situation using innovative A.I. API's", font=("Times New Roman", 14),fg="#D0C395", bg='#9A162B', anchor="w")
button1_label_description.grid(row=5, column=1, pady=(10, 5), padx=(5, 5), sticky="w")

button_Back = tk.Button(root, text="Main Menu", font=("Times New Roman", 15),fg="#D0C395", borderwidth=0, width=100, height=25, compound="center", image=background_image_button, relief="flat", command=backMenu)
button_Back.place(x=25, y=15)

# Start the main event loop
root.mainloop()