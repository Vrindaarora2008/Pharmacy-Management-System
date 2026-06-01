Pharmacy Management System (Python CLI)
A simple Pharmacy Management System built using Python that helps manage medicines, patients, and sales using a command-line interface.
The system uses text files for storage and is divided into multiple modules for better organization and readability.

📌 Features
🧾 Medicine Management

Add new medicines (name, category, price, quantity, expiry) [upesstd-my...epoint.com]
View all medicines with ID, price, and quantity [upesstd-my...epoint.com]
Search medicines by name [upesstd-my...epoint.com]
Low stock alert (quantity < 5) [upesstd-my...epoint.com]


🧑‍⚕️ Patient Management

Add patient details (name, age, phone) [upesstd-my...epoint.com]
View all patient records [upesstd-my...epoint.com]


💰 Sales System

Sell medicines and calculate total bill [upesstd-my...epoint.com]
Automatically reduces stock after sale [upesstd-my...epoint.com]
Stores sales data with date in sales.txt [upesstd-my...epoint.com]


⚙️ Utility Functions

Automatic file creation if missing [upesstd-my...epoint.com]
Pause between operations for better UX [upesstd-my...epoint.com]
Clear console screen for cleaner interface [upesstd-my...epoint.com]


🛠️ Tech Stack

Language: Python
Interface: Command Line (CLI)
Storage: Text files (.txt)
Concepts Used:

Modular Programming (multiple .py files)
File Handling
Exception Handling
Basic Data Processing




📂 Project Structure
pharmacy-management-system/
│
├── main.py          # Main menu & program execution
├── medicine.py      # Medicine management functions
├── patient.py       # Patient management functions
├── sales.py         # Selling and billing logic
├── utils.py         # Helper functions
│
├── medicines.txt    # Stores medicine records
├── patients.txt     # Stores patient records
├── sales.txt        # Stores sales history
│
└── README.md


🚀 How to Run

Install Python:

Shellpython --versionShow more lines

Run the program:

Shellpython main.pyShow more lines

📊 Menu Options
When you run the program, you'll see:
PHARMACY MANAGEMENT SYSTEM

1. Add Medicine
2. View Medicines
3. Search Medicine
4. Low Stock Alert
5. Add Patient
6. View Patients
7. Sell Medicine
8. Exit

 [upesstd-my...epoint.com]

📦 Data Storage Format
Medicines (medicines.txt)
ID   Name   Category   Price   Quantity   Expiry

Patients (patients.txt)
ID,Name,Age,Phone

 [upesstd-my...epoint.com]
Sales (sales.txt)
MedicineName,Quantity,TotalPrice,Date

 [upesstd-my...epoint.com]

⚠️ Known Limitations
No database (uses plain text files)
No GUI (CLI only)
Limited validation of user input
File formatting inconsistency (spaces vs commas)


⚙️ Future Improvements
Add graphical interface (Tkinter / PyQt)
Use SQLite or MySQL instead of text files
Add login/authentication system
Generate formatted invoices
Improve data validation & error handling
Fix delimiter consistency across files
