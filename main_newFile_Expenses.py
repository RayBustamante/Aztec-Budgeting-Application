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

#initialized global variables
data = []
filename = "studentUser_newFile.csv"
incomeData = None

# Retrieves data
with open(filename, mode='r', newline='') as file:
    reader = csv.reader(file)
    for row in reader:
        data.append(row)



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


def validate_input(value):
  # Checks to make sure that the value can only be a two-digit number
  if len(value) <= 5 and (value.isdigit() or (value.startswith('-') and value[1:].isdigit())):
    return True
  elif value == "":
    return True
  else:
    return False


def calculateExpenses():
  global data
  global filename

  housingExpenses = entry_left_Housing.get()
  foodExpenses = entry_left_Food.get()
  transportExpenses = entry_left_Transport.get()
  suppliesExpenses = entry_left_SchoolSupplies.get()
  
  entertainExpenses = entry_right_Entertainment.get()
  careExpenses = entry_right_Care.get()
  techExpenses = entry_right_Technology.get()
  miscExpenses = entry_right_Miscellaneous.get()

  #check if it is empty
  if (housingExpenses == "" or foodExpenses == "" or transportExpenses == "" or suppliesExpenses == "" or entertainExpenses == "" or careExpenses == "" or techExpenses == "" or miscExpenses == ""):
    messagebox.showerror("Error", "Please fill in all expense fields.")
    return

  #add up
  total_expenses = int(housingExpenses) + int(foodExpenses) + int(transportExpenses) + int(suppliesExpenses) + int(entertainExpenses) + int(careExpenses) + int(techExpenses) + int(miscExpenses)

  # send an errors message and return back
  if(total_expenses > int(data[1][5])):

    incomeData = data[1][5]
    messagebox.showerror("Error", ("You have exceeded your monthly budget of $" + str(incomeData) + "\n\nYour current expenses is $" + str(total_expenses - int(incomeData)) + " over your budget. \n\nPlease make adjustments.")  )
    label_left_expenseCalculator.config(text=("Monthly Income/Expense Limit:  $" + str(data[1][5])))
    return

  #if sucess start saving to csv
  incomeData = data[1][5]
  data[1][8] = housingExpenses
  data[1][9] = foodExpenses
  data[1][10] = transportExpenses
  data[1][11] = suppliesExpenses

  data[1][12] = entertainExpenses
  data[1][13] = careExpenses
  data[1][14] = techExpenses
  data[1][16] = miscExpenses
  
  
  savingIncome = int(incomeData) - int(total_expenses)
  savingPercentage = int(savingIncome)/int(incomeData) * 100
  roundPercentage = round(savingPercentage, 2)


  messagebox.showinfo("Success", ("Your expenses have been calculated successfully." + " \n\nYou are $" + str(savingIncome) + " below your expense,  accounting for an ") + str(roundPercentage) + "% in savings to your monthly income."  )



  label_left_expenseCalculator.config(text=("Monthly Income/Expense Limit:  $" + str(data[1][5]) + "\nTotal Savings: $" + str(int(incomeData) - int(total_expenses))))

  data[1][19] = (int(incomeData) - int(total_expenses))

  with open(filename, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)

  # Buttons
  button1.configure(text="Re-Submit")
  buttonNext = tk.Button(root, text="Next", font=("Times New Roman", 15),fg="#D0C395", borderwidth=0, width=130, height=35, compound="center", 
                      image=background_image_button, relief="flat", command=nextPage)
  buttonNext.grid(row=10, column=3, pady=(45, 5), padx=(5, 5), sticky="w")

def nextPage():
  try:
    subprocess.Popen(["python", "main_newFile_Menu.py"])
    sys.exit()
  except subprocess.CalledProcessError as e:
    print("Error occurred while running the Python file:", e)

# Entries and Labels
#-----------------------------------------------------------------
expensesTitle_label = tk.Label(root, text="Personal Expenses", font=("Times New Roman", 38),fg="#D0C395", bg='#9A162B')
expensesTitle_label.grid(row=0, column=0, padx=(150, 5), columnspan=2, pady=(50, 10), sticky="w")

