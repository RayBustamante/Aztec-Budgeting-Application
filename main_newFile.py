import tkinter as tk
from tkinter import messagebox

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

import subprocess
import sys
import csv
import os

#-----------------------------------------------------------------
# by Ramon C Bustamante
#-----------------------------------------------------------------

# global variables
overTimePay = 0
overTime_Hours = 0
netPay = 0.0

def button_calculatePay():

  # retrieve user input
  overTimePay = 0
  payInput = pay_entry.get()
  hourInput = hours_entry.get()
  salaryInput = salary_Entry.get()


  # if pay and hour values are both filled and numeric
  if (payInput != "" and hourInput != "") and (payInput.isnumeric() and hourInput.isnumeric() ):
    
    hourInput = int(hourInput)

    # If hour is greater than 40, do overtime calculation
    if int(hourInput) > 40:
      overTimePay = (float(hourInput) - 40.0) * (float(payInput) * 1.5)
      overTime_Hours = int(hourInput) - 40
      stringOvertime = "Overtime Hours: " + str(overTime_Hours) + " Hours" + "\n" + "Overtime Pay: $" + str(overTimePay)
      messagebox.showinfo("Overtime Pay!", stringOvertime)
      hourInput = int(hourInput - overTime_Hours)
      
    salaryYear = (int(payInput) * hourInput) * 52
    floatValue = float(salaryYear)
    tax_Calculator(floatValue, overTimePay)

  # If salary values are both filled and numeric
  elif (salaryInput != "") and (salaryInput.isnumeric() ):
    
    floatValue = float(salaryInput)
    tax_Calculator(floatValue, overTimePay)

  # If any entry is either empty or not numeric
  else:
    messagebox.showerror("Invalid Input!", "Please enter a numeric value in either Hourly Pay or Salary")
    pay_entry.delete(0, 'end')
    hours_entry.delete(0, 'end')
    salary_Entry.delete(0, 'end')
    
