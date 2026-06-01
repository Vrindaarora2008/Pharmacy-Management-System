from utils import ensure_file
def add_medicine():
    ensure_file("medicines.txt")
    try:
        name = input("Medicine name\n")
        category = input("Category\n")
        price = float(input("Price\n"))
        quantity = int(input("Quantity\n"))
        expiry = input("Expiry date\n ")
        with open("medicines.txt", "r") as file:
            med_id = len(file.readlines()) + 1
        with open("medicines.txt", "a") as file:
            file.write(f"{med_id}   {name}   {category}   {price}   {quantity}   {expiry}\n")
        print("Medicine added successfully.")
    except ValueError:
        print("Invalid input.")

def view_medicines():
    ensure_file("medicines.txt")
    with open("medicines.txt", "r") as file:
        lines = file.readlines()
        if not lines:
            print("No medicines available. Wait for it to restock.")
            return
        for line in lines:
            d = line.strip().split("   ")
            print(f"ID:{d[0]} | Name:{d[1]} | Price:{d[3]} | Qty:{d[4]}")

def search_medicine():
    name = input("Enter medicine name\n").lower()
    ensure_file("medicines.txt")
    found = False

    with open("medicines.txt", "r") as file:
        for line in file:
            d = line.strip().split("   ")
            if d[1].lower() == name:
                print("Found:", d)
                found = True
    if not found:
        print("Medicine not found. Kindly forgive us for the inconvenience.\n")

def low_stock_alert():
    ensure_file("medicines.txt")
    print("\nLow stock medicines:")
    with open("medicines.txt", "r") as file:
        for line in file:
            d = line.strip().split("   ")
            if int(d[4]) < 5:
                print(d[1], "| Qty:", d[4])