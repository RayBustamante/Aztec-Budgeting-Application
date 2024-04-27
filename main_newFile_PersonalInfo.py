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


fullName = None
age = 0
major = None
year = None
incomeData = None

# Functions
#-----------------------------------------------------------------
def validate_input(value):
  # Checks to make sure that the input value can only be a two-digit number
  if len(value) <= 2 and (value.isdigit() or (value.startswith('-') and value[1:].isdigit())):
    return True
  elif value == "":
    return True
  else:
    return False

def checkAllEntry():

  # Checks to make sure that all the entry boxes are filled out
  global fullName
  global age
  global major
  global year

  fullName = ""
  age = 0
  major = ""
  year = ""
  
  fullName = entry_Name.get()
  age = entry_Age.get()
  major = entry_Major.get()
  year = selected_Var.get()

  if fullName == "" or age == "" or major == "":
    messagebox.showerror("Incomplete!", "One or more of the entries are empty!")
  else:
    saveAccount()


def saveAccount():
  global fullName
  global age
  global major
  global year 
  global incomeData
  
  filename = "studentUser_newFile.csv"
  data = []
  
  with open(filename, mode='r', newline='') as file:
      reader = csv.reader(file)
      for row in reader:
          data.append(row)
            

  # Update the value at the specified location
  
  data[1][18] = fullName
  data[1][1] = age
  data[1][3] = year
  data[1][4] = major

  # Write the updated data back to the CSV file
  with open(filename, mode='w', newline='') as file:
      writer = csv.writer(file)
      writer.writerows(data)
  displayText = ("Your account has been successfuly created! "
    + " " +
   "\n \n Student Name: " + str(fullName) + 
   "\n Age: " + str(age) + " "
   "\n School Year: " + str(year) + " "
   "\n Major: " + str(major) + " ")
  messagebox.showinfo("Complete!", displayText)

  button1.config(text="Re-Submit")

  buttonNext = tk.Button(root, text="Next", font=("Times New Roman", 15),fg="#D0C395", borderwidth=0, width=130, height=35, compound="center", image=background_image_button, relief="flat", command=nextPage)
  buttonNext.grid(row=6, column=4, columnspan=2, padx=(255, 20), pady=(180,15))

def nextPage():
  try:
    subprocess.Popen(["python", "main_newFile_Expenses.py"])
    sys.exit()
  except subprocess.CalledProcessError as e:
    print("Error occurred while running the Python file:", e)

  
# Pay and Hourly Inputs/Labels
#-----------------------------------------------------------------
Title_label = tk.Label(root, text="Account Creation", font=("Times New Roman", 38),fg="#D0C395", bg='#9A162B')
Title_label.grid(row=0, column=0, padx=(150, 5), columnspan=2, pady=(50, 10))

Title_label2 = tk.Label(root, text="Please fill the following personal information:", font=("Times New Roman", 15),fg="#D0C395", bg='#9A162B')
Title_label2.grid(row=1, column=0, padx=(180, 5), columnspan=2, pady=(10, 10))

# Left-side Labels and Entry
#-----------------------------------------------------------------

# Full Name Entry
label_Name = tk.Label(root, text="Full Name:", font=("Times New Roman", 12),fg="#D0C395", bg='#9A162B')
label_Name.grid(row=2, column=0, pady=(80, 10), padx=(150, 5), sticky="e")
entry_Name = tk.Entry(root, font=("Times New Roman", 12))
entry_Name.grid(row=2, column=1, pady=(80, 10), padx=(30, 5), sticky="w")

# Age Entry
#   Wraps the callback so it can be called when the user types
validate = root.register(validate_input)

label_Age = tk.Label(root, text="Age:", font=("Times New Roman", 12),fg="#D0C395", bg='#9A162B')
label_Age.grid(row=3, column=0, pady=(20, 10), padx=(150, 5), sticky="e")
entry_Age = tk.Entry(root, font=("Times New Roman", 12), validate="key", validatecommand=(validate, '%P'))
entry_Age.grid(row=3, column=1, pady=10, padx=(30, 5), sticky="w")

# Major Degree
label_Major = tk.Label(root, text="College Major:", font=("Times New Roman", 12),fg="#D0C395", bg='#9A162B')
label_Major.grid(row=4, column=0, pady=(10, 10), padx=(150, 5), sticky="e")
entry_Major = tk.Entry(root, font=("Times New Roman", 12))
entry_Major.grid(row=4, column=1, pady=10, padx=(30, 5), sticky="w")

# Define a global variable to store the selected option
global_selected_option = tk.StringVar()
# School year label
label_Year = tk.Label(root, text="School Year:", font=("Times New Roman", 12),fg="#D0C395", bg='#9A162B')
label_Year.grid(row=5, column=0, pady=(10, 10), padx=(150, 5), sticky="e")

# Options for the dropdown menu
year_Options = ["Freshman", "Sophomore", "Junior", "Senior"]

selected_Var = tk.StringVar(root)
# Set a default value for the dropdown menu
selected_Var.set(year_Options[0])

# Create the dropdown menu
dropdown_Year = tk.OptionMenu(root, selected_Var, *year_Options)
dropdown_Year.config(font=("Times New Roman", 12))
dropdown_Year.grid(row=5, column=1, pady=10, padx=(30, 5), sticky="w")

# Next Button
#-----------------------------------------------------------------
button1 = tk.Button(root, text="Submit", font=("Times New Roman", 15),fg="#D0C395", borderwidth=0, width=130, height=35, compound="center", 
                    image=background_image_button, relief="flat", command=checkAllEntry)
button1.grid(row=6, column=1, columnspan=2, padx=(55, 20), pady=(180,15))

# Start the main event loop
root.mainloop()