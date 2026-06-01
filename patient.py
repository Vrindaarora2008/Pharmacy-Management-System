from utils import ensure_file
def add_patient():
    ensure_file("patients.txt")
    try:
        name = input("Patient name\n")
        age = int(input("Age\n"))
        phone = input("Phone\n")
        with open("patients.txt", "r") as file:
            pid = len(file.readlines()) + 1
        with open("patients.txt", "a") as file:
            file.write(f"{pid},{name},{age},{phone}\n")
        print(" Patient added successfully.")
    except ValueError:
        print(" Invalid input.")

def view_patients():
    ensure_file("patients.txt")
    with open("patients.txt", "r") as file:
        lines = file.readlines()
        if not lines:
            print("No patients found. Kindly check in the hospital behind us.")
            return
        for line in lines:
            d = line.strip().split(",")
            print(f"ID:{d[0]} | Name:{d[1]} | Age:{d[2]} | Phone:{d[3]}")