def tax_Calculator(floatValue, overTimePay):
  global netPay
  netPay = 0
  pieChartList = [20.0, 20.0, 20.0, 20.0, 20.0]
  yearlySalary = int(floatValue)

  # Calculate Overtime if Exist
  overTimePay = overTimePay * 52.0
  monthly_overTimePay = overTimePay / 12.0
  monthly_newValue = (floatValue / 12.0) + monthly_overTimePay
  

  # Display Monthly Income
  moneyValue = ('$' + format(monthly_newValue, ',.2f'))
  monthly_Pay_Label_Output.configure(text=moneyValue)
  netPay = netPay + monthly_newValue

  # Calculate Income Tax and append to list
  incomeTaxPercentage = incomeTax_Calculator(yearlySalary)
  incomeTax = float(monthly_newValue) * float(incomeTaxPercentage)  
  moneyValue = ('$' + format(incomeTax, ',.2f'))
  income_Tax_Label_Output.configure(text=moneyValue)
  netPay = netPay - incomeTax  
  pieChartList[0] = (incomeTax/monthly_newValue) * 100

  # Medicare Tax and append to list
  medicareTax = float(monthly_newValue) * 0.0145
  moneyValue = ('$' + format(medicareTax, ',.2f'))
  income_Med_Label_Output.configure(text=moneyValue)
  netPay = netPay - medicareTax
  medicareTaxRound = round((medicareTax/monthly_newValue) * 100, 2)
  pieChartList[1] = medicareTaxRound
  
  # Social Security Tax and append to list
  socialSecurityTax = float(monthly_newValue) * 0.062
  moneyValue = ('$' + format(socialSecurityTax, ',.2f'))
  income_SSTax_Label_Output.configure(text=moneyValue)
  netPay = netPay - socialSecurityTax
  socialSecurityTaxRound = round((socialSecurityTax/monthly_newValue) * 100, 2)

  pieChartList[2] = socialSecurityTaxRound

  # CA State Tax and append to list
  stateTax = californiaTax_Calculator(yearlySalary)
  californiaTax = float(monthly_newValue) * float(stateTax)
  moneyValue = ('$' + format(californiaTax, ',.2f'))
  income_CATax_Label_Output.configure(text=moneyValue)
  netPay = netPay - stateTax
  pieChartList[3] = stateTax * 100

  # Display Net Monthly Pay
  moneyValue = ('$' + format(netPay, ',.2f'))
  income_Net_Label_Output.configure(text=moneyValue)

  # Calculator the remainder percentage and append
  remainder_percentage = float(100) - float(pieChartList[0] + pieChartList[1] + pieChartList[2] + pieChartList[3])
  pieChartList[4] = remainder_percentage

  # Create a Figure and Axes object
  fig, ax = plt.subplots(figsize=(7, 7))

  # Set the background color of the figure
  fig.set_facecolor('#9A162B')

  # Explode settings for the pie chart
  explode = (0, 0, 0, 0, 0.1) 

  # Define custom colors for the pie chart
  colors = ['#DAF7A6', '#E74C3C', '#FF5733', 'white', 'red']

  ax.set_title('Tax Distribution', fontsize=30)


  # Create the pie chart with custom colors
  ax.pie(pieChartList, labels=['Income Tax', 'Medicare Tax', 'Social Security Tax', 'California Tax', 'Net Pay'],
         autopct='%.2f%%', explode=explode, colors=colors, shadow=True, startangle = 180)

  # Create a canvas to display the pie chart in Tkinter window
  canvas = FigureCanvasTkAgg(fig, master=root)
  canvas.draw()
  canvas.get_tk_widget().grid(row=0, column=2, rowspan=15, padx=2, pady=2)  # Place the canvas in the Tkinter window


  # Next Button
  #-----------------------------------------------------------------
  button1 = tk.Button(root, text="Confirm", font=("Times New Roman", 15), 
                      command=saveIncomeToCSV, borderwidth=0, width=130, height=35, compound="center", 
                      image=background_image_button, relief="flat")
  button1.grid(row=12, column=2, columnspan=2, padx=(55, 20), pady=(5,5))

def incomeTax_Calculator(yearlySalary):
    #retrieve tax based on income
  if yearlySalary > 0 and yearlySalary <= 11600:
    return 0.10
  elif yearlySalary > 11601 and yearlySalary <= 47150:
    return 0.12
  elif yearlySalary > 47151 and yearlySalary <= 100526:
    return 0.22
  elif yearlySalary > 100527 and yearlySalary <= 191950:
    return 0.24
  elif yearlySalary > 191951 and yearlySalary <= 243725:
    return 0.32
  elif yearlySalary > 243726 and yearlySalary <= 609350:
    return 0.35
  else:
    return 0.37

def californiaTax_Calculator(yearlySalary):
    #retrieve tax based on income
  
  if yearlySalary > 0 and yearlySalary <= 10412:
    return 0.01
  elif yearlySalary > 10413 and yearlySalary <= 24684:
    return 0.02
  elif yearlySalary > 24685 and yearlySalary <= 38959:
    return 0.04
  elif yearlySalary > 38960 and yearlySalary <= 54081:
    return 0.06
  elif yearlySalary > 54082 and yearlySalary <= 68350:
    return 0.08
  elif yearlySalary > 68351 and yearlySalary <= 349137:
    return 0.093
  else:
    return 0.103
  
