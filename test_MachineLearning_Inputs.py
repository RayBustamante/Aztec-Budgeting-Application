import tkinter as tk
import csv

# Program that helps input categorization and description into machine learning dataset at a much faster pace
# than manual inputs.

def split_and_append():
    
    word_list = []
    user_input = entry1.get()
    category = selected_category.get()
    
    
    words = user_input.split(",")
    
    word_list.extend(words)
    
    for word in word_list:
        append_to_csv(word, category)
        
    print("Success! Data has been written into dataset for machine learning model")
    
def append_to_csv(word, category):
    with open("machineLearning_Dataset.csv", 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([word, category])
        print(word, category)

# Create the main window
root = tk.Tk()
root.title("String Inputs")

# Create a title label
title_label = tk.Label(root, text="Program that makes it easier to input data for Machine Learning csv file:")
title_label.grid(row=0, column=0, columnspan=2, padx=10, pady=5)

label1 = tk.Label(root, text="Enter as many words of objects seperated by a comma. Also, make it all one category type:")
label1.grid(row=1, column=0, padx=10, pady=5)
label2 = tk.Label(root, text="Select a single category for all these objects:")
label2.grid(row=2, column=0, padx=10, pady=5)


entry1 = tk.Entry(root, width=30)
entry1.grid(row=1, column=1, padx=10, pady=5)

categories = [
    "Food",
    "Housing",
    "Transportation",
    "School Supplies",
    "Entertainment",
    "Personal Care",
    "Technology",
    "Miscellaneous"
]

# Create a variable to store the selected category
selected_category = tk.StringVar(root)
selected_category.set(categories[0])

category_dropdown = tk.OptionMenu(root, selected_category, *categories)
category_dropdown.grid(row=2, column=1, padx=10, pady=5)

submit_button = tk.Button(root, text="Submit", command=split_and_append)
submit_button.grid(row=3, column=0, columnspan=2, pady=10)

# Run the main event loop
root.mainloop()