expensesTitle_label2 = tk.Label(root, text="In the following entries, please fill in all of the \n expenses you pay on a monthly bases based on the categorization featured:",fg="#D0C395", font=("Times New Roman", 12), bg='#9A162B', anchor="w")
expensesTitle_label2.grid(row=1, column=0, padx=(180, 5), columnspan=2, pady=(10, 10), sticky="w")

# Leftsided Expenses and Entries
#-----------------------------------------------------------------

# Housing Entries
label_left_Housing = tk.Label(root, text="Housing:", font=("Times New Roman", 12),fg="#D0C395", bg='#9A162B')
label_left_Housing.grid(row=2, column=0, pady=(80, 5), padx=(130, 5), sticky="e")

validate = root.register(validate_input)

entry_left_Housing = tk.Entry(root, font=("Times New Roman", 12), validate="key", validatecommand=(validate, '%P'))
entry_left_Housing.grid(row=2, column=1, pady=(80, 5), padx=(30, 5), sticky="w")
label_left_HousingDesc = tk.Label(root, text="* Expenses such as mortage, rent and utilities:", font=("Times New Roman", 10),fg="#D0C395", bg='#9A162B')
label_left_HousingDesc.grid(row=3, column=1, pady=(0, 5), sticky="w")

# Food Entries
label_left_Food = tk.Label(root, text="Food:", font=("Times New Roman", 12),fg="#D0C395", bg='#9A162B')
label_left_Food.grid(row=4, column=0, pady=(15, 5), padx=(130, 5), sticky="e")

entry_left_Food = tk.Entry(root, font=("Times New Roman", 12), validate="key", validatecommand=(validate, '%P'))
entry_left_Food.grid(row=4, column=1, pady=(15, 5), padx=(30, 5), sticky="w")
label_left_FoodDesc = tk.Label(root, text="* Expenses such as groceries and dine-in:", font=("Times New Roman", 10),fg="#D0C395", bg='#9A162B')
label_left_FoodDesc.grid(row=5, column=1, pady=(0, 5), sticky="w")

# Transport Entries
label_left_Transport = tk.Label(root, text="Transportation:", font=("Times New Roman", 12),fg="#D0C395", bg='#9A162B')
label_left_Transport.grid(row=6, column=0, pady=(15, 5), padx=(130, 5), sticky="e")
entry_left_Transport = tk.Entry(root, font=("Times New Roman", 12), validate="key", validatecommand=(validate, '%P'))
entry_left_Transport.grid(row=6, column=1, pady=(15, 5), padx=(30, 5), sticky="w")
label_left_TransportDesc = tk.Label(root, text="* Expenses such as gas, insurance and car-note.", font=("Times New Roman", 10),fg="#D0C395", bg='#9A162B')
label_left_TransportDesc.grid(row=7, column=1, pady=(0, 5), sticky="w")

# School Supplies Entries
label_left_SchoolSupplies = tk.Label(root, text="School Supplies:", font=("Times New Roman", 12),fg="#D0C395", bg='#9A162B')
label_left_SchoolSupplies.grid(row=8, column=0, pady=(15, 5), padx=(130, 5), sticky="e")
entry_left_SchoolSupplies = tk.Entry(root, font=("Times New Roman", 12), validate="key", validatecommand=(validate, '%P'))
entry_left_SchoolSupplies.grid(row=8, column=1, pady=(15, 5), padx=(30, 5), sticky="w")
label_left_SchoolSuppliesDesc = tk.Label(root, text="* Expenses such as books and supplies:", font=("Times New Roman", 10),fg="#D0C395", bg='#9A162B')
label_left_SchoolSuppliesDesc.grid(row=9, column=1, pady=(0, 5), sticky="w")