def saveIncomeToCSV():
    #save the data into local csv file
    global netPay
    filename = "studentUser_newFile.csv"

    if os.path.exists(filename):
        os.remove(filename)
  
    with open(filename, 'w', newline='') as file:
        # Create a CSV writer object
        writer = csv.writer(file)
        # Write header row
        writer.writerow(["", "age", "gender", "year_in_school", "major", "monthly_income", 
                         "financial_aid", "tuition", "housing", "food", "transportation", 
                         "books_supplies", "entertainment", "personal_care", "technology", 
                         "health_wellness", "miscellaneous", "preferred_payment_method", "name", "expenditure"])
        # Write empty row
        writer.writerow([""] * 20)  # Writing 19 empty values for the next row

    with open(filename, 'r', newline='') as file:
      reader = csv.reader(file)
      data = list(reader)

    # Update the value in row 2, column 6
    data[1][5] = int(netPay)

    # Write the updated data back to the CSV file
    with open(filename, 'w', newline='') as file:
      writer = csv.writer(file)
      writer.writerows(data)

    messagebox.showinfo("New User!", "Creating new account file...")
        
    button1.destroy()
  
    nextButton = tk.Button(root, text="Next", font=("Times New Roman", 15), 
                        command=nextPage(), borderwidth=0, width=130, height=35, compound="center", 
                        image=background_image_button, relief="flat")
    nextButton.grid(row=12, column=2, columnspan=2, padx=(55, 20), pady=(5,5))

def nextPage():
  try:
    subprocess.Popen(["python", "main_newFile_PersonalInfo.py"])
    sys.exit()
  except subprocess.CalledProcessError as e:
    print("Error occurred while running the Python file:", e)

# Create GUI Window
#-----------------------------------------------------------------
root = tk.Tk()
root.title("Input Form")
root.geometry("1274x714")

# Create Background Image
#-----------------------------------------------------------------
background_image2 = tk.PhotoImage(file="Aztec_Menu_Background_Empty.png")
background_label = tk.Label(root, image=background_image2)
background_label.place(relwidth=1, relheight=1)

background_image_button = tk.PhotoImage(file="button_background_red.png")

# Pay and Hourly Inputs/Labels
#-----------------------------------------------------------------
incomeTitle_label = tk.Label(root, text="Income Calculator", font=("Times New Roman", 38),fg="#D0C395", bg='#9A162B')
incomeTitle_label.grid(row=0, column=0, columnspan=2, pady=(50, 10))

incomeTitle_label2 = tk.Label(root, text="To begin creating a budget, we need to calculate your monthly income. \n Please enter either your hourly pay or your yearly salary.", font=("Times New Roman", 10),fg="#D0C395", bg='#9A162B')
incomeTitle_label2.grid(row=1, column=0, columnspan=2, pady=(10, 10))

pay_label = tk.Label(root, text="Pay:", font=("Times New Roman", 18),fg="#D0C395", bg='#9A162B')
pay_label.grid(row=2, column=0, padx=(150, 5), pady=(20, 10), sticky="w")

pay_entry = tk.Entry(root)
pay_entry.grid(row=2, column=1, sticky="w")

hours_label = tk.Label(root, text="Hours:", font=("Times New Roman", 18),fg="#D0C395", bg='#9A162B')
hours_label.grid(row=3, column=0, padx=(150, 5), pady=(10, 10), sticky="w")

hours_entry = tk.Entry(root)
hours_entry.grid(row=3, column=1, sticky="w")

or_Label = tk.Label(root, text="--OR--", font=("Times New Roman", 18),fg="#D0C395", bg='#9A162B')
or_Label.grid(row=4, column=0, columnspan=2, pady=(10, 10))

# Salary Inputs/Labels
#-----------------------------------------------------------------
salary_Label = tk.Label(root, text="Salary:", font=("Times New Roman", 18),fg="#D0C395", bg='#9A162B')
salary_Label.grid(row=5, column=0, padx=150, pady=(10, 5), sticky="w")

salary_Entry = tk.Entry(root)
salary_Entry.grid(row=5, column=1, sticky="w")

# Calculator Button
#-----------------------------------------------------------------

button1 = tk.Button(root, text="Calculate", font=("Times New Roman", 15),fg="#D0C395", command=button_calculatePay, 
                    borderwidth=0, width=130, height=35, compound="center", 
                    image=background_image_button, relief="flat")
