# Aztec-Budgeting-Application
by Ramon C. Bustamante

This is a student Python application that keeps track of user expense and uses a data analystic API such as Pandas to compare the current dataset with those of other students and provide detailed and dynamic financial advice for their current situation. 

It requires the creation of a local student account which will ask for the students income, account information and monthly expenses with a fully functional user interface for inputs and menu selection. 

Upon creation, the user may access the Tools Menu, which will contain the primary Expense Tracker program. The Expense Tracker interface will contain a chatbox which will contain an informative list of past and current expenses entered by the user. User inputs will be analyized based on which category of expenses the purchase best belongs to using a Support Vector Machine Model for categorical functions. Additionally, a budget log file containing the contents of a chatbox will be used to display the current purchases made to the user and will be saved to a local file that will be dynamically updated every time the user enters a new expense. Lastly, it will use Pandas to analyze the data provided with those of your peers and based on the comparison, will dynamically create a matlibplot graphical chart which shows the linear regression of the overall student body and your place within the graph. Upon completion of analysis, you may be able to save a document file containing all of your information along with financial advice dynamically tailored to your situation by the data provided by the user. The financial advice is created by using an API key from openAI.

This program was created as a final project for my undergraduate program and it is meant to demonstrate my capabilities in using python, API's, Data Analysis, Pandas, matlibplot and Machine Learning Models. 

To run, simply download the entire folder and  run the main.py file. An account would already have been made, allowing for the use of the Expense Tracking Tool in the tools menu.