# Rightsided Expenses and Entries
#-----------------------------------------------------------------
# Entertainment Entries
label_right_Entertainment = tk.Label(root, text="Entertainment:", font=("Times New Roman", 12),fg="#D0C395", bg='#9A162B')
label_right_Entertainment.grid(row=2, column=2, pady=(80, 5), padx=(10, 5), sticky="e")
entry_right_Entertainment = tk.Entry(root, font=("Times New Roman", 12), validate="key", validatecommand=(validate, '%P'))
entry_right_Entertainment.grid(row=2, column=3, pady=(80, 5), padx=(30, 5), sticky="w")
label_right_Entertainment_desc = tk.Label(root, text="* Expenses such as Nightclub/Parties:", font=("Times New Roman", 10),fg="#D0C395", bg='#9A162B')
label_right_Entertainment_desc.grid(row=3, column=3, pady=(0, 5), sticky="w")

# Personal Care Entries
label_right_Care = tk.Label(root, text="Personal-Care:", font=("Times New Roman", 12),fg="#D0C395", bg='#9A162B')
label_right_Care.grid(row=4, column=2, pady=(20, 5), padx=(10, 5), sticky="e")
entry_right_Care = tk.Entry(root, font=("Times New Roman", 12), validate="key", validatecommand=(validate, '%P'))
entry_right_Care.grid(row=4, column=3, pady=(20, 5), padx=(30, 5), sticky="w")
label_right_Care_desc = tk.Label(root, text="* Expenses such as lotions/shampoo:", font=("Times New Roman", 10),fg="#D0C395", bg='#9A162B')
label_right_Care_desc.grid(row=5, column=3, pady=(0, 5), sticky="w")

# Technology Entries
label_right_Technology = tk.Label(root, text="Technology:", font=("Times New Roman", 12), fg="#D0C395",bg='#9A162B')
label_right_Technology.grid(row=6, column=2, pady=(20, 5), padx=(10, 5), sticky="e")
entry_right_Technology = tk.Entry(root, font=("Times New Roman", 12), validate="key", validatecommand=(validate, '%P'))
entry_right_Technology.grid(row=6, column=3, pady=(20, 5), padx=(30, 5), sticky="w")
label_right_Technology_desc = tk.Label(root, text="* Expenses such as computers/phones:", font=("Times New Roman", 10),fg="#D0C395", bg='#9A162B')
label_right_Technology_desc.grid(row=7, column=3, pady=(0, 5), sticky="w")

# Miscellaneous
label_right_Miscellaneous = tk.Label(root, text="Miscellaneous:", font=("Times New Roman", 12),fg="#D0C395", bg='#9A162B')
label_right_Miscellaneous.grid(row=8, column=2, pady=(20, 5), padx=(10, 5), sticky="e")
entry_right_Miscellaneous = tk.Entry(root, font=("Times New Roman", 12), validate="key", validatecommand=(validate, '%P'))
entry_right_Miscellaneous.grid(row=8, column=3, pady=(20, 5), padx=(30, 5), sticky="w")
label_right_Miscellaneous_desc = tk.Label(root, text="* Include other expenses:", font=("Times New Roman", 10),fg="#D0C395", bg='#9A162B')
label_right_Miscellaneous_desc.grid(row=9, column=3, pady=(0, 5), sticky="w")


# Monthly Income Calculator
#-----------------------------------------------------------------

string_Expenses = ("Monthly Income/Expense Limit:  $" + str(data[1][5]))


# Additional Label
label_left_expenseCalculator = tk.Label(root, text=string_Expenses, font=("Times New Roman", 12),fg="#D0C395", bg='#9A162B')
label_left_expenseCalculator.grid(row=10, column=1, pady=(45, 5), padx=(5, 5), sticky="w")

# Buttons
button1 = tk.Button(root, text="Submit", font=("Times New Roman", 15),fg="#D0C395",  borderwidth=0, width=130, height=35, compound="center", 
                    image=background_image_button, relief="flat", command=calculateExpenses)
button1.grid(row=10, column=2, pady=(45, 5), padx=(5, 5), sticky="w")


# Start the main event loop
root.mainloop()