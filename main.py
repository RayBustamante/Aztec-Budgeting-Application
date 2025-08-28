import tkinter as tk
from tkinter import messagebox
import subprocess
import sys
import os
import csv
import cv2

from numpy import False_


# Video Loading Screen
#-----------------------------------------------------------------

try:
    #assign videoSCreen with file name
    videoScreen = cv2.VideoCapture("Loading_Screen.mp4")
    
    # prints error if file not found
    if not videoScreen.isOpened():
        raise IOError("Cannot open video file.")

    # create the video window frame
    while True:
        ret, frame = videoScreen.read()
        if not ret:
            break
        cv2.imshow("Loading Screen", frame)
        
        # waits and allows ot quit early
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
    # plays video and destroy video when finished
    videoScreen.release()
    cv2.destroyAllWindows()

except Exception as e:
    print("Error has occured!!:" + str(e))
# GUI and Button Function
#-----------------------------------------------------------------
string_Text = " "

# intialized variables for load file option.
name = None
age = None
major = None
year = None
file_path = "studentUser_newFile.csv"
data = []

# If new file is clicked start creation process
def button_newFile():
    label_below_button1.configure(text="Loading...")

    try:
      subprocess.Popen([sys.executable, "main_newFile.py"])
      sys.exit()
    except Exception as e:
      print("An error occurred:", e)
    

# If load file is clicked, check if all essential account data in local csv is filled.
def checkIfAccountFilled(file_path):

    global data
    with open(file_path, mode='r', newline='') as file:
      reader = csv.reader(file)
      for row in reader:
        data.append(row)
          
    if data[1][19] == "" or data[1][19] == None:
      print("No account found")
      return False
    else:
      return True
    
# load the csv file containing user data
def button_loadFile():
  file_path = "studentUser_newFile.csv" 

  global name
  global age
  global major
  global year
  global data

  #check to see if an account exist
  if os.path.isfile("studentUser_newFile.csv"):
    #check to see if the account is filled
    if checkIfAccountFilled(file_path):
      global data
      #retrieve the data
      name = data[1][18]
      age = data[1][1]
      major = data[1][3]
      year = data[1][4]
    
        # display the results and confirm.
      displayText = ("Is this your account? "
        + " " +
       "\n \n Student Name: " + str(name) + 
       "\n Age: " + str(age) + " "
       "\n School Year: " + str(major) + " "
       "\n Major: " + str(year) + " ")
      
      result = messagebox.askyesno("Account Found!", displayText)

      # Check the result
      if result:
        subprocess.Popen([sys.executable, "main_newFile_Menu.py"])
        sys.exit()

      else:
          print("Restarting...")
    else:
      messagebox.showerror("Error", "The account file appears incomplete. Please create a new account.")
  else:
    messagebox.showerror("Error", "No account has been created yet. Please create an account using the New File button.")


root = tk.Tk()
root.title("Menu")


root.geometry("1274x714")

# Background
#-----------------------------------------------------------------
background_image2 = tk.PhotoImage(file="Aztec_Menu_Background.png")
background_image = tk.PhotoImage(file="button_background_red.png")

background_label = tk.Label(root, image=background_image2)
background_label.place(relwidth=1, relheight=1)

# Buttons and Labels
#-----------------------------------------------------------------

label = tk.Label(root, text="Aztec Student \n Budgeting Tool", font=("Times New Roman", 45),fg="#D0C395",  bg='#9A162B')
label.pack(pady=(230, 10))

button1 = tk.Button(root, text="New File", font=("Times New Roman", 15), command=button_newFile, fg="#D0C395", 
                    borderwidth=0, width=130, height=35, compound="center", 
                    image=background_image, relief="flat")
button1.pack(pady=(20, 5), padx=30) 

button2 = tk.Button(root, text="Load File", font=("Times New Roman", 15), fg="#D0C395",
                    borderwidth=0, width=130, height=35, compound="center", 
                    image=background_image, relief="flat", command=button_loadFile)
button2.pack(pady=(20, 5), padx=30) 

label_below_button1 = tk.Label(root, text=string_Text, bg='#9A162B')
label_below_button1.pack(pady=(30, 10)) 

label_below_button2 = tk.Label(root, text="Version: 1.0 \n", bg='#9A162B')
label_below_button2.pack(pady=(30, 10)) 

root.mainloop()
