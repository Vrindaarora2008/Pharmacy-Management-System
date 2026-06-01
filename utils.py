import os
def ensure_file(filename):
    try:
        open(filename, "r").close()
    except FileNotFoundError:
        open(filename, "w").close()
def pause():
    input("\nPress Enter to continue...")
def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")