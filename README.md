# 🏛️ Aztec Budgeting Application
**by Ramon C. Bustamante**

A Python-based personal finance tool designed for students. It combines machine learning, data analysis, and an intuitive UI to help users understand and improve their spending habits—while comparing them to a broader dataset of peers.

> 🎓 Built as a final undergraduate project to showcase skills in Python, APIs, data science, and machine learning.

---

## 💼 Overview

The **Aztec Budgeting Application** is a smart budgeting assistant that:

- Tracks personal income and expenses
- Analyzes spending categories using a Support Vector Machine (SVM) model
- Compares your financial data against a student peer dataset using **Pandas**
- Generates visual insights with **Matplotlib**
- Provides **dynamic, AI-generated financial advice** via the OpenAI API

All within a fully functional **graphical interface**.

---

## 🧠 Key Features

### ✅ Account Creation
- Set up a local student profile
- Input monthly income, account info, and fixed expenses
- Data is saved locally and reused across sessions

### 📊 Expense Tracker
- Accessed through the **Tools Menu**
- Includes:
  - **Chatbox Interface** to log and review expenses
  - **Automated Expense Categorization** using an SVM model
  - **Budget Log**: Automatically saved and updated on every new entry

### 📈 Data Analysis & Visualization
- Uses **Pandas** to analyze your expenses relative to peer data
- Dynamically generates a **Matplotlib regression chart**
- Plots your financial position in comparison to other students

### 🧾 Financial Advice
- Upon analysis completion, generates tailored advice
- Advice is created via OpenAI API based on your current spending trends
- Saves a document summarizing:
  - Income
  - Expenses
  - Spending breakdown
  - Personalized financial recommendations

---

## ⚙️ Technologies Used

| Library / API     | Purpose                               |
|-------------------|---------------------------------------|
| `pandas`          | Data analysis and comparison          |
| `matplotlib`      | Graph creation and visualization      |
| `sklearn` (SVM)   | Expense categorization (ML model)     |
| `openai` API      | Dynamic financial advice generation   |
| `tkinter`         | GUI for user input and tool menus     |
| `os` / `csv`      | File handling and data persistence    |

---

## 🧪 How to Run

1. **Download the full project folder**  
2. Ensure all dependencies are installed:
   ```bash
   pip install pandas matplotlib scikit-learn openai

bash
Aztec-Budgeting-Application/

main.py                # Entry point of the application
user_data.csv          # Local user data file
budget_log.txt         # Saved expense chat log
assets/                # Optional folder for UI icons or images
requirements.txt       #(Optional) Dependency list

