from datetime import date
from utils import ensure_file
def sell_medicine():
    ensure_file("medicines.txt")
    ensure_file("sales.txt")
    name = input("Medicine name\n").lower()
    qty = int(input("Quantity\n"))
    medicines = []
    sold = False
    total = 0
    with open("medicines.txt", "r") as file:
        medicines = file.readlines()
    with open("medicines.txt", "w") as file:
        for line in medicines:
            d = line.strip().split(",")
            if d[1].lower() == name:
                stock = int(d[4])
                if stock >= qty:
                    stock -= qty
                    total = qty * float(d[3])
                    sold = True
                d[4] = str(stock)
            file.write(",".join(d) + "\n")
    if sold:
        with open("sales.txt", "a") as file:
            file.write(f"{name},{qty},{total},{date.today()}\n")
        print("Sale successful.")
        print("Total bill- Rs.", total)
    else:
        print("Sale failed. Not enough stock.")