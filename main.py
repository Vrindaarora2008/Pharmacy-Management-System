from unittest import case
from medicine import *
from patient import *
from sales import *
from utils import pause, clear_screen
def main():
    while True:
        print("PHARMACY MANAGEMENT SYSTEM")
        print("1. Add Medicine")
        print("2. View Medicines")
        print("3. Search Medicine")
        print("4. Low Stock Alert")
        print("5. Add Patient")
        print("6. View Patients")
        print("7. Sell Medicine")
        print("8. Exit")
        choice = input("Enter choice\n")
        if choice == '1':
            add_medicine()
        elif choice == '2':
            view_medicines()
        elif choice == '3':
            search_medicine()
        elif choice == '4':
            low_stock_alert()
        elif choice == '5':
            add_patient()
        elif choice == '6':
            view_patients()
        elif choice == '7':
            sell_medicine()
        elif choice == '8':
            exit()
            break
        pause()
        clear_screen()

main()