button1.grid(row=6, column=0, columnspan=2, padx=10, pady=20)



# Tax Calculator Visualization
#-----------------------------------------------------------------
monthly_Pay_Label = tk.Label(root, text="Gross Monthly Pay:" , font=("Times New Roman", 12),fg="#D0C395", bg='#9A162B')
monthly_Pay_Label.grid(row=7, column=0, columnspan=2, padx=220, pady=(5, 5), sticky="w")

monthly_Pay_Label_Output = tk.Label(root, text="$0.00" , font=("Times New Roman", 12),fg="#D0C395", bg='#9A162B')
monthly_Pay_Label_Output.grid(row=7, column=1, columnspan=2, padx=(50, 20), pady=(5, 5), sticky="w")
#-----------------------------------------------------------------

income_Tax_Label = tk.Label(root, text="Federal Income Tax:" , font=("Times New Roman", 12),fg="#D0C395", bg='#9A162B')
income_Tax_Label.grid(row=8, column=0, columnspan=2, padx=220, pady=(5, 5), sticky="w")

income_Tax_Label_Output = tk.Label(root, text="$0.00" , font=("Times New Roman", 12),fg="#D0C395", bg='#9A162B')
income_Tax_Label_Output.grid(row=8, column=1, columnspan=2, padx=(50, 20), pady=(5, 5), sticky="w")
#-----------------------------------------------------------------

income_Med_Label = tk.Label(root, text="Federal Medicare Tax:" , font=("Times New Roman", 12),fg="#D0C395", bg='#9A162B')
income_Med_Label.grid(row=9, column=0, columnspan=2, padx=220, pady=(5, 5), sticky="w")

income_Med_Label_Output = tk.Label(root, text="$0.00" , font=("Times New Roman", 12),fg="#D0C395", bg='#9A162B')
income_Med_Label_Output.grid(row=9, column=1, columnspan=2, padx=(50, 20), pady=(5, 5), sticky="w")

#-----------------------------------------------------------------

income_SSTax_Label = tk.Label(root, text="Social-Security Tax:" , font=("Times New Roman", 12),fg="#D0C395", bg='#9A162B')
income_SSTax_Label.grid(row=10, column=0, columnspan=2, padx=220, pady=(5, 5), sticky="w")

income_SSTax_Label_Output = tk.Label(root, text="$0.00" , font=("Times New Roman", 12),fg="#D0C395", bg='#9A162B')
income_SSTax_Label_Output.grid(row=10, column=1, columnspan=2, padx=(50, 20), pady=(5, 5), sticky="w")
#-----------------------------------------------------------------

income_CATax_Label = tk.Label(root, text="CA State Tax:" , font=("Times New Roman", 12),fg="#D0C395", bg='#9A162B')
income_CATax_Label.grid(row=11, column=0, columnspan=2, padx=220, pady=(5, 5), sticky="w")

income_CATax_Label_Output = tk.Label(root, text="$0.00" , font=("Times New Roman", 12),fg="#D0C395", bg='#9A162B')
income_CATax_Label_Output.grid(row=11, column=1, columnspan=2, padx=(50, 20), pady=(5, 5), sticky="w")
#-----------------------------------------------------------------

income_Net_Label = tk.Label(root, text="Net Monthly Pay:" , font=("Times New Roman", 12),fg="#D0C395", bg='#9A162B')
income_Net_Label.grid(row=12, column=0, columnspan=2, padx=220, pady=(5, 5), sticky="w")

income_Net_Label_Output = tk.Label(root, text="$0.00" , font=("Times New Roman", 12),fg="#D0C395", bg='#9A162B')
income_Net_Label_Output.grid(row=12, column=1, columnspan=2, padx=(50, 20), pady=(5, 5), sticky="w")


# Start the main event loop
root.mainloop()